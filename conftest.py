import pytest
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from pages.guvi_courses_page_after_login import GuviCoursesPageAfterLogin
from pages.guvi_courses_page_before_login import GuviCoursesPageBeforeLogin
from pages.guvi_landing_page import GuviLandingPage
from pages.guvi_login_page import GuviLoginPage
from pages.guvi_logout_page import GuviLogoutPage
from pages.guvi_signup_page import GuviSignupPage

config = dotenv_values(".env.test")


@pytest.fixture()
def credentials():
    return {"email": config.get("LOGIN_EMAIL"), "password": config.get("LOGIN_PASSWORD")}


@pytest.fixture()
def signup_info():
    return {"first_name": config.get("SIGNUP_FIRSTNAME"), "last_name": config.get("SIGNUP_LASTNAME"),
            "email": config.get("SIGNUP_EMAIL"), "password": config.get("SIGNUP_PASSWORD"),
            "mobile_number": config.get("SIGNUP_MOBILE")}


@pytest.fixture()
def signup_failed_info():
    return {"first_name": config.get("SIGNUP_FAILED_FIRSTNAME"), "last_name": config.get("SIGNUP_FAILED_LASTNAME"),
            "email": config.get("SIGNUP_FAILED_EMAIL"), "password": config.get("SIGNUP_FAILED_PASSWORD"),
            "mobile_number": config.get("SIGNUP_FAILED_MOBILE")}


@pytest.fixture(scope="module")
def web_driver():
    web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield web_driver
    web_driver.close()


@pytest.fixture(scope="module")
def landing_page(web_driver):
    landing_page = GuviLandingPage(web_driver)
    landing_page.browse()
    yield landing_page


@pytest.fixture(scope="module")
def login_page(web_driver):
    login_page = GuviLoginPage(web_driver)
    login_page.browse()
    yield login_page


@pytest.fixture(scope="module")
def logout_page(web_driver):
    logout_page = GuviLogoutPage(web_driver)
    logout_page.browse()
    yield logout_page


@pytest.fixture(scope="module")
def course_page_before_login(web_driver):
    course_page_before_login = GuviCoursesPageBeforeLogin(web_driver)
    course_page_before_login.browse()
    yield course_page_before_login


@pytest.fixture(scope="module")
def course_page_after_login(web_driver):
    course_page_after_login = GuviCoursesPageAfterLogin(web_driver)
    course_page_after_login.browse()
    yield course_page_after_login


@pytest.fixture(scope="module")
def signup_page(web_driver):
    signup_page = GuviSignupPage(web_driver)
    signup_page.browse()
    yield signup_page
