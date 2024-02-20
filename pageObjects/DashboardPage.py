from pageObjects.BasePage import BasePage
from locators.dashboard_locators import DashboardPageLocators
from locators.common_locators import CommonLocators
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = DashboardPageLocators()
        self.locators = CommonLocators()

    def click_hotel_drop_down_list(self):
        self.click_element("button_drop_down_hotel_xpath", self.locator.button_drop_down_hotel_xpath)
        sleep(SHORT_WAIT)
        self.click_element("list_hotels_xpath", self.locator.list_hotels_xpath)

    def click_date_range(self):
        self.click_element("button_date_range_selection_xpath", self.locator.button_date_range_selection_xpath)
        sleep(SHORT_WAIT)

    def select_date_range(self, date_from, date_to):
        self.click_date_range()
        self.click_element("list_today_xpath", self.locator.list_today_xpath)
        sleep(MEDIUM_WAIT)
        self.click_date_range()
        self.click_element("list_yesterday_xpath", self.locator.list_yesterday_xpath)
        sleep(MEDIUM_WAIT)
        self.click_date_range()
        self.click_element("list_last_week_xpath", self.locator.list_last_week_xpath)
        sleep(MEDIUM_WAIT)
        self.click_date_range()
        self.click_element("list_last_month_xpath", self.locator.list_last_month_xpath)
        sleep(MEDIUM_WAIT)
        self.click_date_range()
        self.click_element("list_custom_xpath", self.locator.list_custom_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(date_from, "input_from_date_xpath", self.locator.input_from_date_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(date_to, "input_to_date_xpath", self.locator.input_to_date_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_search_xpath", self.locator.button_search_xpath)

    def check_invoices(self):
        self.click_element("div_success_invoices_xpath", self.locator.div_success_invoices_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_pending_invoices_xpath", self.locator.div_pending_invoices_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_failed_invoices_xpath", self.locator.div_failed_invoices_xpath)

    def click_create_new_invoice(self):
        self.click_element("button_create_new_invoice_xpath", self.locator.button_create_new_invoice_xpath)