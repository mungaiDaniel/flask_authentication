# Authenticating a Flask Api Using JSON Web Tokens(JWT)

    First, a user will have to login using a specially created route which returns a token. Once a token is generated, it can be sent along with the rest of the request to other parts of your API to verify the user's identity without the user having to provide any additional login information. It's an easy way to verify the identity of users without making them go through the extra step of logging in every time they make a request.

## Prerequisites

    1. python3
    2. flask
    3. jwt
    4. datetime
    5. functools(wraps)

## Getting Started

* Clone the repo by > git clone https://github.com/mungaiDaniel/flask_authentication.git
* Navigate into projects directory by > cd authentiction_using_JSON_tokens
* create a virtual environment by > virtualenv virtual
* Activate the virtual environment by > souce virtual/bin/activate
* Install the dependencies by > pip install -r requirements.txt
* run the app by > python3 app.py

## Author

    Daniel Mungai

## Reference

    pretty printed
