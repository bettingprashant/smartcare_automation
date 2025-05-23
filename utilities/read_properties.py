from configparser import ConfigParser

config = ConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:
    @staticmethod
    def get_login_page_url():
        url = config.get('smartcare login info', 'login_page_url')
        return url

    @staticmethod
    def get_email():
        email = config.get('smartcare login info', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('smartcare login info', 'password')
        return password

    @staticmethod
    def get_invalid_email():
        invalid_email = config.get('smartcare login info', 'invalid_email')
        return invalid_email