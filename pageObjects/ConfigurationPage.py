from locators.common_locators import CommonLocators
from locators.configuration_locators import (OrganizationDetailsLocators, PaymentSettingsLocators,
                                             EmailConfigurationLocators, TaxSetupLocators)
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class ConfigurationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_organizational_details = OrganizationDetailsLocators()
        self.locator_payment_settings = PaymentSettingsLocators()
        self.locator_email_configurations = EmailConfigurationLocators()
        self.locator_tax_setup = TaxSetupLocators()
        self.locators = CommonLocators()

    def click_configuration(self):
        self.click_element("paragraph_configuration_xpath", self.locator_organizational_details.
                           paragraph_configuration_xpath)

    def click_organizational_details(self):
        self.click_element("span_organization_details_xpath", self.locator_organizational_details.
                           span_organization_details_xpath)

    def click_payment_settings(self):
        self.click_element("span_payment_settings_xpath",
                           self.locator_payment_settings.span_payment_settings_xpath)

    def click_email_configurations(self):
        self.click_element("span_email_configurations_xpath",
                           self.locator_email_configurations.span_email_configurations_xpath)

    def click_tax_setup(self):
        self.click_element("span_tax_setup_xpath", self.locator_tax_setup.span_tax_setup_xpath)

    def set_search(self, name):
        self.send_keys_to_element(name, "input_search_xpath", self.locator_organizational_details.input_search_xpath)

    def clear_search(self):
        self.clear_fields("input_search_xpath", self.locator_organizational_details.input_search_xpath)

    def click_edit_organizational_details(self):
        self.click_element("icon_edit_xpath", self.locator_organizational_details.icon_edit_xpath)

    def click_delete_organizational_details(self):
        self.click_element("icon_delete_xpath", self.locator_organizational_details.icon_delete_xpath)

    def click_edit_payment_settings(self):
        self.click_element("icon_edit_xpath", self.locator_payment_settings.icon_edit_xpath)

    def click_delete_payment_settings(self):
        self.click_element("icon_delete_xpath", self.locator_payment_settings.icon_delete_xpath)

    def click_edit_email_configurations(self):
        self.click_element("icon_edit_xpath", self.locator_email_configurations.icon_edit_xpath)

    def click_delete_email_configurations(self):
        self.click_element("icon_delete_xpath", self.locator_email_configurations.icon_delete_xpath)

    def select_rule(self):
        self.click_element("span_visa_charges_xpath", self.locator_tax_setup.span_visa_charges_xpath)
        sleep(SHORT_WAIT)
        tourism_fee = self.find_element("span_tourism_fee_xpath", self.locator_tax_setup.span_tourism_fee_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', tourism_fee)
        self.click_element("span_tourism_fee_xpath", self.locator_tax_setup.span_tourism_fee_xpath)

    def create_new_tax_setup(self, name, percentage):
        self.click_element("button_create_new_tax_setup_xpath",
                           self.locator_tax_setup.button_create_new_tax_setup_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(name, "input_name_xpath", self.locator_tax_setup.input_name_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(percentage, "input_percentage_xpath", self.locator_tax_setup.input_percentage_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_select_rules_xpath", self.locator_tax_setup.span_select_rules_xpath)
        sleep(SHORT_WAIT)
        self.select_rule()
        sleep(SHORT_WAIT)
        self.click_element("span_rule_2_xpath", self.locator_tax_setup.span_rule_2_xpath)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_no_permission_xpath",
                                          self.locators.notification_no_permission_xpath)

    def search_org_details_by_code(self, code):
        self.set_search(code)
        sleep(SHORT_WAIT)
        result = self.find_element("td_code_xpath", self.locator_organizational_details.td_code_xpath).text
        assert result == "Test", f"Expected result: 'Test', Actual result: {result}"
        print("Searched Result:", result)

    def search_org_details_by_name(self, name):
        self.clear_search()
        sleep(SHORT_WAIT)
        self.set_search(name)
        sleep(SHORT_WAIT)
        result = self.find_element("td_name_xpath", self.locator_organizational_details.td_name_xpath).text
        assert result == "Testing Hotel", f"Expected result: 'Testing Hotel', Actual result: {result}"
        print("Searched Result:", result)

    def search_payment_settings_by_name(self, name):
        self.set_search(name)
        sleep(SHORT_WAIT)
        result = self.find_element("td_name_xpath", self.locator_payment_settings.td_name_xpath).text
        assert result == "Testing Hotel", f"Expected result: 'Testing Hotel', Actual result: {result}"
        print("Searched Result:", result)
        sleep(SHORT_WAIT)

    def search_payment_settings_by_invalid_name(self, name):
        self.clear_search()
        sleep(SHORT_WAIT)
        self.set_search(name)
        sleep(SHORT_WAIT)
        result = self.find_element("td_empty_name_xpath", self.locator_payment_settings.td_empty_name_xpath).text
        assert result == "No matching records found", (f"Expected result: 'No matching records found', Actual result: "
                                                       f"{result}")
        print("Searched Result:", result)
        sleep(SHORT_WAIT)

    def search_email_configuration_by_name(self, name):
        self.set_search(name)
        sleep(SHORT_WAIT)
        result = self.find_element("td_name_xpath", self.locator_email_configurations.td_name_xpath).text
        assert result == "Testing Hotel", f"Expected result: 'Testing Hotel', Actual result: {result}"
        print("Searched Result:", result)
        sleep(SHORT_WAIT)
