import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.ItemsPage import ItemsPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SetupPage import SetupPage
from test_data.add_new_item_test_data import CreateNewItemTestData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_create_new_item_assertion


class TestSetUp:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_add_new_item(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.setup = SetupPage(self.driver)
        self.add_item = ItemsPage(self.driver)
        sleep(SHORT_WAIT)
        self.setup.click_setup()
        sleep(MEDIUM_WAIT)
        self.add_item.click_items()
        sleep(SHORT_WAIT)
        self.add_item.click_add_new_item()
        sleep(SHORT_WAIT)
        self.add_item.add_new_item(CreateNewItemTestData.name,
                                   CreateNewItemTestData.code,
                                   CreateNewItemTestData.rate,
                                   CreateNewItemTestData.description)
        sleep(SHORT_WAIT)

        try:
            success_message = 'Added record successfully'
            perform_create_new_item_assertion(self.driver, self.add_item, self.logger, success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="create_new_item_failed_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

        sleep(SHORT_WAIT)
        self.driver.close()
