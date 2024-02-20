from self import self
from pageObjects.LoginPage import LoginPage
from pageObjects.DashboardPage import DashboardPage
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, MEDIUM_WAIT


class TestDashboard:
    base_url = ReadConfig.get_application_url(self)
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_dashboard(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.login_to_application(self.username, self.password)
        self.dashboard = DashboardPage(self.driver)
        sleep(SHORT_WAIT)
        self.dashboard.click_hotel_drop_down_list()
        sleep(SHORT_WAIT)
        self.dashboard.select_date_range()
        sleep(MEDIUM_WAIT)
        self.driver.close()
