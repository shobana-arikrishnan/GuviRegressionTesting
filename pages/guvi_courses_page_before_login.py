from selenium.webdriver.common.by import By
from pages.data.data import PageData
from pages.locators.coursespages_beforelogin_locators import CoursesBeforeLoginLocators


class GuviCoursesPageBeforeLogin():
    # url = 'https://www.guvi.in/'
    # courses_link_locator = '/html/body/header/nav/div/div/div[2]/div[1]/ul/li[1]/a'
    # login_link_locator = '//*[@id="accountGroup"]/ul/li[1]/a'
    # signup_link_locator = '//*[@id="accountGroup"]/ul/li[2]/a'
    # search_bar_locator = '//*[@id="users"]/div[2]/div/div[4]/input'
    # course_library_link_locator = '//*[@id="home-tab"]'
    # combo_link_locator = '//*[@id="offersList"]'
    # free_library_link_locator = '//*[@id="contact-tab"]'
    # codekata_link_locator = '//*[@id="sidebar"]/ul[1]/li[2]/a'
    # webkata_link_locator = '//*[@id="sidebar"]/ul[1]/li[3]/a'
    # debugging_link_locator = '//*[@id="debuggingset"]'
    # ide_link_locator = '//*[@id="sidebar"]/ul[1]/li[5]/a'
    # leaderboard_link_locator = '//*[@id="sidebar"]/ul[1]/li[6]/a'
    # rewards_link_locator = '//*[@id="sidebar"]/ul[1]/li[7]/a'
    # referral_link_locator = '//*[@id="sidebar"]/ul[1]/li[8]/a'

    def __init__(self, driver):
        self.driver = driver

    def browse(self):
        self.driver.maximize_window()
        self.driver.get(PageData.url)
        return self

    def get_course_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.courses_link_locator).click()

    def get_title(self):
        return self.driver.title

    def get_login_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.login_link_locator)

    def get_signup_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.signup_link_locator)

    def get_search_bar(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.search_bar_locator)

    def get_course_library_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.course_library_link_locator)

    def get_combo_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.combo_link_locator)

    def get_free_library_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.free_library_link_locator)

    def get_codekata_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.codekata_link_locator)

    def get_webkata_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.webkata_link_locator)

    def get_debugging_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.debugging_link_locator)

    def get_ide_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.ide_link_locator)

    def get_leaderboard_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.leaderboard_link_locator)

    def get_rewards_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.rewards_link_locator)

    def get_referral_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesBeforeLoginLocators.referral_link_locator)
