import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.CreateInvoicePage import CreateInvoicePage
from pageObjects.CreateNewDiscountPage import CreateNewDiscountPage
from pageObjects.LoginPage import LoginPage
from test_data.create_new_discount_test_data import CreateNewDiscountTestData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_save_edit_invoice_assertion


class TestCreateInvoice:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_create_new_discount(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.create_guest_page = CreateInvoicePage(self.driver)
        self.create_new_discount = CreateNewDiscountPage(self.driver)
        sleep(SHORT_WAIT)
        self.create_guest_page.click_create_new_invoice()
        sleep(MEDIUM_WAIT)
        self.create_new_discount.add_new_discount(CreateNewDiscountTestData.name,
                                                  CreateNewDiscountTestData.code,
                                                  CreateNewDiscountTestData.amount,
                                                  CreateNewDiscountTestData.description)
        try:
            success_message = 'Added record successfully'
            perform_save_edit_invoice_assertion(self.driver, self.create_new_discount, self.logger, success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="create_new_discount_failed_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

        sleep(SHORT_WAIT)
        self.driver.close()
