from locators.common_locators import CommonLocators
from locators.payment_term_locators import AddNewPaymentTermsPageLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class CreateNewPaymentTermsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_new_payment_terms = AddNewPaymentTermsPageLocators()
        self.locators = CommonLocators()

    def click_create_new_payment_term(self):
        self.click_element("span_create_new_payment_term_xpath",
                           self.locator_new_payment_terms.span_create_new_payment_term_xpath)

    def set_term_name(self, name):
        self.send_keys_to_element(name, "input_term_name_xpath", self.locator_new_payment_terms.input_term_name_xpath)

    def set_term_code(self, code):
        self.send_keys_to_element(code, "input_term_code_xpath", self.locator_new_payment_terms.input_term_code_xpath)

    def set_term_description(self, term):
        self.send_keys_to_element(term, "textarea_term_description_xpath",
                                  self.locator_new_payment_terms.textarea_term_description_xpath)

    def click_save_and_select(self):
        self.click_element("button_save_and_select_xpath", self.locator_new_payment_terms.button_save_and_select_xpath)

    def create_new_payment_term(self, name, code, term):
        self.set_term_name(name)
        sleep(SHORT_WAIT)
        self.set_term_code(code)
        sleep(SHORT_WAIT)
        self.set_term_description(term)
        sleep(SHORT_WAIT)
        self.click_save_and_select()

    def find_create_payment_term(self):
        create_new_payment_term = self.find_element("span_create_new_payment_term_xpath",
                                                    self.locator_new_payment_terms.span_create_new_payment_term_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', create_new_payment_term)
        sleep(SHORT_WAIT)
        self.click_element("span_create_new_payment_term_xpath",
                           self.locator_new_payment_terms.span_create_new_payment_term_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locators.notification_xpath)
