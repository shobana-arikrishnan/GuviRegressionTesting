import pytest
from dotenv import dotenv_values

from guvi_landing_page import GuviLandingPage
from guvi_login_page import GuviLoginPage

config = dotenv_values(".env.test")


@pytest.fixture()
def credentials():
    return {"email": config.get("LOGIN_EMAIL"), "password": config.get("LOGIN_PASSWORD")}


@pytest.fixture(scope="module")
def landing_page():
    landing_page = GuviLandingPage()
    landing_page.browse()
    yield landing_page
    landing_page.driver.close()


@pytest.fixture(scope="module")
def login_page():
    login_page = GuviLoginPage()
    login_page.browse()
    yield login_page
    login_page.driver.close()
