from self import self
from pageObjects.ConfigurationPage import ConfigurationPage
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class TestConfigurations:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_search_payment_settings(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.configuration = ConfigurationPage(self.driver)
        sleep(MEDIUM_WAIT)
        self.configuration.click_configuration()
        sleep(SHORT_WAIT)
        self.configuration.click_payment_settings()
        sleep(SHORT_WAIT)
        self.configuration.search_payment_settings_by_name("Testing Hotel")
        sleep(SHORT_WAIT)
        self.configuration.search_payment_settings_by_invalid_name("Flora Creek Deluxe Hotel Apartments")
        self.driver.close()
