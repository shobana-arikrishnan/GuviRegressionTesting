class TestSignUpPage:

    def test_signup_title(self, signup_page):
        assert (signup_page.get_title()) == 'GUVI | Sign-up'

    def test_logo(self, signup_page):
        assert (signup_page.get_logo().is_displayed())

    def test_google_signin(self, signup_page):
        assert (signup_page.get_google_signin().is_displayed())

    def test_signup_success(self, signup_info, signup_page):
        signup_page.signup(firstname=signup_info.get("first_name"), lastname=signup_info.get("last_name"),
                           password=signup_info.get("password"), email=signup_info.get("email"),
                           mobile=signup_info.get("mobile_number"))
        elements = signup_page.get_invalid_feedback()
        elements_texts = list(filter(lambda txt: txt != '', map(lambda el: el.text, elements)))
        assert len(elements_texts) == 0

    def test_signup_failed(self, signup_failed_info, signup_page):
        signup_page.signup(firstname=signup_failed_info.get("first_name"), lastname=signup_failed_info.get("last_name"),
                           password=signup_failed_info.get("password"), email=signup_failed_info.get("email"),
                           mobile=signup_failed_info.get("mobile_number"))
        elements = signup_page.get_invalid_feedback()
        elements_texts = list(filter(lambda txt: txt != '', map(lambda el: el.text, elements)))

        for error in elements_texts:
            assert (error in ['Please Enter a valid First Name', 'Please Enter a valid Last Name',
                              'Please Enter a valid email-id',
                              'Email-id already Exist. Login here', 'Password must satisfy conditions below.',
                              ' Please Enter a valid Mobile number'])
