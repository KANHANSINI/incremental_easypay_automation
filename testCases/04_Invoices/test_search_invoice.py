import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.InvoicesPage import InvoicesPage
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class TestSearchInvoice:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_search_invoice(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        sleep(MEDIUM_WAIT)
        self.search_invoice = InvoicesPage(self.driver)
        sleep(SHORT_WAIT)
        self.search_invoice.set_search_name("Anu")
        sleep(SHORT_WAIT)
        self.driver.close()
