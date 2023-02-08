import time


def test_logout_success(credentials, logout_page):
    time.sleep(10)
    logout_page.login(credentials["email"], credentials["password"])
    time.sleep(7)
    logout_link = logout_page.get_signout_link()
    assert (logout_link.is_displayed())
    logout_page.logout()
    time.sleep(3)
    assert logout_page.driver.current_url == 'https://www.guvi.in/'
