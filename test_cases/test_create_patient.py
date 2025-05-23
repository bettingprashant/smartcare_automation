
from base_pages.Login_Smartcare import Login_Doctor_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.Create_Patient import Create_Patient


class Test_02_Create_New_Patient:
    login_page_url = Read_Config.get_login_page_url()
    email = Read_Config.get_email()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    def test_add_new_patient(self,setup):
        self.logger.info("******************Test_02_Create_New_Patient_Started*********************")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.login_page_url)

        self.doctor_lp = Login_Doctor_Page(self.driver)
        self.doctor_lp.enter_email(self.email)
        self.doctor_lp.enter_password(self.password)
        self.doctor_lp.click_login()
        self.driver.maximize_window()

        self.logger.info("***********Login completed *************")

        self.logger.info("***********starting add customer test *************")

        self.add_patient = Create_Patient(self.driver)
        self.add_patient.select_role()
        self.add_patient.patient_list()
        self.add_patient.add_new_patient()
        self.add_patient.patient_name("Prashant")
        self.add_patient.select_gender()
        self.add_patient.select_male()
        self.add_patient.enter_age("26")
        self.add_patient.click_save_btn()

        self.driver.close()



