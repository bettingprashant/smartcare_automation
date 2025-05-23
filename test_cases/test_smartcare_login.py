import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Smartcare import Login_Doctor_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_01_Admin_Login:
    login_page_url = Read_Config.get_login_page_url()
    email = Read_Config.get_email()
    password = Read_Config.get_password()
    # invalid_username = Read_Config.get_invalid_email()
    logger = Log_Maker.log_gen()

    def test_valid_smartcare_login(self, setup):
        self.logger.info("***************test valid smartcare login started*******************")
        self.driver = setup
        self.driver.get(self.login_page_url)
        self.smartcare_lp = Login_Doctor_Page(self.driver)
        self.smartcare_lp.enter_email(self.email)
        self.smartcare_lp.enter_password(self.password)
        self.smartcare_lp.click_login()
        act_title = self.driver.title
        exp_title = "Best Clinic Management Platform for Doctors, Cloud-based Clinic Management Software in India."
        if act_title == exp_title:
            self.logger.info("**************test verification title matched********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("**************test verification title not matched********************")
            self.driver.close()
            assert False
