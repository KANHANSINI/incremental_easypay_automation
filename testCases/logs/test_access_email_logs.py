import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.LoginPage import LoginPage
from pageObjects.LogsPage import LogsPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT


class TestLogs:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_access_email_logs(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.logs = LogsPage(self.driver)
        sleep(SHORT_WAIT)
        self.logs.click_logs()
        sleep(SHORT_WAIT)
        self.logs.click_email_logs()
        sleep(SHORT_WAIT)
        self.driver.close()

    def test_view_email_logs(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.logs = LogsPage(self.driver)
        sleep(SHORT_WAIT)
        self.logs.click_logs()
        sleep(SHORT_WAIT)
        self.logs.click_email_logs()
        sleep(SHORT_WAIT)
        self.logs.click_action()
        sleep(SHORT_WAIT)
        self.logs.click_close()
        sleep(SHORT_WAIT)
        self.driver.close()
