import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.GuestPage import CreateNewGuestPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SetupPage import SetupPage
from test_data.create_new_guest_test_data import CreateNewGuestTestData, CreateNewGuestTestData_NegativeTesting
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT, perform_create_new_guest_negative_testing_assertion


class TestSetUp:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_add_invalid_phone_number(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.setup = SetupPage(self.driver)
        self.create_guest_page = CreateNewGuestPage(self.driver)
        sleep(SHORT_WAIT)
        self.setup.click_setup()
        sleep(MEDIUM_WAIT)
        self.create_guest_page.click_guest()
        sleep(MEDIUM_WAIT)
        self.create_guest_page.add_new_guest(CreateNewGuestTestData.first_name,
                                             CreateNewGuestTestData.last_name,
                                             CreateNewGuestTestData.email,
                                             CreateNewGuestTestData_NegativeTesting.phone_number,
                                             CreateNewGuestTestData.address_line_1,
                                             CreateNewGuestTestData.address_line_2,
                                             CreateNewGuestTestData.zip_code)
        sleep(SHORT_WAIT)
        try:
            success_message = 'Add new guest record failed, Please try again'
            perform_create_new_guest_negative_testing_assertion(self.driver, self.create_guest_page, self.logger,
                                                                success_message)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="create_new_guest_failed_scr",
                          attachment_type=AttachmentType.PNG)
            raise e

        sleep(SHORT_WAIT)
        self.driver.close()
