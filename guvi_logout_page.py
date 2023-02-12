import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class GuviLogoutPage():
    url = "https://www.guvi.in/sign-in"
    email_locator = "login_email"
    password_locator = "login_password"
    login_locator = "login_button"
    logout_dropdown_locator = '/html/body/header/nav/div[2]/button'
    logout_locator = 'signout'

    def __init__(self, driver):
        self.driver = driver

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

    def get_signout_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.logout_dropdown_locator)

    def logout(self):
        time.sleep(5)
        logout_dropdown_locator = self.driver.find_element(by=By.XPATH, value=self.logout_dropdown_locator)
        action = ActionChains(self.driver)
        action.click(on_element=logout_dropdown_locator).perform()
        time.sleep(3)
        self.driver.find_element(by=By.ID, value=self.logout_locator).click()
