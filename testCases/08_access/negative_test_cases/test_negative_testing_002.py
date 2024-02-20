import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.AccessPage import AccessPage
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_add_new_user_with_invalid_email_assertion


class TestAccess:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_create_user_with_invalid_email(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.access = AccessPage(self.driver)
        sleep(MEDIUM_WAIT)
        self.access.click_access()
        sleep(SHORT_WAIT)
        self.access.click_users()
        sleep(SHORT_WAIT)
        self.access.create_new_user_with_invalid_email("ishadiceydigitalcom")
        sleep(SHORT_WAIT)
        #
        # # 2024/01/30
        # try:
        #     success_message = 'nvalid Syntax'
        #     perform_add_new_user_with_invalid_email_assertion(self.driver, self.access, self.logger, success_message)
        #     print(self.access.error_message())
        # except Exception as e:
        #     allure.attach(self.driver.get_screenshot_as_png(), name="create_new_user_failed_scr",
        #                   attachment_type=AttachmentType.PNG)
        #     raise e
        #
        # sleep(SHORT_WAIT)
        self.driver.close()
