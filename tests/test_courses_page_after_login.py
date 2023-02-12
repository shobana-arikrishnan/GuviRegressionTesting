import time


class TestCoursesPageAfterLogin:

    def test_login_success(self, credentials, course_page_after_login):
        time.sleep(5)
        course_page_after_login.login(credentials["email"], credentials["password"])
        time.sleep(5)
        actual_url = 'https://www.guvi.in/courses.html?current_tab=myCourses'
        expected_url = course_page_after_login.driver.current_url
        assert expected_url == actual_url
        time.sleep(5)

    def test_title(self, course_page_after_login):
        assert (course_page_after_login.get_title()) == 'GUVI | courses'

    def test_search_bar(self, course_page_after_login):
        search_bar = course_page_after_login.get_search_bar()
        assert (search_bar.is_displayed())

    def test_course_library_link(self, course_page_after_login):
        course_library = course_page_after_login.get_course_library_link()
        assert (course_library.is_displayed())

    def test_combo_link(self, course_page_after_login):
        combo = course_page_after_login.get_combo_link()
        assert (combo.is_displayed())

    def test_free_library_link(self, course_page_after_login):
        free_library = course_page_after_login.get_free_library_link()
        assert (free_library.is_displayed())

    def test_my_courses_link(self, course_page_after_login):
        my_courses = course_page_after_login.get_my_courses_link()
        assert (my_courses.is_displayed())

    def test_codekata_link(self, course_page_after_login):
        codekata = course_page_after_login.get_codekata_link()
        assert (codekata.is_displayed())

    def test_webkata_link(self, course_page_after_login):
        webkata = course_page_after_login.get_webkata_link()
        assert (webkata.is_displayed())

    def test_debugging_link(self, course_page_after_login):
        debugging = course_page_after_login.get_debugging_link()
        assert (debugging.is_displayed())

    def test_ide_link(self, course_page_after_login):
        ide = course_page_after_login.get_ide_link()
        assert (ide.is_displayed())

    def test_leaderboard_link(self, course_page_after_login):
        leaderboard = course_page_after_login.get_leaderboard_link()
        assert (leaderboard.is_displayed())

    def test_rewards_link(self, course_page_after_login):
        rewards = course_page_after_login.get_rewards_link()
        assert (rewards.is_displayed())

    def test_referral_link(self, course_page_after_login):
        referral = course_page_after_login.get_referral_link()
        assert (referral.is_displayed())

    def test_forum_link(self, course_page_after_login):
        forum = course_page_after_login.get_forum_link()
        assert (forum.is_displayed())

    def test_logout_success(self, credentials, course_page_after_login):
        logout_link = course_page_after_login.get_signout_link()
        assert (logout_link.is_displayed())
        course_page_after_login.logout()
