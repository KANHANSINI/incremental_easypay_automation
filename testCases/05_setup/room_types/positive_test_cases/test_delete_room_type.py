import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.LoginPage import LoginPage
from pageObjects.RoomTypePage import RoomTypePage
from pageObjects.SetupPage import SetupPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_create_new_room_type_assertion, \
    perform_remove_room_type_assertion


class TestSetUp:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_delete_room_type(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.setup = SetupPage(self.driver)
        self.delete_room_type = RoomTypePage(self.driver)
        sleep(SHORT_WAIT)
        self.setup.click_setup()
        sleep(MEDIUM_WAIT)
        self.delete_room_type.click_room_type()
        sleep(SHORT_WAIT)
        self.delete_room_type.click_remove_item()
        sleep(SHORT_WAIT)
        try:
            success_message = 'No permission!'
            perform_remove_room_type_assertion(self.driver, self.delete_room_type, self.logger, success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="remove_room_type_failed_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

        sleep(SHORT_WAIT)
        self.driver.close()
