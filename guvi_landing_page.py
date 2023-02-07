from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class GuviLandingPage():
    url = 'https://www.guvi.in/'
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    logo_locator = 'head-guvi-logo'
    courses_link_locator = '/html/body/header/nav/div/div/div[2]/div[1]/ul/li[1]/a'
    login_link_locator = '/html/body/header/nav/div/div/div[2]/div[2]/ul/li[1]/a'
    signup_link_locator = '/html/body/header/nav/div/div/div[2]/div[2]/ul/li[2]/a'
    footer_locator = '/html/body/main/footer/div/div[2]/div[2]/div/div[2]/p'

    def browse(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        return self

    def get_title(self):
        return self.driver.title

    def get_logo(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=self.logo_locator)

    def get_course_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.courses_link_locator)

    def get_login_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.login_link_locator)

    def get_signup_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.signup_link_locator)

    def get_footer_text(self):
        return self.driver.find_element(by=By.XPATH, value=self.footer_locator)

    def close_browser(self):
        self.driver.quit()
