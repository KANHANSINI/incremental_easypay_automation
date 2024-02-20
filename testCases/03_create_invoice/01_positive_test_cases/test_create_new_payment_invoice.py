import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.CreateInvoicePage import CreateInvoicePage
from pageObjects.LoginPage import LoginPage
from test_data.create_new_payment_invoice_test_data import CreateNewPaymentInvoiceTestData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_create_payment_invoice_assertion


class TestCreateInvoice:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_create_new_invoice(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.create_invoice = CreateInvoicePage(self.driver)
        sleep(SHORT_WAIT)
        self.create_invoice.click_create_new_invoice()
        sleep(MEDIUM_WAIT)
        self.create_invoice.create_new_payment_invoice(CreateNewPaymentInvoiceTestData.guest_name,
                                                       CreateNewPaymentInvoiceTestData.reservation_number,
                                                       CreateNewPaymentInvoiceTestData.remark)
        self.create_invoice.select_item_from_dropdown()
        sleep(SHORT_WAIT)
        self.create_invoice.add_and_remove_item()
        sleep(SHORT_WAIT)
        self.create_invoice.select_discount()
        sleep(SHORT_WAIT)
        self.create_invoice.click_toggle()
        sleep(SHORT_WAIT)
        self.create_invoice.add_new_term()
        sleep(SHORT_WAIT)
        self.create_invoice.click_save_button()
        sleep(SHORT_WAIT)

        try:
            success_message = 'Added record successfully'
            perform_create_payment_invoice_assertion(self.driver, self.create_guest_page,
                                                     self.logger, success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="create_new_payment_invoice_failed_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

        sleep(SHORT_WAIT)
        self.driver.close()
