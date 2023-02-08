from selenium.webdriver.common.by import By


class GuviLandingPage():
    url = 'https://www.guvi.in/'
    logo_locator = 'head-guvi-logo'
    courses_link_locator = '/html/body/header/nav/div/div/div[2]/div[1]/ul/li[1]/a'
    login_link_locator = '/html/body/header/nav/div/div/div[2]/div[2]/ul/li[1]/a'
    signup_link_locator = '/html/body/header/nav/div/div/div[2]/div[2]/ul/li[2]/a'
    footer_locator = '/html/body/main/footer/div/div[2]/div[2]/div/div[2]/p'

    def __init__(self, driver):
        self.driver = driver

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
