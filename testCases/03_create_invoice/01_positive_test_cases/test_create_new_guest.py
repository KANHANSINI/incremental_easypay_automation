import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.GuestPage import CreateNewGuestPage
from pageObjects.LoginPage import LoginPage
from test_data.create_new_guest_test_data import CreateNewGuestTestData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_create_new_item_assertion


class TestCreateInvoice:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_create_new_guest(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.create_guest_page = CreateNewGuestPage(self.driver)
        sleep(SHORT_WAIT)
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
        try:
            success_message = 'Added record successfully'
            perform_create_new_item_assertion(self.driver, self.create_guest_page, self.logger, success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="create_new_guest_failed_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

        sleep(SHORT_WAIT)
        self.driver.close()
