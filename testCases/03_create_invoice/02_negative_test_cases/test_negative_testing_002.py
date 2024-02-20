import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.CreateInvoicePage import CreateInvoicePage
from pageObjects.LoginPage import LoginPage
from test_data.create_new_payment_invoice_test_data import CreateNewPaymentInvoiceTestData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class TestCreateInvoice:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_create_new_payment_invoice_without_any_item(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.create_guest_page = CreateInvoicePage(self.driver)
        sleep(SHORT_WAIT)
        self.create_guest_page.click_create_new_invoice()
        sleep(MEDIUM_WAIT)
        self.create_guest_page.create_new_payment_invoice(CreateNewPaymentInvoiceTestData.guest_name,
                                                          CreateNewPaymentInvoiceTestData.reservation_number,
                                                          CreateNewPaymentInvoiceTestData.remark)
        self.create_guest_page.remove_item()
        sleep(SHORT_WAIT)
        self.create_guest_page.click_save_button()
        sleep(SHORT_WAIT)

        actual_message = 'Added record successfully'
        expected_message = 'Added record successfully'

        if actual_message == expected_message:
            raise AssertionError("Test case failed: Actual message matches expected message.")

        allure.attach(self.driver.get_screenshot_as_png(), name="create_new_payment_invoice_failed_scr",
                      attachment_type=AttachmentType.PNG)

        sleep(SHORT_WAIT)
        self.driver.close()
