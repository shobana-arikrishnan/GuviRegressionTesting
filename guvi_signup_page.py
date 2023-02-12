from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class GuviSignupPage:
    url = 'https://www.guvi.in/register'
    logo_locator = '//*[@id="sign-in-page"]/div[2]/div/div/div[2]/div[1]/a/picture/img'
    google_button_locator = 'google-button'
    firstname_locator = 'firstName'
    lastname_locator = 'lastName'
    email_locator = 'emailInput'
    password_locator = 'passwordInput'
    mobile_locator = 'mobileNumberInput'
    signup_button_locator = 'signup'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def browse(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        return self

    def get_title(self):
        return self.driver.title

    def get_logo(self):
        return self.driver.find_element(by=By.XPATH, value=self.logo_locator)

    def get_google_signin(self):
        return self.driver.find_element(by=By.ID, value=self.google_button_locator)

    def get_invalid_feedback(self):
        return self.driver.find_elements(by=By.CLASS_NAME, value="invalid-feedback")

    def signup(self, firstname, lastname, email, password, mobile):
        try:
            firstname_input = self.wait.until(EC.presence_of_element_located((By.ID, self.firstname_locator)))
            lastname_input = self.wait.until(EC.presence_of_element_located((By.ID, self.lastname_locator)))
            email_input = self.wait.until(EC.presence_of_element_located((By.ID, self.email_locator)))
            password_input = self.wait.until(EC.presence_of_element_located((By.ID, self.password_locator)))
            mobile_input = self.wait.until(EC.presence_of_element_located((By.ID, self.mobile_locator)))
            submit_button = self.wait.until(EC.presence_of_element_located((By.ID, self.signup_button_locator)))

            firstname_input.send_keys(firstname)
            lastname_input.send_keys(lastname)
            email_input.send_keys(email)
            password_input.send_keys(password)
            mobile_input.send_keys(mobile)
            submit_button.click()
        except NoSuchElementException:
            print('Some of the elements are missing!')
