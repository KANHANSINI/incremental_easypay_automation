from locators.item_locators import AddNewItemPageLocators
from locators.common_locators import CommonLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class ItemsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_items = AddNewItemPageLocators()
        self.locators = CommonLocators()

    def click_items(self):
        self.click_element("span_items_xpath", self.locator_items.span_items_xpath)

    def click_add_new_item(self):
        self.click_element("button_add_new_item_xpath", self.locator_items.button_add_new_item_xpath)

    def set_item_name(self, name):
        self.send_keys_to_element(name, "input_name_xpath", self.locator_items.input_name_xpath)

    def set_item_code(self, code):
        self.send_keys_to_element(code, "input_code_xpath", self.locator_items.input_code_xpath)

    def set_item_rate(self, rate):
        self.send_keys_to_element(rate, "input_rate_xpath", self.locator_items.input_rate_xpath)

    def select_item_type(self):
        self.click_element("span_select_item_type_xpath", self.locator_items.span_select_item_type_xpath)
        sleep(SHORT_WAIT)
        self.find_element("span_item_type_xpath", self.locator_items.span_item_type_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_item_type_xpath", self.locator_items.span_item_type_xpath)

    def set_description(self, desc):
        self.send_keys_to_element(desc, "input_description_xpath", self.locator_items.input_description_xpath)

    def click_save_button(self):
        self.click_element("button_save_xpath", self.locator_items.button_save_xpath)

    def click_close(self):
        self.click_element("button_close_xpath", self.locator_items.button_close_xpath)

    def add_new_item(self, name, code, rate, desc):
        self.set_item_name(name)
        sleep(SHORT_WAIT)
        self.set_item_code(code)
        sleep(SHORT_WAIT)
        self.set_item_rate(rate)
        sleep(SHORT_WAIT)
        self.select_item_type()
        sleep(SHORT_WAIT)
        self.set_description(desc)
        sleep(SHORT_WAIT)
        self.click_save_button()
        sleep(SHORT_WAIT)
        self.click_close()

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locators.notification_xpath)
