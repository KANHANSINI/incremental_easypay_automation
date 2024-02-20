from locators.common_locators import CommonLocators
from locators.guest_locators import CreateNewGuestPageLocators, AddNewGuestPageLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class CreateNewGuestPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CreateNewGuestPageLocators()
        self.locator_add_guest = AddNewGuestPageLocators()
        self.locators = CommonLocators()

    def click_create_new_invoice(self):
        self.click_element("list_create_new_invoice_xpath", self.locator.list_create_new_invoice_xpath)
        sleep(MEDIUM_WAIT)
        self.click_element("link_create_new_invoice_xpath", self.locator.link_create_new_invoice_xpath)

    def click_guest(self):
        self.click_element("span_guest_xpath", self.locator.span_guest_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_add_new_guest_xpath", self.locator.button_add_new_guest_xpath)

    def select_guest(self):
        self.click_element("input_select_guest_xpath", self.locator.input_select_guest_xpath)
        sleep(MEDIUM_WAIT)
        self.click_element("option_create_new_guest_xpath", self.locator.span_create_new_guest_xpath)
        sleep(SHORT_WAIT)

    def create_new_guest(self, first_name, last_name, email, phone_number, address_1, address_2, zip_code):
        self.send_keys_to_element(first_name, "input_first_name_xpath", self.locator.input_first_name_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(last_name, "input_last_name_xpath", self.locator.input_last_name_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(email, "input_email_xpath", self.locator.input_email_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(phone_number, "input_phone_number_xpath", self.locator.input_phone_number_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(address_1, "input_address_line_1_xpath", self.locator.input_address_line_1_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(address_2, "input_address_line_2_xpath", self.locator.input_address_line_2_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_select_country_xpath", self.locator.div_select_country_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_country_xpath", self.locator.span_country_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_select_state_xpath", self.locator.div_select_state_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_state_xpath", self.locator.span_state_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_select_city_xpath", self.locator.div_select_city_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_city_xpath", self.locator.option_city_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(zip_code, "input_zip_code_xpath", self.locator.input_zip_code_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_save_and_select_xpath", self.locator.button_save_and_select_xpath)

    def add_new_guest(self, first_name, last_name, email, phone_number, address_1, address_2, zip_code):
        self.send_keys_to_element(first_name, "input_first_name_xpath", self.locator_add_guest.input_first_name_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(last_name, "input_last_name_xpath", self.locator_add_guest.input_last_name_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(email, "input_email_xpath", self.locator_add_guest.input_email_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(phone_number, "input_phone_number_xpath",
                                  self.locator_add_guest.input_phone_number_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(address_1, "input_address_line_1_xpath",
                                  self.locator_add_guest.input_address_line_1_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(address_2, "input_address_line_2_xpath",
                                  self.locator_add_guest.input_address_line_2_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_drop_down_select_country_xpath",
                           self.locator_add_guest.span_drop_down_select_country_xpath)
        self.click_element("span_country_xpath", self.locator_add_guest.span_country_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_drop_down_select_state_xpath",
                           self.locator_add_guest.span_drop_down_select_state_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_state_xpath", self.locator_add_guest.span_state_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_drop_down_select_city_xpath", self.locator_add_guest.span_drop_down_select_city_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_city_xpath", self.locator_add_guest.span_city_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(zip_code, "input_zip_code_xpath", self.locator_add_guest.input_zip_code_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_save_xpath", self.locator_add_guest.button_save_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_error_xpath", self.locators.notification_error_xpath)

    def retrieve_success_message(self):
        return self.retrieve_element_text("notification_xpath", self.locators.notification_xpath)
