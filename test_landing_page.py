import time


def test_title(landing_page):
    assert (landing_page.get_title()) == 'GUVI | Learn to code in your native language'


def test_logo(landing_page):
    assert (landing_page.get_logo().is_displayed())
    landing_page.get_logo().click()
    assert landing_page.driver.current_url == 'https://www.guvi.in/'


def test_footer_text(landing_page):
    assert (landing_page.get_footer_text().is_displayed())


def test_signup_link(landing_page):
    time.sleep(5)
    signup_link = landing_page.get_signup_link()
    assert (signup_link.is_displayed())
    signup_link.click()
    assert landing_page.driver.current_url == 'https://www.guvi.in/register'


def test_courses_link(landing_page):
    landing_page.browse()
    time.sleep(5)
    course_link = landing_page.get_course_link()
    assert (course_link.is_displayed())
    course_link.click()
    assert landing_page.driver.current_url == 'https://www.guvi.in/courses'


def test_login_link(landing_page):
    landing_page.browse()
    time.sleep(10)
    login_link = landing_page.get_login_link()
    assert (login_link.is_displayed())
    login_link.click()
    assert landing_page.driver.current_url == 'https://www.guvi.in/sign-in'
