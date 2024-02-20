from locators.common_locators import CommonLocators
from locators.create_invoice_locators import CreateInvoicePageLocators
from locators.invoice_locators import InvoicePageLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class CreateInvoicePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CreateInvoicePageLocators()
        self.locator_invoice_page = InvoicePageLocators()
        self.locators = CommonLocators()

    def click_create_new_invoice(self):
        self.click_element("list_create_new_invoice_xpath", self.locator.list_create_new_invoice_xpath)
        sleep(SHORT_WAIT)
        self.click_element("link_create_new_invoice_xpath", self.locator.link_create_new_invoice_xpath)

    # def create_new_payment_invoice(self, guest_name, reservation_number, remark):
    #     self.click_element("input_select_guest_xpath", self.locator.input_select_guest_xpath)
    #     self.send_keys_to_element(guest_name, "input_select_guest_xpath", self.locator.input_select_guest_xpath)
    #     sleep(SHORT_WAIT)
    #     self.click_element("span_select_guest_name_xpath", self.locator.span_select_guest_name_xpath)
    #     sleep(MEDIUM_WAIT)
    #     self.send_keys_to_element(reservation_number, "input_reservation_number_xpath",
    #                               self.locator.input_reservation_number_xpath)
    #     sleep(SHORT_WAIT)
    #     self.click_element("input_room_name_xpath", self.locator.input_room_name_xpath)
    #     sleep(SHORT_WAIT)
    #     self.click_element("option_room_name_xpath", self.locator.option_room_name_xpath)
    #     sleep(SHORT_WAIT)
    #     self.click_element("button_check_in_date_xpath", self.locator.button_check_in_date_xpath)
    #     sleep(SHORT_WAIT)
    #     self.click_element("div_check_in_date_xpath", self.locator.div_check_in_date_xpath)
    #     sleep(SHORT_WAIT)
    #     self.click_element("div_check_out_date_xpath", self.locator.button_check_out_date_xpath)
    #     sleep(SHORT_WAIT)
    #     self.click_element("div_check_out_date_name_xpath", self.locator.div_check_out_date_xpath)
    #     sleep(SHORT_WAIT)
    #     remark_path = self.find_element("input_remark_xpath", self.locator.input_remark_xpath)
    #     self.driver.execute_script('arguments[0].scrollIntoView(true)', remark_path)
    #     self.send_keys_to_element(remark, "input_remark_xpath", self.locator.input_remark_xpath)

    def create_new_payment_invoice(self, reservation_number, remark):
        # self.click_element("input_select_guest_xpath", self.locator.input_select_guest_xpath)
        # self.send_keys_to_element(guest_name, "input_select_guest_xpath", self.locator.input_select_guest_xpath)
        # sleep(SHORT_WAIT)
        # self.click_element("span_select_guest_name_xpath", self.locator.span_select_guest_name_xpath)
        # sleep(MEDIUM_WAIT)
        self.send_keys_to_element(reservation_number, "input_reservation_number_xpath",
                                  self.locator.input_reservation_number_xpath)
        sleep(SHORT_WAIT)
        self.click_element("input_room_name_xpath", self.locator.input_room_name_xpath)
        sleep(SHORT_WAIT)
        self.click_element("option_room_name_xpath", self.locator.option_room_name_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_check_in_date_xpath", self.locator.button_check_in_date_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_check_in_date_xpath", self.locator.div_check_in_date_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_check_out_date_xpath", self.locator.button_check_out_date_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_check_out_date_name_xpath", self.locator.div_check_out_date_xpath)
        sleep(SHORT_WAIT)
        remark_path = self.find_element("input_remark_xpath", self.locator.input_remark_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', remark_path)
        self.send_keys_to_element(remark, "input_remark_xpath", self.locator.input_remark_xpath)

    def select_item_from_dropdown(self):
        self.find_element("div_select_item_1_xpath", self.locator.div_select_item_1_xpath)
        sleep(SHORT_WAIT)
        heading = self.find_element("hr_item_heading_xpath", self.locator.hr_item_heading_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', heading)
        sleep(SHORT_WAIT)
        self.click_element("div_select_item_1_xpath", self.locator.div_select_item_1_xpath)
        sleep(MEDIUM_WAIT)
        self.click_element("span_item_visa_charges_xpath", self.locator.span_item_visa_charges_xpath)
        sleep(SHORT_WAIT)
        self.click_element("icon_copy_item_xpath", self.locator.icon_copy_item_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_select_item_2_xpath", self.locator.div_select_item_2_xpath)
        sleep(MEDIUM_WAIT)
        self.click_element("span_item_desert_safari_xpath", self.locator.span_item_desert_safari_xpath)
        sleep(SHORT_WAIT)

    def select_discount(self):
        heading = self.find_element("heading_discounts_xpath", self.locator.heading_discounts_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', heading)
        sleep(SHORT_WAIT)
        self.click_element("span_select_offer_xpath", self.locator.span_select_offer_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_offer_xpath", self.locator.span_offer_xpath)

    def click_toggle(self):
        self.click_element("span_toggle_xpath", self.locator.span_toggle_xpath)

    def click_save_button(self):
        self.click_element("button_save_xpath", self.locator.button_save_xpath)

    def retrieve_success_message(self):
        return self.retrieve_element_text("notification_xpath", self.locators.notification_xpath)

    def click_add_new_item(self):
        self.click_element("button_add_new_item_xpath", self.locator.button_add_new_item_xpath)

    def click_clear_button(self):
        self.click_element("icon_delete_item_xpath", self.locator.icon_delete_item_xpath)

    def add_new_term(self):
        self.click_element("button_add_new_terms_xpath", self.locator.button_add_new_terms_xpath)

    def add_and_remove_item(self):
        self.click_add_new_item()
        sleep(SHORT_WAIT)
        self.click_clear_button()

    def remove_item(self):
        self.find_element("div_select_item_1_xpath", self.locator.div_select_item_1_xpath)
        sleep(SHORT_WAIT)
        heading = self.find_element("hr_item_heading_xpath", self.locator.hr_item_heading_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', heading)
        sleep(SHORT_WAIT)
        self.click_element("icon_remove_item_xpath", self.locator.icon_remove_item_xpath)
        sleep(SHORT_WAIT)
        charges = self.find_element("heading_charges_xpath", self.locator.heading_charges_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', charges)
        sleep(SHORT_WAIT)
        self.click_element("icon_remove_charges_xpath", self.locator.icon_remove_charges_xpath)
        sleep(SHORT_WAIT)
        heading = self.find_element("heading_discounts_xpath", self.locator.heading_discounts_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', heading)
        sleep(SHORT_WAIT)
        self.click_element("icon_remove_discount_xpath", self.locator.icon_remove_discount_xpath)
        sleep(SHORT_WAIT)
        general_terms = self.find_element("heading_general_terms_xpath", self.locator.heading_general_terms_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', general_terms)
        sleep(SHORT_WAIT)
        self.click_element("icon_remove_general_terms_xpath", self.locator.icon_remove_general_terms_xpath)
        sleep(SHORT_WAIT)
        self.click_element("icon_remove_payment_terms_xpath", self.locator.icon_remove_payment_terms_xpath)

    def add_item(self):
        self.find_element("div_select_item_1_xpath", self.locator.div_select_item_1_xpath)
        sleep(SHORT_WAIT)
        heading = self.find_element("hr_item_heading_xpath", self.locator.hr_item_heading_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', heading)
        sleep(SHORT_WAIT)
        self.click_element("icon_copy_item_xpath", self.locator.icon_copy_item_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_error_xpath", self.locators.notification_error_xpath)

    def add_new_item(self):
        self.find_element("div_select_item_1_xpath", self.locator.div_select_item_1_xpath)
        sleep(SHORT_WAIT)
        heading = self.find_element("hr_item_heading_xpath", self.locator.hr_item_heading_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', heading)
        sleep(SHORT_WAIT)
        self.click_element("button_add_new_item_xpath", self.locator.button_add_new_item_xpath)

    def click_copy_charges(self):
        charges = self.find_element("heading_charges_xpath", self.locator.heading_charges_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', charges)
        sleep(SHORT_WAIT)
        self.click_element("icon_copy_charges_xpath", self.locator.icon_copy_charges_xpath)

    def click_copy_discount(self):
        heading = self.find_element("heading_discounts_xpath", self.locator.heading_discounts_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', heading)
        sleep(SHORT_WAIT)
        self.click_element("icon_copy_discount_xpath", self.locator.icon_copy_discount_xpath)

    def go_to_general_terms(self):
        general_terms = self.find_element("heading_general_terms_xpath", self.locator.heading_general_terms_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', general_terms)
        sleep(SHORT_WAIT)
        self.click_element("span_general_term_xpath", self.locator.span_general_term_xpath)

    def go_to_payment_terms(self):
        payment_terms = self.find_element("heading_payment_terms_xpath", self.locator.heading_payment_terms_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', payment_terms)
        sleep(MEDIUM_WAIT)
        self.click_element("span_payment_term_xpath", self.locator.span_payment_term_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locator.button_save_xpath)

    def click_send_email(self):
        self.click_element("button_send_email_xpath", self.locator_invoice_page.button_send_email_xpath)

    def click_generate_link(self):
        self.click_element("button_generate_link_xpath", self.locator_invoice_page.button_generate_link_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_copy_link_xpath", self.locator_invoice_page.button_copy_link_xpath)
        sleep(SHORT_WAIT)
        self.click_element("hyperlink_close_xpath", self.locator_invoice_page.hyperlink_close_xpath)

    def click_print_and_preview(self):
        self.click_element("button_print_and_preview_xpath", self.locator_invoice_page.button_print_and_preview_xpath)

    def click_close_invoice(self):
        self.click_element("button_close_edit_xpath", self.locator_invoice_page.button_close_edit_xpath)

