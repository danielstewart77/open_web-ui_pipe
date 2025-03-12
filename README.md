# OpenWebUI Forwarder Pipe

The `OpenWebUIForwarder` is a custom integration for OpenWebUI that enables users to forward chat messages to a specified Web API. By incorporating this Pipe class, you can create a model selection within OpenWebUI that seamlessly routes user inputs to your external API, allowing for customized processing and responses.

## Features

- **Seamless Integration**: Adds a model option in OpenWebUI that forwards chat messages to your specified Web API.
- **Asynchronous Processing**: Utilizes `httpx.AsyncClient` for non-blocking HTTP requests.
- **Structured Output**: Designed to handle structured responses compatible with OpenWebUI's requirements.

## Prerequisites

- OpenWebUI installed and running.
- Access to the OpenWebUI `models` directory.
- A Web API endpoint ready to receive and process chat messages.

## Installation

1. **Clone the Repository**: Clone or download the repository containing the `OpenWebUIForwarder` Pipe class to your local machine.

2. **Place the Pipe Script**: Copy the `OpenWebUIForwarder.py` script into the OpenWebUI `models` directory.

3. **Configure the Remote API URL**: Open the `OpenWebUIForwarder.py` file and set the `REMOTE_API_URL` variable to your Web API's address and port:

   ```python
   REMOTE_API_URL = "http://your-api-address:port"
   ```

4. **Restart OpenWebUI**: Restart the OpenWebUI service to recognize the new Pipe integration.

## Usage

1. **Access OpenWebUI**: Navigate to your OpenWebUI instance in a web browser.

2. **Select the Forwarder Model**: In the model selection dropdown, choose the model associated with the `OpenWebUIForwarder` Pipe.

3. **Initiate Chat**: Start a chat session. Messages sent will be forwarded to your specified Web API, and responses will be displayed within OpenWebUI.

## Customization

- **Logging**: The Pipe uses Python's `logging` module. Adjust the logging level as needed:

  ```python
  logging.basicConfig(level=logging.DEBUG)
  ```

- **Timeout Settings**: Modify the HTTP client timeout by changing the `timeout` parameter:

  ```python
  self.client = httpx.AsyncClient(timeout=360)
  ```

## Notes

- Ensure that your Web API is configured to handle the JSON structure sent by OpenWebUI and returns responses in the expected format.
- For detailed information on integrating custom models and Pipes, refer to the [OpenWebUI documentation](https://docs.openwebui.com/features/workspace/models/).

## Contributing

If you encounter issues or have suggestions for improvements, please open an issue or submit a pull request in the repository.

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

---

By following this guide, you can extend OpenWebUI's functionality to interact with external APIs, enabling customized processing and responses tailored to your specific requirements.

