# API Proxy

** Currently not working, making routing requests properly but not adding CORS headers **

This API proxy allows you to securely access any API using Flask-Cors for handling CORS headers. Intended to be used during front end development to bypass CORS. Very basic implementation meant to be used by my PDX Code Guild classmates.

## Usage

To use the API proxy, simply make a GET request to the endpoint `/proxy` with a query parameter `url` that contains the URL of the API you want to access. For example, to access the JSONPlaceholder API, you would make a request to `/proxy?url=https://jsonplaceholder.typicode.com/posts`.

You can also use this proxy by visiting the landing page of the service and entering the API URL in the form provided, then submit the form.

### Examples

- To access the JSONPlaceholder API:
 
/proxy?url=https://jsonplaceholder.typicode.com/posts


- To access the OpenWeatherMap API:
/proxy?url=https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY



## Security

Please note that this proxy server is for demonstration purpose only and it is not suitable for production use. You may want to add more robust error handling, security features and caching.
Also, for security reasons, it is not recommended to allow any origin in production environments, you should set the headers to specific values and use security measures like authentication and authorization.

## Installation

1. Clone this repository
git clone https://github.com/YOUR_USERNAME/API_proxy.git


2. Install the required dependencies
pip install -r requirements.txt


3. Run the script
python proxy.py

The proxy server will be running on `http://localhost:5000/`

## Additional Resources
- [Flask documentation](https://flask.palletsprojects.com/en/2.1.x/)
- [Flask-Cors documentation](https://flask-cors.readthedocs.io/en/latest/)
- [Requests documentation](https://requests.readthedocs.io/en/latest/)

## Support

In case you have any issues or questions, feel free to open an issue on the repository or contact me.

Aware of the following issues:

- CORS headers not being added to end API response


Please note that the above script and instructions are for demonstration purposes only and may not be suitable for production use. It's important to secure your API proxy and make sure to follow best practices for security, performance, and error handling.