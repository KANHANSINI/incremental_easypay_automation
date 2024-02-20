import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url(self):
        url = config.get('common data', 'base_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common data', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('common data', 'invalid_username')
        return invalid_username

    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('common data', 'invalid_password')
        return invalid_password
