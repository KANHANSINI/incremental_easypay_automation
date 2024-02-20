from self import self
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT


class TestLogin:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_login_with_valid_credentials(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.login_page.click_drop_down()
        sleep(SHORT_WAIT)
        self.login_page.click_logout()
        sleep(SHORT_WAIT)
        self.driver.close()
