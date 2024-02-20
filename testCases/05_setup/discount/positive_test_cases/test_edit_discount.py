import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.DiscountPage import DiscountPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SetupPage import SetupPage
from test_data.add_new_discount_test_data import AddNewDiscountTestData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, perform_edit_discount_assertion


class TestSetUp:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_edit_discount(self, setup):
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
        self.discount.edit_discount(AddNewDiscountTestData.amount)

        sleep(SHORT_WAIT)
        try:
            success_message = 'Updated record successfully'
            perform_edit_discount_assertion(self.driver, self.discount, self.logger, success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="create_new_guest_failed_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

        sleep(SHORT_WAIT)
        self.driver.close()
