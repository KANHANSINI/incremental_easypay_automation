import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.ConfigurationPage import ConfigurationPage
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_delete_configuration_assertion


class TestConfigurations:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_delete_email_configurations(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.configuration = ConfigurationPage(self.driver)
        sleep(MEDIUM_WAIT)
        self.configuration.click_configuration()
        sleep(SHORT_WAIT)
        self.configuration.click_email_configurations()
        sleep(SHORT_WAIT)
        self.configuration.click_delete_email_configurations()
        sleep(SHORT_WAIT)
        try:
            success_message = 'No permission!'
            perform_delete_configuration_assertion(self.driver, self.configuration, self.logger, success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="delete_email_configurations_failed_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

        sleep(SHORT_WAIT)
        self.driver.close()
