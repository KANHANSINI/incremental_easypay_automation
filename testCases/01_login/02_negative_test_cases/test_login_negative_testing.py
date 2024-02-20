import allure
import pytest
import self as self
from allure_commons.types import AttachmentType
from pageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.test_utils import (sleep, SHORT_WAIT,
                                  perform_login_invalid_credentials_001_assertion,
                                  perform_login_invalid_credentials_002_assertion,
                                  perform_login_invalid_credentials_003_assertion)


class TestLogin:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    invalid_username = ReadConfig.get_invalid_username()
    invalid_password = ReadConfig.get_invalid_password()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        yield
        self.driver.close()

    # valid username and invalid password
    def test_login_invalid_credentials_001(self):
        try:
            self.login_page.login_with_valid_username_and_invalid_password(self.username, self.invalid_password)
            success_message = 'Oops! Wrong password'
            sleep(SHORT_WAIT)
            perform_login_invalid_credentials_001_assertion(self.driver, self.login_page, self.logger, success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="login_invalid_credentials_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

    # invalid username and valid password
    def test_login_invalid_credentials_002(self):
        try:
            self.login_page.login_with_invalid_username_and_valid_password(self.invalid_username, self.password)
            success_message = 'No user found'
            sleep(SHORT_WAIT)
            perform_login_invalid_credentials_002_assertion(self.driver, self.login_page, self.logger, success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="login_invalid_credentials_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

    # Invalid username and invalid password
    def test_login_invalid_credentials_003(self):
        try:
            self.login_page.login_with_invalid_username_and_invalid_password(self.invalid_username,
                                                                             self.invalid_password)
            success_message = 'No user found'
            sleep(SHORT_WAIT)
            perform_login_invalid_credentials_003_assertion(self.driver, self.login_page, self.logger, success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="login_invalid_credentials_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

    # Without enter username and password
    def test_login_invalid_credentials_004(self):
        try:
            self.login_page.login_without_enter_username_password()
            email_error_message = self.login_page.retrieve_error_message_email()
            password_error_message = self.login_page.retrieve_error_message_password()

            assert email_error_message == 'Email is required', f"Actual email error message: {email_error_message}"
            assert password_error_message == 'Password is required', (f"Actual password error message: "
                                                                      f"{password_error_message}")

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="login_invalid_credentials_scr",
                          attachment_type=AttachmentType.PNG)
            raise e
