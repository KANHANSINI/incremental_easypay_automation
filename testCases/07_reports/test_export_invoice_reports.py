from self import self
from pageObjects.LoginPage import LoginPage
from pageObjects.ReportsPage import ReportsPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class TestReports:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_export_invoice_reports(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.payment_receipts = ReportsPage(self.driver)
        sleep(MEDIUM_WAIT)
        self.payment_receipts.click_reports()
        sleep(SHORT_WAIT)
        self.payment_receipts.click_invoice_reports()
        sleep(SHORT_WAIT)
        self.payment_receipts.search_invoice_report_details()
        sleep(MEDIUM_WAIT)
        self.payment_receipts.click_export()
        sleep(SHORT_WAIT)
        # Export invoice report as Excel
        self.payment_receipts.click_export_as_excel()
        sleep(SHORT_WAIT)
        self.payment_receipts.click_close()
        sleep(SHORT_WAIT)
        self.payment_receipts.click_export()
        sleep(SHORT_WAIT)
        # Export invoice report as PDF
        self.payment_receipts.click_export_as_pdf()
        sleep(SHORT_WAIT)
        self.payment_receipts.click_close()
        sleep(SHORT_WAIT)
        self.driver.close()
