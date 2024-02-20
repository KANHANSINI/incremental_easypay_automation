from locators.common_locators import CommonLocators
from locators.setup_locators import SetupPageLocators
from pageObjects.BasePage import BasePage


class SetupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_setup = SetupPageLocators()
        self.locators = CommonLocators()

    def click_setup(self):
        self.click_element("list_setup_xpath", self.locator_setup.list_setup_xpath)
