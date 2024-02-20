from locators.item_type_locators import AddNewItemTypeLocators, EditItemTypeLocators, DeleteItemTypeLocators
from locators.common_locators import CommonLocators
from locators.terms_locators import AddNewTermLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import SHORT_WAIT, sleep, MEDIUM_WAIT


class TermsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CommonLocators()
        self.locators_add_new_terms = AddNewTermLocators()
        self.locators_edit_terms = EditItemTypeLocators()
        self.locators_delete_terms = DeleteItemTypeLocators()

    def click_terms(self):
        self.click_element("span_terms_xpath", self.locators_add_new_terms.span_terms_xpath)

    def click_add_new_term(self):
        self.click_element("button_add_new_term_xpath", self.locators_add_new_terms.button_add_new_term_xpath)

    def set_name(self, name):
        self.send_keys_to_element(name, "input_name_xpath", self.locators_add_new_terms.input_name_xpath)

    def set_code(self, code):
        self.send_keys_to_element(code, "input_code_xpath", self.locators_add_new_terms.input_code_xpath)

    def set_term(self, term):
        self.click_element("paragraph_terms_xpath", self.locators_add_new_terms.paragraph_terms_xpath)
        self.send_keys_to_element(term, "paragraph_terms_xpath", self.locators_add_new_terms.paragraph_terms_xpath)

    def add_new_term(self, name, code, term):
        self.click_add_new_term()
        sleep(SHORT_WAIT)
        self.set_name(name)
        sleep(SHORT_WAIT)
        self.set_code(code)
        sleep(MEDIUM_WAIT)
        self.set_term(term)

    def retrieve_success_message(self):
        return self.retrieve_element_text("notification_xpath", self.locators.notification_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_error_xpath", self.locators.notification_error_xpath)