import allure
from allure_commons.types import AttachmentType
from self import self
from pageObjects.LoginPage import LoginPage
from pageObjects.RoomTypePage import RoomTypePage
from pageObjects.SetupPage import SetupPage
from test_data.room_type_test_data import SearchRoomTypeTestData
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class TestSetUp:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_search_room_type_by_name(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.setup = SetupPage(self.driver)
        self.search_room_type = RoomTypePage(self.driver)
        sleep(SHORT_WAIT)
        self.setup.click_setup()
        sleep(MEDIUM_WAIT)
        self.search_room_type.click_room_type()
        sleep(SHORT_WAIT)
        self.search_room_type.set_search_by_name(SearchRoomTypeTestData.name)
        sleep(SHORT_WAIT)
        self.driver.close()

    def test_search_room_type_by_code(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.setup = SetupPage(self.driver)
        self.search_room_type = RoomTypePage(self.driver)
        sleep(SHORT_WAIT)
        self.setup.click_setup()
        sleep(MEDIUM_WAIT)
        self.search_room_type.click_room_type()
        sleep(SHORT_WAIT)
        self.search_room_type.set_search_by_code(SearchRoomTypeTestData.code)
        sleep(SHORT_WAIT)
        self.driver.close()
