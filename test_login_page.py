import time


def test_login_title(login_page):
    assert (login_page.get_title()) == 'GUVI | Sign-in'


def test_login_success(credentials, login_page):
    time.sleep(5)
    login_page.login(credentials["email"], credentials["password"])
    time.sleep(3)
    actual_url = 'https://www.guvi.in/courses'
    expected_url = login_page.driver.current_url
    assert expected_url == actual_url

# def test_login_failure():
#     login_page = GuviLoginPage().browse()
#     time.sleep(5)
#     login_page.login("fgfgfgf", password)
#     time.sleep(5)
#     email_warn_text = login_page.driver.find_element(By.ID, "email_warn").text
#     assert email_warn_text == 'E-mail is Invalid'
#     assert login_page.driver.current_url == 'https://www.guvi.in/sign-in'
#
#
# def test_login_failure_with_good_email():
#     login_page = GuviLoginPage().browse()
#     time.sleep(5)
#     login_page.login('testtest@test.com', password)
#     time.sleep(5)
#     email_warn_text = login_page.driver.find_element(By.ID, "pass_warn").text
#     assert email_warn_text == 'Incorrect Username or Password'
#     assert login_page.driver.current_url == 'https://www.guvi.in/sign-in'
