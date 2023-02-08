# Guvi Portal Selenium Tests

## Setup

- Install Python 3.8+
- Create a `.env.test` file to set up the environment variables below before running the tests

```
LOOGIN_EMAIL="You Guvi Username"
LOGIN_PASSWORD="Your Guvi Portal Password"
```

- Install dependencies

```bash
pip install -r requirements.txt
```

## Running tests

```bash
pytest -v
```