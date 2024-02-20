import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.CreateInvoicePage import CreateInvoicePage
from pageObjects.NewGeneralTermsPage import CreateNewGeneralTermsPage
from pageObjects.LoginPage import LoginPage
from test_data.add_new_general_terms_test_data import AddNewGeneralTermTestData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_save_edit_invoice_assertion


class TestCreateInvoice:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_create_new_general_terms(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.create_guest_page = CreateInvoicePage(self.driver)
        self.create_new_general_term = CreateNewGeneralTermsPage(self.driver)
        sleep(SHORT_WAIT)
        self.create_guest_page.click_create_new_invoice()
        sleep(SHORT_WAIT)
        self.create_guest_page.go_to_general_terms()
        sleep(SHORT_WAIT)
        self.create_new_general_term.find_create_general_term()
        sleep(SHORT_WAIT)
        self.create_new_general_term.create_new_general_term(AddNewGeneralTermTestData.name,
                                                             AddNewGeneralTermTestData.code,
                                                             AddNewGeneralTermTestData.term)

        sleep(SHORT_WAIT)

        try:
            success_message = 'Term created successfully.'
            perform_save_edit_invoice_assertion(self.driver, self.create_new_general_term, self.logger, success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="create_new_general_terms_failed_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

        sleep(SHORT_WAIT)
        self.driver.close()
