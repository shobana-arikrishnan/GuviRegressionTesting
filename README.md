# Guvi Portal Selenium Tests

## Setup

- Install Python 3.8+
- Create a `.env.test` file to set up the environment variables below before running the tests

```
LOOGIN_EMAIL="You Guvi Username"
LOGIN_PASSWORD="Your Guvi Portal Password"
SIGNUP_FIRSTNAME = "Correct FirstName"
SIGNUP_LASTNAME = "Correct LastName"
SIGNUP_EMAIL = "Correct Email address"
SIGNUP_PASSWORD = "Correct Password"
SIGNUP_MOBILE = "Correct Mobile Number"
SIGNUP_FAILED_FIRSTNAME = "Incorrect FirstName"
SIGNUP_FAILED_LASTNAME = "Incorrect LastName"
SIGNUP_FAILED_EMAIL = "Incorrect Email address"
SIGNUP_FAILED_PASSWORD = "Incorrect Password"
SIGNUP_FAILED_MOBILE = "Incorrect Mobile Number"
```

- Install dependencies

```bash
pip install -r requirements.txt
```

## Running tests

```bash
pytest -v
```