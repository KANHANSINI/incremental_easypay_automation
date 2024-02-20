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

    def test_search_payment_logs_by_confirmation_number(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.logs = LogsPage(self.driver)
        sleep(MEDIUM_WAIT)
        self.logs.click_logs()
        sleep(SHORT_WAIT)
        self.logs.click_payment_logs()
        sleep(SHORT_WAIT)
        self.logs.search_by_confirmation_number("1232131")
        sleep(MEDIUM_WAIT)
        self.driver.close()

    def test_search_payment_logs_by_date(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.logs = LogsPage(self.driver)
        sleep(MEDIUM_WAIT)
        self.logs.click_logs()
        sleep(SHORT_WAIT)
        self.logs.click_payment_logs()
        sleep(SHORT_WAIT)
        self.logs.search_by_date("25-Nov-2019")
        sleep(MEDIUM_WAIT)
        self.driver.close()

    def test_search_payment_logs_by_invoice_number(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.logs = LogsPage(self.driver)
        sleep(MEDIUM_WAIT)
        self.logs.click_logs()
        sleep(SHORT_WAIT)
        self.logs.click_payment_logs()
        sleep(SHORT_WAIT)
        self.logs.search_by_invoice_number_payment_log("Test1561463147595498")
        sleep(MEDIUM_WAIT)
        self.driver.close()

    def test_search_email_logs_by_amount(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.logs = LogsPage(self.driver)
        sleep(MEDIUM_WAIT)
        self.logs.click_logs()
        sleep(SHORT_WAIT)
        self.logs.click_payment_logs()
        sleep(SHORT_WAIT)
        self.logs.search_by_amount("504.00")
        sleep(MEDIUM_WAIT)
        self.driver.close()
