import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.ItemTypePage import ItemTypePage
from pageObjects.LoginPage import LoginPage
from pageObjects.SetupPage import SetupPage
from test_data.add_new_item_type_test_data import CreateNewItemTypeTestData, EditItemTypeTestData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, perform_create_new_item_type_assertion, \
    perform_edit_item_type_assertion


class TestSetUp:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_edit_item_type(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.setup = SetupPage(self.driver)
        self.item_type = ItemTypePage(self.driver)
        sleep(SHORT_WAIT)
        self.setup.click_setup()
        sleep(SHORT_WAIT)
        self.item_type.click_item_type()
        sleep(SHORT_WAIT)
        self.item_type.edit_item_type(EditItemTypeTestData.name)

        sleep(SHORT_WAIT)
        try:
            success_message = 'Item type updated successfully.'
            perform_edit_item_type_assertion(self.driver, self.item_type, self.logger, success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="edit_item_type_failed_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

        sleep(SHORT_WAIT)
        self.driver.close()
