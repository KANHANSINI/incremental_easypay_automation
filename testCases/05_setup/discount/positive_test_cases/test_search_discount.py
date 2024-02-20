import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.DiscountPage import DiscountPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SetupPage import SetupPage
from test_data.create_new_discount_test_data import SearchDiscountTestData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT


class TestSetUp:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_search_discount_by_name(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.setup = SetupPage(self.driver)
        self.discount = DiscountPage(self.driver)
        sleep(SHORT_WAIT)
        self.setup.click_setup()
        sleep(SHORT_WAIT)
        self.discount.click_discount()
        sleep(SHORT_WAIT)
        self.discount.search_discount_by_name(SearchDiscountTestData.name)
        sleep(SHORT_WAIT)
        self.driver.close()

    def test_search_discount_by_code(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.setup = SetupPage(self.driver)
        self.discount = DiscountPage(self.driver)
        sleep(SHORT_WAIT)
        self.setup.click_setup()
        sleep(SHORT_WAIT)
        self.discount.click_discount()
        sleep(SHORT_WAIT)
        self.discount.search_discount_by_code(SearchDiscountTestData.code)
        sleep(SHORT_WAIT)
        self.driver.close()
