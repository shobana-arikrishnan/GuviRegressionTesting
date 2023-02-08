from selenium.webdriver.common.by import By


class GuviCoursesPageBeforeLogin():
    url = 'https://www.guvi.in/'
    courses_link_locator = '/html/body/header/nav/div/div/div[2]/div[1]/ul/li[1]/a'
    login_link_locator = '//*[@id="accountGroup"]/ul/li[1]/a'
    signup_link_locator = '//*[@id="accountGroup"]/ul/li[2]/a'
    search_bar_locator = '//*[@id="users"]/div[2]/div/div[4]/input'
    course_library_link_locator = '//*[@id="home-tab"]'
    combo_link_locator = '//*[@id="offersList"]'
    free_library_link_locator = '//*[@id="contact-tab"]'
    codekata_link_locator = '//*[@id="sidebar"]/ul[1]/li[2]/a'
    webkata_link_locator = '//*[@id="sidebar"]/ul[1]/li[3]/a'
    debugging_link_locator = '//*[@id="debuggingset"]'
    ide_link_locator = '//*[@id="sidebar"]/ul[1]/li[5]/a'
    leaderboard_link_locator = '//*[@id="sidebar"]/ul[1]/li[6]/a'
    rewards_link_locator = '//*[@id="sidebar"]/ul[1]/li[7]/a'
    referral_link_locator = '//*[@id="sidebar"]/ul[1]/li[8]/a'

    def __init__(self, driver):
        self.driver = driver

    def browse(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        return self

    def get_course_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.courses_link_locator).click()

    def get_title(self):
        return self.driver.title

    def get_login_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.login_link_locator)

    def get_signup_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.signup_link_locator)

    def get_search_bar(self):
        return self.driver.find_element(by=By.XPATH, value=self.search_bar_locator)

    def get_course_library_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.course_library_link_locator)

    def get_combo_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.combo_link_locator)

    def get_free_library_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.free_library_link_locator)

    def get_codekata_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.codekata_link_locator)

    def get_webkata_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.webkata_link_locator)

    def get_debugging_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.debugging_link_locator)

    def get_ide_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.ide_link_locator)

    def get_leaderboard_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.leaderboard_link_locator)

    def get_rewards_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.rewards_link_locator)

    def get_referral_link(self):
        return self.driver.find_element(by=By.XPATH, value=self.referral_link_locator)
