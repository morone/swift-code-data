
# SWIFT Code Data API

This project provides an API that fetches and returns data associated with a given SWIFT code. It is implemented in Python using Flask and BeautifulSoup for HTML parsing.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- Flask
- BeautifulSoup
- requests
- flasgger

### Installation

1. Clone this repository:

`git clone https://github.com/morone/swift-code-data.git`


2. Navigate into the project directory:

`cd swift-code-data-api`

3. Install the required Python packages:

`pip install -r requirements.txt`

## Running the Application

1. Run the application:

`python app.py`


2. The application will start running on `http://localhost:5000`.

## API Endpoints

- GET `/api/swift?code=<SWIFT_CODE>`: Fetches and returns data associated with the given SWIFT code.

## Swagger Documentation

The Swagger documentation for the API is available at `http://localhost:5000/apidocs`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
