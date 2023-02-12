import time

from pages.data.data import PageData


class TestLoginPage:

    def test_login_title(self, login_page):
        assert (login_page.get_title()) == 'GUVI | Sign-in'

    def test_login_incorrect_password(self, credentials, login_page):
        time.sleep(5)
        login_page.clear_login_form()
        login_page.login(credentials["email"], '*****')
        time.sleep(5)
        warning = login_page.get_warning()
        assert warning[1].text == 'Incorrect Username or Password'

    def test_login_incorrect_email(self, login_page):
        time.sleep(5)
        login_page.clear_login_form()
        login_page.login('invalidemail@', '*****')
        time.sleep(5)
        warning = login_page.get_warning()
        assert warning[0].text == 'E-mail is Invalid'

    def test_login_success(self, credentials, login_page):
        time.sleep(5)
        login_page.clear_login_form()
        login_page.login(credentials["email"], credentials["password"])
        time.sleep(5)
        actual_url = 'https://www.guvi.in/courses.html?current_tab=myCourses'
        expected_url = login_page.driver.current_url
        cookie = login_page.driver.get_cookie("USER_DATA")
        assert cookie["value"] != ''
        assert expected_url != PageData.login_url
