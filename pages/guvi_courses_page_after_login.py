import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.data.data import PageData
from pages.locators.coursespages_afterlogin_locators import CoursesAfterLoginLocators


class GuviCoursesPageAfterLogin():
    # url = 'https://www.guvi.in/sign-in'
    # email_locator = "login_email"
    # password_locator = "login_password"
    # login_locator = "login_button"
    # search_bar_locator = '//*[@id="users"]/div[2]/div/div[4]/input'
    # course_library_link_locator = 'Course Library'
    # combo_link_locator = 'Combo'
    # free_library_link_locator = 'Free Library'
    # my_courses_link_locator = 'My Courses'
    # zen_link_locator = 'Zen'
    # codekata_link_locator = '//*[@id="sidebar"]/ul[1]/li[3]/a'
    # webkata_link_locator = '//*[@id="sidebar"]/ul[1]/li[4]/a'
    # debugging_link_locator = 'debuggingset'
    # ide_link_locator = '//*[@id="sidebar"]/ul[1]/li[6]/a'
    # leaderboard_link_locator = '//*[@id="sidebar"]/ul[1]/li[7]/a'
    # rewards_link_locator = '//*[@id="sidebar"]/ul[1]/li[8]/a'
    # referral_link_locator = '//*[@id="sidebar"]/ul[1]/li[9]/a'
    # forum_link_locator = '//*[@id="forum_link"]/a'
    # logout_dropdown_locator = '/html/body/header/nav/div[2]/button'
    # logout_locator = 'signout'

    def __init__(self, driver):
        self.driver = driver

    def browse(self):
        self.driver.maximize_window()
        self.driver.get(PageData.login_url)
        return self

    def login(self, email, password):
        self.driver.find_element(by=By.ID, value=CoursesAfterLoginLocators.email_locator).send_keys(email)
        self.driver.find_element(by=By.ID, value=CoursesAfterLoginLocators.password_locator).send_keys(password)
        self.driver.find_element(by=By.ID, value=CoursesAfterLoginLocators.login_locator).click()

    def get_title(self):
        return self.driver.title

    def get_search_bar(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesAfterLoginLocators.search_bar_locator)

    def get_course_library_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value=CoursesAfterLoginLocators.course_library_link_locator)

    def get_combo_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value=CoursesAfterLoginLocators.combo_link_locator)

    def get_free_library_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value=CoursesAfterLoginLocators.free_library_link_locator)

    def get_my_courses_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value=CoursesAfterLoginLocators.my_courses_link_locator)

    def get_zen_link(self):
        return self.driver.find_element(by=By.LINK_TEXT, value=CoursesAfterLoginLocators.zen_link_locator)

    def get_codekata_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesAfterLoginLocators.codekata_link_locator)

    def get_webkata_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesAfterLoginLocators.webkata_link_locator)

    def get_debugging_link(self):
        return self.driver.find_element(by=By.ID, value=CoursesAfterLoginLocators.debugging_link_locator)

    def get_ide_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesAfterLoginLocators.ide_link_locator)

    def get_leaderboard_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesAfterLoginLocators.leaderboard_link_locator)

    def get_rewards_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesAfterLoginLocators.rewards_link_locator)

    def get_referral_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesAfterLoginLocators.referral_link_locator)

    def get_forum_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesAfterLoginLocators.forum_link_locator)

    def get_signout_link(self):
        return self.driver.find_element(by=By.XPATH, value=CoursesAfterLoginLocators.logout_dropdown_locator)

    def logout(self):
        time.sleep(5)
        logout_dropdown_locator = self.driver.find_element(by=By.XPATH,
                                                           value=CoursesAfterLoginLocators.logout_dropdown_locator)
        # Create the ActionChains Object which will take webdriver as an argument

        action = ActionChains(self.driver)
        # Tell the ActionChains to Click on the HTML Element
        # perform() should be used so that ActionChain can be done successfully

        action.click(on_element=logout_dropdown_locator).perform()
        time.sleep(3)
        self.driver.find_element(by=By.ID, value=CoursesAfterLoginLocators.logout_locator).click()
