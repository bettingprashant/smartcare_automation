import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Create_Patient:

    def __init__(self, driver):
        self.driver = driver

    select_role_xpath = "//*[@class ='role-manage-list-card doctor-color']"
    patient_list_xpath = "//li[5]//a[1]//div[1]"
    add_new_patient_xpath = "//span[contains(text(),'Add New Patients')]"
    select_gender_xpath = "//span[normalize-space()='Select gender']"
    male_gender_xpath = "//div[@class='q-item__label'][normalize-space()='Male']"
    female_gender_xpath = "//div[contains(text(),'Female')]"
    patient_fname_xpath = "//input[@placeholder='Enter first name']"
    enter_age_xpath = "//input[@placeholder='Enter age']"
    save_btn_xpath = "//span[contains(text(),'Save')]"

    def select_role(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH, self.select_role_xpath))
        ).click()
        time.sleep(20)
        # self.driver.find_element(By.XPATH, self.select_role_xpath).click()

    def patient_list(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.patient_list_xpath))
        ).click()
        time.sleep(5)
        # self.driver.find_element(By.XPATH, self.patient_list_xpath).click()

    def add_new_patient(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH, self.add_new_patient_xpath))
        ).click()
        # self.driver.find_element(By.XPATH, self.add_new_patient_xpath).click()

    def patient_name(self, fname):
        patient_name = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.patient_fname_xpath))
        )
        patient_name.click()
        patient_name.send_keys(fname)

        # self.driver.find_element(By.XPATH, self.patient_fname_xpath).click()
        # self.driver.find_element(By.XPATH, self.patient_fname_xpath).send_keys(fname)

    def select_gender(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.select_gender_xpath))
        ).click()
        time.sleep(5)
        # self.driver.find_element(By.XPATH, self.select_gender_xpath).click()

    def select_male(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.male_gender_xpath))
        ).click()
        # self.driver.find_element(By.XPATH, self.male_gender_xpath).click()

    def enter_age(self,actual_age):
        age = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.enter_age_xpath))
        )
        age.click()
        age.send_keys(actual_age)
        # self.driver.find_element(By.XPATH, self.enter_age_xpath)

    def click_save_btn(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.save_btn_xpath))
        ).click()
        # self.driver.find_element(By.XPATH, self.save_btn_xpath)




