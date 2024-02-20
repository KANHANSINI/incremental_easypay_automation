from self import self
from pageObjects.AccessPage import AccessPage
from pageObjects.CreateInvoicePage import CreateInvoicePage
from pageObjects.DashboardPage import DashboardPage
from pageObjects.DiscountPage import DiscountPage
from pageObjects.GuestPage import CreateNewGuestPage
from pageObjects.InvoicesPage import InvoicesPage
from pageObjects.ItemTypePage import ItemTypePage
from pageObjects.ItemsPage import ItemsPage
from pageObjects.LoginPage import LoginPage
from pageObjects.LogsPage import LogsPage
from pageObjects.ReportsPage import ReportsPage
from pageObjects.RoomTypePage import RoomTypePage
from pageObjects.SetupPage import SetupPage
from pageObjects.TermsPage import TermsPage
from test_data.add_new_discount_test_data import AddNewDiscountTestData
from test_data.add_new_item_test_data import CreateNewItemTestData
from test_data.add_new_item_type_test_data import CreateNewItemTypeTestData, EditItemTypeTestData
from test_data.create_new_discount_test_data import SearchDiscountTestData
from test_data.create_new_guest_test_data import CreateNewGuestTestData
from test_data.create_new_payment_invoice_test_data import CreateNewPaymentInvoiceTestData
from test_data.room_type_test_data import AddNewRoomTypeTestData, EditRoomTypeTestData, SearchRoomTypeTestData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, LONG_WAIT


