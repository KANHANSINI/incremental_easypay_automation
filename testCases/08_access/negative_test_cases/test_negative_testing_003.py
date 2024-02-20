from self import self
from pageObjects.AccessPage import AccessPage
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class TestAccess:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_create_user_without_email(self, setup):
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
        self.access.create_new_user_without_email()
        sleep(SHORT_WAIT)
        self.driver.close()
