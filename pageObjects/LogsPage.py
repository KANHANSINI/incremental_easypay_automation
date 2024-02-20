from locators.common_locators import CommonLocators
from locators.logs_locators import LogsPageLocators, EmailLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class LogsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_logs = LogsPageLocators()
        self.locator_email_logs = EmailLocators()
        self.locators = CommonLocators()

    def click_logs(self):
        self.click_element("paragraph_logs_xpath", self.locator_logs.paragraph_logs_xpath)

    def click_email_logs(self):
        self.click_element("span_email_logs_xpath", self.locator_email_logs.span_email_logs_xpath)

    def click_payment_logs(self):
        self.click_element("span_payment_logs_xpath", self.locator_email_logs.span_payment_logs_xpath)

    def click_action(self):
        self.click_element("icon_actions_xpath", self.locator_email_logs.icon_actions_xpath)

    def click_close(self):
        self.click_element("icon_close_xpath", self.locator_email_logs.icon_close_xpath)

    def search_by_name(self, name):
        self.send_keys_to_element(name, "input_search_xpath", self.locator_email_logs.input_search_xpath)
        result = self.find_element("td_recipients_name_xpath", self.locator_email_logs.td_recipients_name_xpath).text
        assert result == "Nirant Sarin", f"Expected result: 'Nirant Sarin', Actual result: {result}"
        print("Searched Result:", result)

    def search_by_invoice_number(self, number):
        self.clear_fields("input_search_xpath", self.locator_email_logs.input_search_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(number, "input_search_xpath", self.locator_email_logs.input_search_xpath)
        result = self.find_element("td_invoice_number_xpath", self.locator_email_logs.td_invoice_number_xpath).text
        assert result == "Test1663033276837548", f"Expected result: 'Test1663033276837548', Actual result: {result}"
        print("Searched Result:", result)

    def search_by_invoice_date(self, date):
        self.clear_fields("input_search_xpath", self.locator_email_logs.input_search_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(date, "input_search_xpath", self.locator_email_logs.input_search_xpath)
        result = self.find_element("td_date_xpath", self.locator_email_logs.td_date_xpath).text
        assert result == "2022-03-04", f"Expected result: '2022-03-04', Actual result: {result}"
        print("Searched Result:", result)

    def search_by_invoice_subject(self, subject):
        self.clear_fields("input_search_xpath", self.locator_email_logs.input_search_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(subject, "input_search_xpath", self.locator_email_logs.input_search_xpath)
        result = self.find_element("td_subject_xpath", self.locator_email_logs.td_subject_xpath).text
        assert result == "Payment Failure - TESTRESRV02122020111", \
            f"Expected result: 'Payment Failure - TESTRESRV02122020111', Actual result: {result}"
        print("Searched Result:", result)

    def search_by_confirmation_number(self, confirmation_number):
        self.clear_fields("input_search_xpath", self.locator_email_logs.input_search_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(confirmation_number, "input_search_xpath", self.locator_email_logs.input_search_xpath)
        result = self.find_element("td_confirmation_number_xpath", self.locator_email_logs.td_confirmation_number_xpath).text
        assert result == "TESTRESRV113221", f"Expected result: 'TESTRESRV113221', Actual result: {result}"
        print("Searched Result:", result)

    def search_by_date(self, date):
        self.clear_fields("input_search_xpath", self.locator_email_logs.input_search_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(date, "input_search_xpath", self.locator_email_logs.input_search_xpath)
        result = self.find_element("td_date_time_xpath", self.locator_email_logs.td_date_time_xpath).text
        assert result == "25-Jun-2019 07:50:42 PM", f"Expected result: '25-Jun-2019 07:50:42 PM', Actual result: {result}"
        print("Searched Result:", result)

    def search_by_amount(self, amount):
        self.clear_fields("input_search_xpath", self.locator_email_logs.input_search_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(amount, "input_search_xpath", self.locator_email_logs.input_search_xpath)
        result = self.find_element("td_amount_xpath", self.locator_email_logs.td_amount_xpath).text
        assert result == "504.00", f"Expected result: '504.00', Actual result: {result}"
        print("Searched Result:", result)

    def search_by_invoice_number_payment_log(self, number):
        self.clear_fields("input_search_xpath", self.locator_email_logs.input_search_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(number, "input_search_xpath", self.locator_email_logs.input_search_xpath)
        result = self.find_element("td_invoice_number_payment_log_xpath",
                                   self.locator_email_logs.td_invoice_number_payment_log_xpath).text
        assert result == "Test1646764533558606", f"Expected result: 'Test1646764533558606', Actual result: {result}"
        print("Searched Result:", result)