class TestAutomation:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_automation(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.dashboard = DashboardPage(self.driver)
        self.create_guest_page = CreateNewGuestPage(self.driver)
        self.create_invoice = CreateInvoicePage(self.driver)
        self.invoice_page = InvoicesPage(self.driver)
        self.setup = SetupPage(self.driver)
        self.create_guest_page = CreateNewGuestPage(self.driver)
        self.add_item = ItemsPage(self.driver)
        self.item_type = ItemTypePage(self.driver)
        self.terms = TermsPage(self.driver)
        self.discount = DiscountPage(self.driver)
        self.room_type = RoomTypePage(self.driver)
        self.logs = LogsPage(self.driver)
        self.reports = ReportsPage(self.driver)
        self.access = AccessPage(self.driver)

        # Login
        self.login_page.login_to_application(self.username, self.password)
        sleep(MEDIUM_WAIT)

        # Dashboard
        self.dashboard.click_hotel_drop_down_list()
        sleep(MEDIUM_WAIT)
        self.dashboard.select_date_range("2023/12/31", "2024/01/10")
        sleep(MEDIUM_WAIT)
        # # alert = self.driver.switch_to.alert
        # # alert.accept()
        # # sleep(SHORT_WAIT)
        # # self.dashboard.click_create_new_invoice()

        # Create New Payment Invoice
        self.create_guest_page.click_create_new_invoice()
        sleep(MEDIUM_WAIT)
        self.create_guest_page.select_guest()
        sleep(SHORT_WAIT)
        self.create_guest_page.create_new_guest(CreateNewGuestTestData.first_name,
                                                CreateNewGuestTestData.last_name,
                                                CreateNewGuestTestData.email,
                                                CreateNewGuestTestData.phone_number,
                                                CreateNewGuestTestData.address_line_1,
                                                CreateNewGuestTestData.address_line_2,
                                                CreateNewGuestTestData.zip_code)
        sleep(SHORT_WAIT)
        self.create_invoice.create_new_payment_invoice(CreateNewPaymentInvoiceTestData.reservation_number,
                                                       CreateNewPaymentInvoiceTestData.remark)
        sleep(SHORT_WAIT)
        self.create_invoice.select_item_from_dropdown()
        sleep(SHORT_WAIT)
        self.create_invoice.add_and_remove_item()
        sleep(SHORT_WAIT)
        self.create_invoice.select_discount()
        sleep(SHORT_WAIT)
        self.create_invoice.click_toggle()
        sleep(MEDIUM_WAIT)
        self.create_invoice.add_new_term()
        sleep(MEDIUM_WAIT)
        self.create_invoice.click_save_button()
        sleep(LONG_WAIT)
        self.create_invoice.click_send_email()
        sleep(SHORT_WAIT)
        self.create_invoice.click_generate_link()
        sleep(SHORT_WAIT)
        self.create_invoice.click_print_and_preview()
        sleep(SHORT_WAIT)
        self.create_invoice.click_close_invoice()
        sleep(MEDIUM_WAIT)

        # # "Edit invoices"
        # # self.invoice_page.invoice_action_close()
        # #         # sleep(SHORT_WAIT)
        # #         # self.invoice_page.invoice_action_generate_link()
        # #         # sleep(SHORT_WAIT)
        # #         # self.invoice_page.invoice_action_print_and_preview()
        # #         # sleep(SHORT_WAIT)
        # #         # self.invoice_page.click_close_invoice()
        # #         # sleep(SHORT_WAIT)
        # #         # self.invoice_page.invoice_action_edit()
        # #         # sleep(SHORT_WAIT)
        # #         # self.invoice_page.invoice_action_send_email()
        # #         # sleep(SHORT_WAIT)

        # Invoices
        self.invoice_page.invoice_action_view_pending_invoices()
        sleep(SHORT_WAIT)
        self.invoice_page.invoice_action_view_paid_invoices()
        sleep(SHORT_WAIT)
        self.invoice_page.set_search_name("Anu")
        sleep(SHORT_WAIT)
        alert = self.driver.switch_to.alert
        alert.accept()
        # sleep(SHORT_WAIT)
        sleep(MEDIUM_WAIT)
        self.invoice_page.invoice_actions_delete()

        # Create New Guest
        self.setup.click_setup()
        sleep(MEDIUM_WAIT)
        self.create_guest_page.click_guest()
        sleep(MEDIUM_WAIT)
        self.create_guest_page.add_new_guest(CreateNewGuestTestData.first_name,
                                             CreateNewGuestTestData.last_name,
                                             CreateNewGuestTestData.email,
                                             CreateNewGuestTestData.phone_number,
                                             CreateNewGuestTestData.address_line_1,
                                             CreateNewGuestTestData.address_line_2,
                                             CreateNewGuestTestData.zip_code)

        # Add New Item
        self.add_item.click_items()
        sleep(SHORT_WAIT)
        self.add_item.click_add_new_item()
        sleep(SHORT_WAIT)
        self.add_item.add_new_item(CreateNewItemTestData.name,
                                   CreateNewItemTestData.code,
                                   CreateNewItemTestData.rate,
                                   CreateNewItemTestData.description)
        sleep(SHORT_WAIT)

        # Add new item type
        self.item_type.click_item_type()
        sleep(SHORT_WAIT)
        self.item_type.click_add_new_item_type()
        sleep(SHORT_WAIT)
        self.item_type.create_new_item_type(CreateNewItemTypeTestData.name, CreateNewItemTypeTestData.code)
        sleep(MEDIUM_WAIT)
        self.item_type.edit_item_type(EditItemTypeTestData.name)
        sleep(SHORT_WAIT)
        self.item_type.click_delete()
        sleep(SHORT_WAIT)
        # # self.terms.click_terms()
        # # sleep(SHORT_WAIT)
        # # self.terms.add_new_term("abc", "efh", "dafgajhfa")

        # Add new discount
        self.setup.click_setup()
        sleep(SHORT_WAIT)
        self.discount.click_discount()
        sleep(SHORT_WAIT)
        self.discount.create_new_discount(AddNewDiscountTestData.name,
                                          AddNewDiscountTestData.code,
                                          AddNewDiscountTestData.amount,
                                          AddNewDiscountTestData.description)
        sleep(SHORT_WAIT)
        self.discount.edit_discount(AddNewDiscountTestData.percentage)
        sleep(SHORT_WAIT)
        self.discount.click_delete()
        sleep(SHORT_WAIT)
        self.discount.search_discount_by_name(SearchDiscountTestData.name)
        sleep(SHORT_WAIT)
        self.discount.search_discount_by_code(SearchDiscountTestData.code)
        sleep(SHORT_WAIT)

        # Add new room type
        self.room_type.click_room_type()
        sleep(SHORT_WAIT)
        self.room_type.click_add_new_room_type()
        sleep(SHORT_WAIT)
        self.room_type.add_new_room_type(AddNewRoomTypeTestData.name, AddNewRoomTypeTestData.code)
        sleep(SHORT_WAIT)
        self.room_type.edit_name(EditRoomTypeTestData.name)
        sleep(SHORT_WAIT)
        # self.room_type.click_remove_item()
        # sleep(MEDIUM_WAIT)
        self.room_type.set_search_by_name(SearchRoomTypeTestData.name)
        sleep(SHORT_WAIT)
        self.room_type.set_search_by_code(SearchRoomTypeTestData.code)
        sleep(SHORT_WAIT)

        # View email logs
        self.logs.click_logs()
        sleep(SHORT_WAIT)
        self.logs.click_email_logs()
        sleep(MEDIUM_WAIT)
        self.logs.search_by_name("Nirant Sarin")
        sleep(MEDIUM_WAIT)
        self.logs.search_by_invoice_date("2022-03-04")
        sleep(MEDIUM_WAIT)
        self.logs.search_by_invoice_subject("Payment Failure - TESTRESRV02122020111")
        sleep(MEDIUM_WAIT)
        self.logs.click_payment_logs()
        sleep(SHORT_WAIT)
        self.logs.search_by_confirmation_number("TESTRESRV113221")
        sleep(MEDIUM_WAIT)
        self.logs.search_by_date("25-Jun-2019")
        sleep(MEDIUM_WAIT)
        self.logs.search_by_invoice_number_payment_log("Test1646764533558606")
        sleep(MEDIUM_WAIT)
        self.logs.search_by_amount("504.00")
        sleep(MEDIUM_WAIT)

        # Access invoice reports
        self.reports.click_reports()
        sleep(SHORT_WAIT)
        self.reports.click_invoice_reports()
        sleep(SHORT_WAIT)
        self.reports.search_invoice_report_details()
        sleep(MEDIUM_WAIT)
        self.reports.click_export()
        sleep(SHORT_WAIT)
        # Export invoice report as Excel
        self.reports.click_export_as_excel()
        sleep(SHORT_WAIT)
        self.reports.click_close()
        sleep(SHORT_WAIT)
        self.reports.click_export()
        sleep(SHORT_WAIT)
        # Export invoice report as PDF
        self.reports.click_export_as_pdf()
        sleep(SHORT_WAIT)
        self.reports.click_close()
        sleep(SHORT_WAIT)
        self.reports.click_payment_receipts()
        sleep(SHORT_WAIT)
        self.reports.search_payment_receipt_details("2/29/2020", "3/29/2020")
        sleep(SHORT_WAIT)
        self.reports.click_export()
        sleep(SHORT_WAIT)
        self.reports.click_export_as_excel()
        sleep(SHORT_WAIT)
        self.reports.click_close()
        sleep(SHORT_WAIT)
        self.reports.click_export()
        sleep(SHORT_WAIT)
        self.reports.click_export_as_pdf()
        sleep(SHORT_WAIT)
        self.reports.click_close()
        sleep(SHORT_WAIT)

        self.access.click_access()
        sleep(SHORT_WAIT)
        self.access.click_users()
        sleep(SHORT_WAIT)
        self.access.create_new_user("xeciyec104@ikuromi.com", "Maya Patel",
                                    "test@1234", "test@1234")
