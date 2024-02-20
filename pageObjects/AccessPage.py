from locators.access_locators import AccessLocators, AddNewUserLocators, DeleteUserLocators, SearchUserLocators, \
    EditUserLocators
from locators.common_locators import CommonLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class AccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_access = AccessLocators()
        self.locator_create_new_user = AddNewUserLocators()
        self.locator_delete_user = DeleteUserLocators()
        self.locator_search_user = SearchUserLocators()
        self.locator_edit_user = EditUserLocators()
        self.locators = CommonLocators()

    def click_access(self):
        self.click_element("paragraph_access_xpath", self.locator_access.paragraph_access_xpath)

    def click_users(self):
        self.click_element("span_users_xpath", self.locator_access.span_users_xpath)

    def click_add_new_user(self):
        self.click_element("button_create_new_user_xpath", self.locator_create_new_user.button_create_new_user_xpath)

    def set_email(self, email):
        self.send_keys_to_element(email, "input_email_xpath", self.locator_create_new_user.input_email_xpath)

    def click_email(self):
        self.click_element("input_email_xpath", self.locator_create_new_user.input_email_xpath)

    def set_name(self, name):
        self.send_keys_to_element(name, "input_name_xpath", self.locator_create_new_user.input_name_xpath)

    def click_name(self):
        self.click_element("input_name_xpath", self.locator_create_new_user.input_name_xpath)

    def set_password(self, password):
        self.send_keys_to_element(password, "input_password_xpath", self.locator_create_new_user.input_password_xpath)

    def click_password(self):
        self.click_element("input_password_xpath", self.locator_create_new_user.input_password_xpath)

    def set_confirm_password(self, password):
        self.send_keys_to_element(password, "input_confirm_password_xpath",
                                  self.locator_create_new_user.input_confirm_password_xpath)

    def click_confirm_password(self):
        self.click_element("input_confirm_password_xpath", self.locator_create_new_user.input_confirm_password_xpath)

    def select_role(self):
        self.click_element("span_assign_role_xpath", self.locator_create_new_user.span_assign_role_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_assign_a_role_xpath", self.locator_create_new_user.span_assign_a_role_xpath)

    def select_hotel(self):
        self.click_element("span_assign_hotel_xpath", self.locator_create_new_user.span_assign_hotel_xpath)
        sleep(SHORT_WAIT)

    def click_save(self):
        save = self.find_element("button_save_xpath", self.locator_create_new_user.button_save_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', save)
        sleep(SHORT_WAIT)
        self.click_element("button_save_xpath", self.locator_create_new_user.button_save_xpath)

    def retrieve_success_message(self):
        return self.retrieve_element_text("notification_xpath", self.locators.notification_xpath)

    def delete_user(self):
        self.click_element("icon_delete_xpath", self.locator_delete_user.icon_delete_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_accept_delete_xpath", self.locator_delete_user.button_accept_delete_xpath)

    def set_search(self, name):
        self.send_keys_to_element(name, "input_search_xpath", self.locator_search_user.input_search_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_error_xpath", self.locators.notification_error_xpath)

    def error_message(self):
        return self.retrieve_element_text("span_error_xpath", self.locator_create_new_user.span_error_xpath)

    def click_edit(self):
        self.click_element("icon_edit_xpath", self.locator_edit_user.icon_edit_xpath)

    def create_new_user(self, email, name, password, confirm_password):
        self.click_add_new_user()
        sleep(SHORT_WAIT)
        self.set_email(email)
        sleep(SHORT_WAIT)
        self.set_name(name)
        sleep(SHORT_WAIT)
        self.set_password(password)
        sleep(SHORT_WAIT)
        self.set_confirm_password(confirm_password)
        sleep(SHORT_WAIT)
        self.select_role()
        sleep(SHORT_WAIT)
        self.select_hotel()
        sleep(SHORT_WAIT)
        self.click_save()

    def search_user_by_name(self, name):
        self.set_search(name)
        sleep(SHORT_WAIT)
        result = self.find_element("td_name_xpath", self.locator_search_user.td_name_xpath).text
        assert result == "Ishadi", f"Expected result: 'Ishadi', Actual result: {result}"
        print("Searched Result:", result)

    def search_user_by_email(self, email):
        self.clear_fields("input_search_xpath", self.locator_search_user.input_search_xpath)
        sleep(SHORT_WAIT)
        self.set_search(email)
        sleep(SHORT_WAIT)
        result = self.find_element("td_email_xpath", self.locator_search_user.td_email_xpath).text
        assert result == "ishadi@ceydigital.com", f"Expected result: 'ishadi@ceydigital.com', Actual result: {result}"
        print("Searched Result:", result)

    def search_user_by_role(self, role):
        self.clear_fields("input_search_xpath", self.locator_search_user.input_search_xpath)
        sleep(SHORT_WAIT)
        self.set_search(role)
        sleep(SHORT_WAIT)
        result = self.find_element("td_role_xpath", self.locator_search_user.td_role_xpath).text
        assert result == "Front Office", f"Expected result: 'Front Office', Actual result: {result}"
        print("Searched Result:", result)

    def create_new_user_with_same_email(self, email, name):
        self.click_add_new_user()
        sleep(SHORT_WAIT)
        self.set_email(email)
        sleep(SHORT_WAIT)
        self.set_name(name)

    def create_new_user_with_invalid_email(self, email):
        self.click_add_new_user()
        sleep(SHORT_WAIT)
        self.set_email(email)
        sleep(SHORT_WAIT)
        result = self.find_element("td_name_xpath", self.locator_create_new_user.span_error_xpath).text
        assert result == "invalid Syntax", f"Expected result: 'invalid Syntax', Actual result: {result}"
        print("Searched Result:", result)

    def create_new_user_without_email(self):
        self.click_add_new_user()
        sleep(SHORT_WAIT)
        self.click_email()
        sleep(SHORT_WAIT)
        self.set_name("test")
        sleep(SHORT_WAIT)
        result = self.find_element("td_name_xpath", self.locator_create_new_user.span_error_xpath).text
        assert result == "Email is required", f"Expected result: 'Email is required', Actual result: {result}"
        print("Searched Result:", result)

    def create_new_user_without_enter_name(self, email, password):
        self.click_add_new_user()
        sleep(SHORT_WAIT)
        self.set_email(email)
        sleep(SHORT_WAIT)
        self.click_name()
        sleep(SHORT_WAIT)
        self.set_password(password)
        result = self.find_element("td_name_xpath", self.locator_create_new_user.mat_error_name_xpath).text
        assert result == "Nae is required", f"Expected result: 'Nae is required', Actual result: {result}"
        print("Searched Result:", result)

    def create_new_user_without_enter_password(self):
        self.click_add_new_user()
        sleep(SHORT_WAIT)
        self.click_password()
        sleep(SHORT_WAIT)
        self.click_confirm_password()
        sleep(SHORT_WAIT)
        result = self.find_element("td_name_xpath", self.locator_create_new_user.span_error_xpath).text
        assert result == "Password is required", f"Expected result: 'Password is required', Actual result: {result}"
        print("Searched Result:", result)

    def create_new_user_with_enter_invalid_password(self, password):
        self.click_add_new_user()
        sleep(SHORT_WAIT)
        self.set_password(password)
        sleep(SHORT_WAIT)
        result = self.find_element("td_name_xpath", self.locator_create_new_user.span_error_xpath).text
        assert result == ("Password need to have Minimum 8 Characters, "
                          "At least one Special Character, At least one Capital Letter, "
                          "At least one number"), (f"Expected result: 'Password need to have Minimum 8 Characters, "
                                                   f"At least one Special Character, "
                                                   f"At least one Capital Letter, At least one number', "
                                                   f"Actual result: {result}")
        print("Searched Result:", result)

    def edit_user(self):
        self.click_edit()
        sleep(SHORT_WAIT)
        # self.select_hotel()
        # sleep(SHORT_WAIT)
        self.click_save()
        sleep(SHORT_WAIT)
