import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.InvoicesPage import InvoicesPage
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, perform_save_edit_invoice_assertion, MEDIUM_WAIT


class TestEditInvoice:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_save_payment_invoice(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        sleep(MEDIUM_WAIT)
        self.save_invoice_page = InvoicesPage(self.driver)
        sleep(SHORT_WAIT)
        self.save_invoice_page.invoice_action_edit()
        sleep(SHORT_WAIT)

        try:
            success_message = 'Updated record successfully'
            perform_save_edit_invoice_assertion(self.driver, self.save_invoice_page, self.logger, success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="save_invoice_failed_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

        sleep(SHORT_WAIT)
        self.driver.close()
