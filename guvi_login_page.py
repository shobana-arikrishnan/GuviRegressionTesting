import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class GuviLoginPage():
    url = "https://www.guvi.in/sign-in"
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    email_locator = "login_email"
    password_locator = "login_password"
    login_locator = "login_button"

    def browse(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        return self

    def get_title(self):
        time.sleep(5)
        return self.driver.title

    def login(self, email, password):
        self.driver.find_element(by=By.ID, value=self.email_locator).send_keys(email)
        self.driver.find_element(by=By.ID, value=self.password_locator).send_keys(password)
        self.driver.find_element(by=By.ID, value=self.login_locator).click()