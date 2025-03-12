from fastapi import Request
import logging
import httpx
from typing import Optional, Callable, Awaitable

# Set up logging
logger = logging.getLogger("OpenWebUIForwarder")
logging.basicConfig(level=logging.DEBUG)

# Remote Web API URL (Update with your actual production API endpoint)
REMOTE_API_URL = "<your api address:port"


class Pipe:
    """OpenWebUI-compatible Pipe class that forwards requests to the production API"""

    __current_event_emitter__: Callable[[dict], Awaitable[None]]

    def __init__(self):
        self.type = "structured_output"
        self.client = httpx.AsyncClient(timeout=360)
        logger.debug("Initialized OpenWebUI Forwarder Pipe")

    async def pipe(
        self,
        body: dict,
        __user__: dict,
        __event_emitter__: Optional[Callable[[dict], Awaitable[None]]] = None,
    ) -> str:
        """Forwards request to the production web API"""
        logger.debug(f"Forwarding request body: {body}")

        if not body.get("messages"):
            await self.emit_status("error", "No chat content found.", True)
            return "Error: No chat content."

        self.__current_event_emitter__ = __event_emitter__
        logger.debug("Emitting progress event")
        await self.progress("Forwarding request to remote API...")

        try:
            response = await self.client.post(f"{REMOTE_API_URL}/chat", json=body)
            response.raise_for_status()

            result = response.json()

            # Check for error responses
            if "error" in result:
                error_msg = result.get("error", "Unknown error")
                await self.emit_status("error", error_msg, True)
                return f"Error: {error_msg}"

            # Get standardized response
            message = result.get("response", "No response received.")

            logger.debug(f"Received response: {message}")
            # await self.emit_message(message)

            logger.debug("Emitting done event")
            await self.done()
            return message
        except Exception as e:
            logger.error(f"Error forwarding request: {e}")
            await self.emit_status("error", f"Error: {e}", True)
            return f"Error: {e}"

    async def progress(self, message: str):
        """Emits a progress update with status info"""
        logger.debug(f"Progress: {message}")
        await self.emit_status("info", message, False)

    async def done(self):
        """Signals process completion"""
        logger.debug("Processing complete.")
        await self.emit_status("info", "Processing complete.", True)

    async def emit_message(self, message: str):
        """Emits a message event with search results or AI-generated content"""
        if self.__current_event_emitter__:
            logger.debug(f"Emitting message: {message}")
            await self.__current_event_emitter__(
                {
                    "type": "message",
                    "data": {"content": message},
                }
            )

    async def emit_status(self, level: str, message: str, done: bool):
        """Emits a status event with current progress details"""
        if self.__current_event_emitter__:
            logger.debug(f"Emitting status: {message}")
            await self.__current_event_emitter__(
                {
                    "type": "status",
                    "data": {
                        "status": "complete" if done else "in_progress",
                        "level": level,
                        "description": message,
                        "done": done,
                    },
                }
            )
