import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.CreateInvoicePage import CreateInvoicePage
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_create_new_invoice_negative_testing


class TestCreateInvoice:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    # Add new Item without select an item before
    def test_negative_testing_003(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.create_guest_page = CreateInvoicePage(self.driver)
        sleep(SHORT_WAIT)
        self.create_guest_page.click_create_new_invoice()
        sleep(MEDIUM_WAIT)
        self.create_guest_page.add_new_item()
        sleep(SHORT_WAIT)

        try:
            success_message = 'Invalid item found in item list'
            perform_create_new_invoice_negative_testing(self.driver, self.create_guest_page, self.logger,
                                                        success_message)
            allure.attach(self.driver.get_screenshot_as_png(), name="copy_item_without_select_item_before_scr",
                          attachment_type=AttachmentType.PNG)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="copy_item_without_select_item_before_failed_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

        sleep(SHORT_WAIT)
        self.driver.close()
