from locators.common_locators import CommonLocators
from locators.general_terms_locators import AddNewGeneralTermsPageLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class CreateNewGeneralTermsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_new_general_terms = AddNewGeneralTermsPageLocators()
        self.locators = CommonLocators()

    def click_create_new_general_term(self):
        self.click_element("span_create_new_general_term_xpath",
                           self.locator_new_general_terms.span_create_new_general_term_xpath)

    def set_term_name(self, name):
        self.send_keys_to_element(name, "input_name_xpath", self.locator_new_general_terms.input_name_xpath)

    def set_term_code(self, code):
        self.send_keys_to_element(code, "input_code_xpath", self.locator_new_general_terms.input_code_xpath)

    def set_term(self, term):
        self.send_keys_to_element(term, "textarea_term_xpath", self.locator_new_general_terms.textarea_term_xpath)

    def click_save_and_select(self):
        self.click_element("button_save_and_select_xpath", self.locator_new_general_terms.button_save_and_select_xpath)

    def find_create_general_term(self):
        create_new_general_term = self.find_element("span_create_new_general_term_xpath",
                                                    self.locator_new_general_terms.span_create_new_general_term_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', create_new_general_term)
        sleep(SHORT_WAIT)
        self.click_element("span_create_new_general_term_xpath",
                           self.locator_new_general_terms.span_create_new_general_term_xpath)

    def create_new_general_term(self, name, code, term):
        self.set_term_name(name)
        sleep(SHORT_WAIT)
        self.set_term_code(code)
        sleep(SHORT_WAIT)
        self.set_term(term)
        sleep(SHORT_WAIT)
        self.click_save_and_select()

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locators.notification_xpath)
