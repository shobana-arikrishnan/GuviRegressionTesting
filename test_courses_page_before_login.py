import time


def test_courses_link(course_page_before_login):
    course_page_before_login.browse()
    time.sleep(5)
    course_page_before_login.get_course_link()
    time.sleep(5)
    assert course_page_before_login.driver.current_url == 'https://www.guvi.in/courses'


def test_title(course_page_before_login):
    assert (course_page_before_login.get_title()) == 'GUVI | courses'


def test_signup_link(course_page_before_login):
    signup_link = course_page_before_login.get_signup_link()
    assert (signup_link.is_displayed())


def test_login_link(course_page_before_login):
    login_link = course_page_before_login.get_login_link()
    assert (login_link.is_displayed())


def test_search_bar(course_page_before_login):
    search_bar = course_page_before_login.get_search_bar()
    assert (search_bar.is_displayed())


def test_course_library_link(course_page_before_login):
    course_library = course_page_before_login.get_course_library_link()
    assert (course_library.is_displayed())


def test_combo_link(course_page_before_login):
    combo = course_page_before_login.get_combo_link()
    assert (combo.is_displayed())


def test_free_library_link(course_page_before_login):
    free_library = course_page_before_login.get_free_library_link()
    assert (free_library.is_displayed())


def test_codekata_link(course_page_before_login):
    codekata = course_page_before_login.get_codekata_link()
    assert (codekata.is_displayed())


def test_webkata_link(course_page_before_login):
    webkata = course_page_before_login.get_webkata_link()
    assert (webkata.is_displayed())


def test_debugging_link(course_page_before_login):
    debugging = course_page_before_login.get_debugging_link()
    assert (debugging.is_displayed())


def test_ide_link(course_page_before_login):
    ide = course_page_before_login.get_ide_link()
    assert (ide.is_displayed())


def test_leaderboard_link(course_page_before_login):
    leaderboard = course_page_before_login.get_leaderboard_link()
    assert (leaderboard.is_displayed())


def test_rewards_link(course_page_before_login):
    rewards = course_page_before_login.get_rewards_link()
    assert (rewards.is_displayed())


def test_referral_link(course_page_before_login):
    referral = course_page_before_login.get_referral_link()
    assert (referral.is_displayed())


