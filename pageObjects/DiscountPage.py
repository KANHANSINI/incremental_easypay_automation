from locators.common_locators import CommonLocators
from locators.discount_locators import (CreateDiscountLocators, EditDiscountLocators, DeleteDiscountLocators,
                                        SearchDiscountLocators)
from pageObjects.BasePage import BasePage
from utilities.test_utils import SHORT_WAIT, sleep


class DiscountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_discount = CreateDiscountLocators()
        self.locator_edit_discount = EditDiscountLocators()
        self.locator_delete_discount = DeleteDiscountLocators()
        self.locator_search_discount = SearchDiscountLocators()
        self.locators = CommonLocators()

    def click_discount(self):
        self.click_element("list_discount_xpath", self.locator_discount.list_discount_xpath)

    def click_add_new_discount(self):
        self.click_element("button_add_new_discount_xpath", self.locator_discount.button_add_new_discount_xpath)

    def set_name(self, name):
        self.send_keys_to_element(name, "input_name_xpath", self.locator_discount.input_name_xpath)

    def set_code(self, code):
        self.send_keys_to_element(code, "input_code_xpath", self.locator_discount.input_code_xpath)

    def set_amount(self, amount):
        self.send_keys_to_element(amount, "input_amount_xpath", self.locator_discount.input_amount_xpath)

    def set_percentage(self, percentage):
        self.send_keys_to_element(percentage, "input_percentage_xpath", self.locator_discount.input_percentage_xpath)

    def set_description(self, desc):
        self.send_keys_to_element(desc, "textarea_description_xpath", self.locator_discount.textarea_description_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locator_discount.button_save_xpath)

    def click_edit(self):
        self.click_element("icon_edit_discount_xpath", self.locator_edit_discount.icon_edit_discount_xpath)

    def edit_amount(self, amount):
        self.send_keys_to_element(amount, "input_edit_percentage_xpath",
                                  self.locator_edit_discount.input_edit_percentage_xpath)

    def click_save_edited_details(self):
        self.click_element("button_save_xpath", self.locator_edit_discount.button_save_xpath)

    def click_delete(self):
        self.click_element("icon_delete_discount_xpath", self.locator_delete_discount.icon_delete_discount_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locator_delete_discount.button_accept_delete_xpath)

    def search_discount_by_name(self, name):
        self.send_keys_to_element(name, "input_search_xpath",
                                  self.locator_search_discount.input_search_xpath)
        result = self.find_element("td_name_xpath", self.locator_search_discount.td_name_xpath).text
        assert result == "Test Discount", f"Expected result: 'Test Discount', Actual result: {result}"
        print("Searched Result:", result)

    def search_discount_by_code(self, code):
        self.clear_fields("input_search_xpath", self.locator_search_discount.input_search_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(code, "input_search_xpath",
                                  self.locator_search_discount.input_search_xpath)
        result = self.find_element("td_code_xpath", self.locator_search_discount.td_code_xpath).text
        assert result == "TD", f"Expected result: 'TD', Actual result: {result}"
        print("Searched Result:", result)

    def clear_search_field(self):
        self.clear_fields("input_search_xpath", self.locator_search_discount.input_search_xpath)

    def retrieve_success_message(self):
        return self.retrieve_element_text("notification_xpath", self.locators.notification_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_error_xpath", self.locators.notification_error_xpath)

    def create_new_discount(self, name, code, amount, desc):
        self.click_add_new_discount()
        sleep(SHORT_WAIT)
        self.set_name(name)
        sleep(SHORT_WAIT)
        self.set_code(code)
        sleep(SHORT_WAIT)
        self.set_amount(amount)
        sleep(SHORT_WAIT)
        # self.set_percentage(percentage)
        # sleep(SHORT_WAIT)
        self.set_description(desc)
        sleep(SHORT_WAIT)
        self.click_save()

    def edit_discount(self, amount):
        self.click_edit()
        sleep(SHORT_WAIT)
        self.click_element("input_edit_percentage_xpath", self.locator_edit_discount.input_edit_percentage_xpath)
        sleep(SHORT_WAIT)
        self.clear_fields("input_edit_percentage_xpath", self.locator_edit_discount.input_edit_percentage_xpath)
        sleep(SHORT_WAIT)
        self.edit_amount(amount)
        sleep(SHORT_WAIT)
        self.click_save_edited_details()

    def create_new_discount_without_enter_amount_or_discount(self, name, code, desc):
        self.click_add_new_discount()
        sleep(SHORT_WAIT)
        self.set_name(name)
        sleep(SHORT_WAIT)
        self.set_code(code)
        sleep(SHORT_WAIT)
        self.set_description(desc)
        sleep(SHORT_WAIT)
        self.click_save()
