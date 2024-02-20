from locators.common_locators import CommonLocators
from locators.room_type_locators import AddNewRoomTypeLocators, EditRoomTypeLocators, DeleteRoomTypeLocators, \
    SearchRoomTypeLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import SHORT_WAIT, sleep


class RoomTypePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CommonLocators()
        self.locators_add_new_room_type = AddNewRoomTypeLocators()
        self.locators_edit_room_type = EditRoomTypeLocators()
        self.locators_delete_room_type = DeleteRoomTypeLocators()
        self.locators_search_room_type = SearchRoomTypeLocators()

    def click_room_type(self):
        self.click_element("span_room_type_xpath", self.locators_add_new_room_type.span_room_type_xpath)

    def click_add_new_room_type(self):
        self.click_element("button_add_new_room_type_xpath",
                           self.locators_add_new_room_type.button_add_new_room_type_xpath)

    def set_name(self, name):
        self.send_keys_to_element(name, "input_name_xpath", self.locators_add_new_room_type.input_name_xpath)

    def set_code(self, code):
        self.send_keys_to_element(code, "input_code_xpath", self.locators_add_new_room_type.input_code_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locators_add_new_room_type.button_save_xpath)

    def click_remove_item(self):
        self.click_element("icon_remove_item_xpath", self.locators_delete_room_type.icon_remove_item_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locators_delete_room_type.button_accept_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_ok_xpath", self.locators_delete_room_type.button_ok_xpath)

    def retrieve_success_message(self):
        return self.retrieve_element_text("notification_xpath", self.locators.notification_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_no_permission_xpath",
                                          self.locators.notification_no_permission_xpath)

    def set_search_by_name(self, name):
        self.send_keys_to_element(name, "input_search_name_xpath",
                                  self.locators_search_room_type.input_search_name_xpath)
        result = self.find_element("td_name_xpath", self.locators_search_room_type.td_name_xpath).text
        assert result == "1501-Deluxe(DLX)", (f"Expected result: '1501-Deluxe(DLX)', "
                                              f""f"Actual result: {result}")
        print("Searched Result:", result)

    def set_search_by_code(self, code):
        self.clear_fields("input_search_name_xpath", self.locators_search_room_type.input_search_name_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(code, "input_search_name_xpath",
                                  self.locators_search_room_type.input_search_name_xpath)
        result = self.find_element("td_code_xpath", self.locators_search_room_type.td_code_xpath).text
        assert result == "TBPV", f"Expected result: 'TBPV', Actual result: {result}"
        print("Searched Result:", result)

    def edit_name(self, name):
        self.click_element("icon_edit_xpath", self.locators_edit_room_type.icon_edit_xpath)
        sleep(SHORT_WAIT)
        self.clear_fields("input_name_xpath", self.locators_edit_room_type.input_name_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(name, "input_name_xpath", self.locators_edit_room_type.input_name_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_save_xpath", self.locators_edit_room_type.button_save_xpath)

    def add_new_room_type(self, name, code):
        self.set_name(name)
        sleep(SHORT_WAIT)
        self.set_code(code)
        sleep(SHORT_WAIT)
        self.click_save()
