from locators.common_locators import CommonLocators
from locators.reports_locators import ReportLocators, PaymentReceiptsLocators, InvoiceReportsLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class ReportsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_reports = ReportLocators()
        self.locator_payment_receipts = PaymentReceiptsLocators()
        self.locator_invoice_reports = InvoiceReportsLocators()
        self.locators = CommonLocators()

    def click_reports(self):
        self.click_element("paragraph_reports_xpath", self.locator_reports.paragraph_reports_xpath)

    def click_payment_receipts(self):
        self.click_element("span_payment_receipts_xpath", self.locator_payment_receipts.span_payment_receipts_xpath)

    def click_invoice_reports(self):
        self.click_element("span_invoice_reports_xpath", self.locator_invoice_reports.span_invoice_reports_xpath)

    def set_date_from(self, date_from):
        self.send_keys_to_element(date_from, "input_date_from_xpath",
                                  self.locator_payment_receipts.input_date_from_xpath)

    def clear_date_from(self):
        self.click_element("input_date_from_xpath", self.locator_payment_receipts.input_date_from_xpath)
        sleep(SHORT_WAIT)
        self.clear_fields("input_date_from_xpath", self.locator_payment_receipts.input_date_from_xpath)

    def set_date_to(self, date_to):
        self.send_keys_to_element(date_to, "input_date_to_xpath", self.locator_payment_receipts.input_date_to_xpath)

    def clear_date_to(self):
        self.click_element("input_date_to_xpath", self.locator_payment_receipts.input_date_to_xpath)
        sleep(SHORT_WAIT)
        self.clear_fields("input_date_to_xpath", self.locator_payment_receipts.input_date_to_xpath)

    def click_search(self):
        self.click_element("button_search_xpath", self.locator_payment_receipts.button_search_xpath)

    def click_export(self):
        self.click_element("button_export_xpath", self.locator_payment_receipts.button_export_xpath)

    def click_export_as_excel(self):
        self.click_element("button_excel_xpath", self.locator_payment_receipts.button_excel_xpath)

    def click_export_as_pdf(self):
        self.click_element("button_pdf_xpath", self.locator_payment_receipts.button_pdf_xpath)

    def click_close(self):
        self.click_element("button_close_xpath", self.locator_payment_receipts.button_close_xpath)

    def click_search_invoice(self):
        self.click_element("button_search_xpath", self.locator_invoice_reports.button_search_xpath)

    def select_start_date(self):
        self.click_element("button_date_from_xpath", self.locator_invoice_reports.button_date_from_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_arrow_xpath", self.locator_invoice_reports.div_arrow_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_year_1_xpath", self.locator_invoice_reports.div_year_1_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_month_xpath", self.locator_invoice_reports.div_month_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_date_xpath", self.locator_invoice_reports.div_date_xpath)

    def select_end_date(self):
        self.click_element("button_date_to_xpath", self.locator_invoice_reports.button_date_to_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_arrow_xpath", self.locator_invoice_reports.div_arrow_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_year_2_xpath", self.locator_invoice_reports.div_year_2_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_month_xpath", self.locator_invoice_reports.div_month_xpath)
        sleep(SHORT_WAIT)
        self.click_element("div_date_xpath", self.locator_invoice_reports.div_date_xpath)

    def search_payment_receipt_details(self, date_from, date_to):
        self.set_date_from(date_from)
        sleep(SHORT_WAIT)
        self.set_date_to(date_to)
        sleep(SHORT_WAIT)
        self.click_search()
        sleep(SHORT_WAIT)
        result = self.find_element("td_name_xpath", self.locator_payment_receipts.td_name_xpath).text
        assert result == "Nirant Sarin", f"Expected result: 'Nirant Sarin', Actual result: {result}"
        print("Searched Result:", result)

    def search_invoice_report_details(self):
        self.select_start_date()
        sleep(SHORT_WAIT)
        self.select_end_date()
        sleep(SHORT_WAIT)
        self.click_search_invoice()
        sleep(SHORT_WAIT)
        result = self.find_element("td_name_xpath", self.locator_invoice_reports.td_name_xpath).text
        assert result == "Nirant Sarin", f"Expected result: 'Nirant Sarin', Actual result: {result}"
        print("Searched Result:", result)
