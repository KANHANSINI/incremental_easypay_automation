from selenium.webdriver.support.wait import WebDriverWait
from locators.common_locators import CommonLocators
from locators.create_invoice_locators import CreateInvoicePageLocators
from locators.create_new_discount_locators import CreateNewDiscountPageLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class CreateNewDiscountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_new_discount = CreateNewDiscountPageLocators()
        self.locator_new_invoice = CreateInvoicePageLocators()
        self.locators = CommonLocators()
        self.wait = WebDriverWait(driver, 10)

    def add_new_discount(self, name, code, amount, description):
        heading = self.find_element("heading_discounts_xpath", self.locator_new_invoice.heading_discounts_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', heading)
        sleep(SHORT_WAIT)
        self.click_element("span_select_offer_xpath", self.locator_new_invoice.span_select_offer_xpath)
        sleep(SHORT_WAIT)
        self.click_element("span_add_new_discount_xpath", self.locator_new_invoice.span_add_new_discount_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(name, "input_discount_name_xpath",
                                  self.locator_new_discount.input_discount_name_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(code, "input_discount_code_xpath",
                                  self.locator_new_discount.input_discount_code_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(amount, "input_amount_xpath", self.locator_new_discount.input_amount_xpath)
        sleep(SHORT_WAIT)
        self.send_keys_to_element(description, "input_description_xpath",
                                  self.locator_new_discount.input_description_xpath)
        sleep(SHORT_WAIT)
        self.click_element("button_save_and_select_xpath", self.locator_new_discount.button_save_and_select_xpath)
        sleep(SHORT_WAIT)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("notification_xpath", self.locators.notification_xpath)
