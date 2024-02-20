from self import self
from pageObjects.LoginPage import LoginPage
from pageObjects.LogsPage import LogsPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class TestLogs:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_search_email_logs_by_name(self, setup):
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
        self.logs.search_by_name("Jon Mayer Polanski")
        sleep(MEDIUM_WAIT)
        self.driver.close()

    def test_search_email_logs_by_invoice_number(self, setup):
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
        self.logs.search_by_invoice_number("Test1663033276837548")
        sleep(MEDIUM_WAIT)
        self.driver.close()

    def test_search_email_logs_by_date(self, setup):
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
        self.logs.search_by_invoice_date("2022-09-13")
        sleep(MEDIUM_WAIT)
        self.driver.close()

    def test_search_email_logs_by_subject(self, setup):
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
        self.logs.search_by_invoice_subject("Invoice From Testing Hotel - LH220913104")
        sleep(MEDIUM_WAIT)
        self.driver.close()
