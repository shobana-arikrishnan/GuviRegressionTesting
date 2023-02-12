import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.data.data import PageData
from pages.locators.logoutpage_locators import LogoutPageLocators


class GuviLogoutPage():
    # url = "https://www.guvi.in/sign-in"
    # email_locator = "login_email"
    # password_locator = "login_password"
    # login_locator = "login_button"
    # logout_dropdown_locator = '/html/body/header/nav/div[2]/button'
    # logout_locator = 'signout'

    def __init__(self, driver):
        self.driver = driver

    def browse(self):
        self.driver.maximize_window()
        self.driver.get(PageData.login_url)
        return self

    def get_title(self):
        time.sleep(5)
        return self.driver.title

    def login(self, email, password):
        self.driver.find_element(by=By.ID, value=LogoutPageLocators.email_locator).send_keys(email)
        self.driver.find_element(by=By.ID, value=LogoutPageLocators.password_locator).send_keys(password)
        self.driver.find_element(by=By.ID, value=LogoutPageLocators.login_locator).click()

    def get_signout_link(self):
        return self.driver.find_element(by=By.XPATH, value=LogoutPageLocators.logout_dropdown_locator)

    def logout(self):
        time.sleep(5)
        logout_dropdown_locator = self.driver.find_element(by=By.XPATH,
                                                           value=LogoutPageLocators.logout_dropdown_locator)
        action = ActionChains(self.driver)
        action.click(on_element=logout_dropdown_locator).perform()
        time.sleep(3)
        self.driver.find_element(by=By.ID, value=LogoutPageLocators.logout_locator).click()
