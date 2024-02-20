from locators.item_type_locators import AddNewItemTypeLocators, EditItemTypeLocators, DeleteItemTypeLocators
from locators.common_locators import CommonLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import SHORT_WAIT, sleep, MEDIUM_WAIT


class ItemTypePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CommonLocators()
        self.locators_add_new_item_type = AddNewItemTypeLocators()
        self.locators_edit_item_type = EditItemTypeLocators()
        self.locators_delete_item_type = DeleteItemTypeLocators()

    def click_item_type(self):
        self.click_element("span_item_type_xpath", self.locators_add_new_item_type.span_item_type_xpath)

    def click_add_new_item_type(self):
        self.click_element("button_add_new_item_type_xpath",
                           self.locators_add_new_item_type.button_add_new_item_type_xpath)

    def set_name(self, name):
        self.send_keys_to_element(name, "input_name_xpath", self.locators_add_new_item_type.input_name_xpath)

    def set_code(self, code):
        self.send_keys_to_element(code, "input_code_xpath", self.locators_add_new_item_type.input_code_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators_add_new_item_type.button_save_xpath)

    def click_edit_button(self):
        self.click_element("icon_edit_item_type_xpath", self.locators_edit_item_type.icon_edit_item_type_xpath)

    def set_edit_name(self, name):
        self.click_element("input_edit_name_xpath", self.locators_edit_item_type.input_edit_name_xpath)
        sleep(SHORT_WAIT)
        self.clear_fields("input_edit_name_xpath", self.locators_edit_item_type.input_edit_name_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(name, "input_edit_name_xpath", self.locators_edit_item_type.input_edit_name_xpath)

    def click_edit_save(self):
        self.click_element("button_save_xpath", self.locators_edit_item_type.button_save_xpath)

    def click_delete(self):
        self.click_element("icon_delete_item_type_xpath", self.locators_delete_item_type.icon_delete_item_type_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_delete_accept_xpath", self.locators_delete_item_type.button_delete_accept_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_ok_xpath", self.locators_delete_item_type.button_ok_xpath)

    def retrieve_success_message(self):
        return self.retrieve_element_text("notification_xpath", self.locators.notification_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_error_xpath", self.locators.notification_error_xpath)

    def create_new_item_type(self, name, code):
        self.set_name(name)
        sleep(SHORT_WAIT)
        self.set_code(code)
        sleep(SHORT_WAIT)
        self.click_save()

    def edit_item_type(self, name):
        self.click_edit_button()
        sleep(MEDIUM_WAIT)
        self.set_edit_name(name)
        sleep(SHORT_WAIT)
        self.click_edit_save()
