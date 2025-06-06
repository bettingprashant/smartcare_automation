import allure
from selenium import webdriver
import time
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Book_Appointment:
    def __init__(self,driver):
        self.driver = driver

    select_role_xpath = "//*[@class ='role-manage-list-card doctor-color']"
    doctor_consultation_btn_xpath = "//div[@class='col-lg-51 p-0 desk-show']//li[3]//a[1]//div[1]//span[1]//img[1]"
    slot_time_xpath = "//div[normalize-space()='7:00 - 7:30']"
    patient_search_xpath = "//*[@placeholder='Search patient']"
    select_patient_xpath = "//body[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/ul[1]/li[1]/span[1]"
    book_now_btn_xpath = "//span[contains(text(),'Book Now')]"
    payment_mode_css = "button:nth-child(2) span:nth-child(2) span:nth-child(1) span:nth-child(1)" # "//span[contains(text(),'Confirm')]"
    receive_payment_xpath = "//span[contains(text(),'Receive Payment')]"
    start_consultation_xpath = "//span[contains(text(),'Start consultation')]"

    select_medicine_btn_xpath = "//p[normalize-space()='Medicine']"
    choose_medicine_xpath = "//input[@placeholder='Choose medicine']"
    select_medicine_dropdown_xpath = "//div[@class='q-page-container']//li[1]"
    medicine_dosage_xpath = "//div[@class='w-100 text-capitalize d-flex justify-between dosage pz-form-input']//input[@class='pz-list-text']"
    select_dosage_xpath = "//body[1]/div[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]/div[9]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]"
    select_ngt_xpath = "//span[1]//div[1]//div[1]//div[1]//div[1]//div[17]//div[1]//div[1]//div[1]//div[1]//*[name()='svg']"
    medicine_days_xpath = "//span[1]//div[1]//div[1]//div[1]//div[1]//div[19]//div[1]//input[1]"
    sign_btn_xpath = "//p[@class='bg-blueclr w-color br_half fontsize13 px-3 py-1 cursor-pointer']"



    def select_role(self):
        WebDriverWait(self.driver,40).until(
            EC.element_to_be_clickable((By.XPATH, self.select_role_xpath))
        ).click()
        time.sleep(20)

    def doctor_consultation_btn(self):
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, self.doctor_consultation_btn_xpath))
        ).click()

    def slot_time(self):
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, self.slot_time_xpath))
        ).click()

    def patient_search(self,name):
        patient_search = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, self.patient_search_xpath))
        )
        patient_search.click()
        patient_search.send_keys(name)

    def select_patient(self):
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, self.select_patient_xpath))
        ).click()

    def book_now_btn(self):
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, self.book_now_btn_xpath))
        ).click()
        time.sleep(10)

    def payment_mode(self):
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.payment_mode_css))
        ).click()
        time.sleep(20)

    def receive_payment(self):
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, self.receive_payment_xpath))
        ).click()
        time.sleep(5)
    def start_consultation(self):
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, self.start_consultation_xpath))
        ).click()
        time.sleep(5)

    def select_medicine_btn(self):
        WebDriverWait(self.driver,40).until(
            EC.element_to_be_clickable((By.XPATH, self.select_medicine_btn_xpath))
        ).click()

    def choose_medicine(self,medicine):
        choose_med = WebDriverWait(self.driver,40).until(
            EC.element_to_be_clickable((By.XPATH, self.choose_medicine_xpath))
        )
        choose_med.click()
        choose_med.send_keys(medicine)

    def select_medicine_dropdown(self):
        WebDriverWait(self.driver,40).until(
            EC.element_to_be_clickable((By.XPATH, self.select_medicine_dropdown_xpath))
        ).click()

    def medicine_dosage(self):
        WebDriverWait(self.driver,40).until(
            EC.element_to_be_clickable((By.XPATH,self.medicine_dosage_xpath))
        ).click()

    def select_dosage(self):
        WebDriverWait(self.driver,40).until(
            EC.element_to_be_clickable((By.XPATH,self.select_dosage_xpath))
        ).click()

    def select_ngt(self):
        WebDriverWait(self.driver,40).until(
            EC.element_to_be_clickable((By.XPATH, self.select_ngt_xpath))
        ).click()

    def medicine_days(self,days):
        med_days = WebDriverWait(self.driver,40).until(
            EC.element_to_be_clickable((By.XPATH,self.medicine_days_xpath))
        )
        med_days.click()
        med_days.send_keys(days)

    def sign_btn(self):
        WebDriverWait(self.driver,40).until(
            EC.element_to_be_clickable((By.XPATH,self.sign_btn_xpath))
        ).click()
        time.sleep(5)