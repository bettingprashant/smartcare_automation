import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login_Doctor_Page:
    login_email_xpath = "//*[@placeholder='Mobile/Email/User Id']"
    enter_btn_xpath = "//*[@class='svg-inline--fa fa-arrow-right icon-bg wcolor br-50 p-2 cursor-pointer']"
    password_xpath = "//*[@placeholder='Password']"
    login_btn_xpath = "//*[@class='bg-blue br-20px px-4 py-2 cursor-pointer wcolor']"

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.login_email_xpath).click()
        self.driver.find_element(By.XPATH, self.login_email_xpath).send_keys(email)
        self.driver.find_element(By.XPATH,self.enter_btn_xpath).click()
    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        password_input = wait.until(EC.presence_of_element_located((By.XPATH, self.password_xpath)))
        password_input.click()
        password_input.send_keys(password)
        # self.driver.find_element(By.XPATH, self.password_xpath).click()
        # self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)
        # self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    # def invalid_email(self,invalid_email):
    #     self.driver.find_element(By.XPATH, self.login_email_xpath).click()
    #     self.driver.find_element(By.XPATH, self.login_email_xpath).send_keys(invalid_email)
    #     self.driver.find_element(By.XPATH, self.enter_btn_xpath).click()

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()
        time.sleep(10)