from locators.common_locators import CommonLocators
from locators.invoice_locators import InvoicePageLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, LONG_WAIT


class InvoicesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = InvoicePageLocators()
        self.locators = CommonLocators()

    def click_invoices(self):
        self.click_element("list_invoices_xpath", self.locator.list_invoices_xpath)

    def click_actions(self):
        self.click_element("img_actions_xpath", self.locator.img_actions_xpath)

    def click_actions_paid(self):
        self.click_element("img_actions_paid_xpath", self.locator.img_actions_paid_xpath)

    def click_view(self):
        self.click_element("div_view_xpath", self.locator.div_view_xpath)
        sleep(MEDIUM_WAIT)
        heading = self.find_element("tr_page_end_xpath", self.locator.tr_page_end_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', heading)
        sleep(SHORT_WAIT)
        self.click_element("hyperlink_receipt_xpath", self.locator.hyperlink_receipt_xpath)
        sleep(SHORT_WAIT)
        self.click_element("hyperlink_payments_logs_xpath", self.locator.hyperlink_payments_logs_xpath)
        sleep(SHORT_WAIT)
        self.click_element("hyperlink_mail_logs_xpath", self.locator.hyperlink_mail_logs_xpath)
        sleep(SHORT_WAIT)
        self.click_element("hyperlink_invoice_logs_xpath", self.locator.hyperlink_invoice_logs_xpath)

    def click_view_paid(self):
        self.click_element("div_view_paid_xpath", self.locator.div_view_paid_xpath)
        sleep(MEDIUM_WAIT)
        heading = self.find_element("tr_page_end_xpath", self.locator.tr_page_end_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', heading)
        sleep(SHORT_WAIT)
        self.click_element("hyperlink_receipt_xpath", self.locator.hyperlink_receipt_xpath)
        sleep(SHORT_WAIT)
        self.click_element("hyperlink_payments_logs_xpath", self.locator.hyperlink_payments_logs_xpath)
        sleep(SHORT_WAIT)
        self.click_element("hyperlink_mail_logs_xpath", self.locator.hyperlink_mail_logs_xpath)
        sleep(SHORT_WAIT)
        self.click_element("hyperlink_invoice_logs_xpath", self.locator.hyperlink_invoice_logs_xpath)

    def click_close(self):
        self.click_element("button_close_xpath", self.locator.button_close_xpath)

    def click_edit(self):
        self.click_element("list_edit_xpath", self.locator.list_edit_xpath)

    def click_save(self):
        self.click_element("button_save_xpath", self.locator.button_save_xpath)

    def click_send_email(self):
        self.click_element("button_send_email_xpath", self.locator.button_send_email_xpath)

    def click_generate_link(self):
        self.click_element("button_generate_link_xpath", self.locator.button_generate_link_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_copy_link_xpath", self.locator.button_copy_link_xpath)
        sleep(SHORT_WAIT)
        self.click_element("hyperlink_close_xpath", self.locator.hyperlink_close_xpath)

    def click_print_and_preview(self):
        self.click_element("button_print_and_preview_xpath", self.locator.button_print_and_preview_xpath)

    def click_close_invoice(self):
        self.click_element("button_close_edit_xpath", self.locator.button_close_edit_xpath)

    def set_search_name(self, search):
        self.clear_fields("input_search_xpath", self.locator.input_search_xpath)
        sleep(SHORT_WAIT)
        self.click_element("input_search_xpath", self.locator.input_search_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(search, "input_search_xpath", self.locator.input_search_xpath)

    def click_delete(self):
        self.click_element("list_delete_xpath", self.locator.list_delete_xpath)
        sleep(SHORT_WAIT)
        # self.click_element("button_accept_delete_xpath", self.locator.button_accept_delete_xpath)
        self.click_element("button_cancel_xpath", self.locator.button_cancel_xpath)

    def retrieve_success_message(self):
        return self.retrieve_element_text("notification_xpath", self.locators.notification_xpath)

    def invoice_action_view_pending_invoices(self):
        self.click_invoices()
        sleep(SHORT_WAIT)
        self.set_search_name("Nir")
        sleep(SHORT_WAIT)
        alert = self.driver.switch_to.alert
        alert.accept()
        self.click_actions()
        sleep(SHORT_WAIT)
        self.click_view()
        sleep(SHORT_WAIT)
        self.click_close()

    def invoice_action_view_paid_invoices(self):
        self.click_actions_paid()
        sleep(SHORT_WAIT)
        self.click_view_paid()
        sleep(SHORT_WAIT)
        self.click_close()

    def edit_action(self):
        self.click_invoices()
        sleep(MEDIUM_WAIT)
        self.click_actions()
        sleep(MEDIUM_WAIT)
        self.click_edit()
        sleep(MEDIUM_WAIT)

    def invoice_action_edit(self):
        self.edit_action()
        self.click_save()

    def invoice_action_send_email(self):
        self.edit_action()
        self.click_send_email()

    def invoice_action_generate_link(self):
        self.edit_action()
        self.click_generate_link()
        sleep(SHORT_WAIT)

    def invoice_action_print_and_preview(self):
        self.edit_action()
        self.click_print_and_preview()
        sleep(SHORT_WAIT)

    def invoice_action_close(self):
        self.edit_action()
        self.click_close_invoice()
        sleep(SHORT_WAIT)

    def invoice_actions_delete(self):
        self.click_actions()
        sleep(MEDIUM_WAIT)
        self.click_delete()

