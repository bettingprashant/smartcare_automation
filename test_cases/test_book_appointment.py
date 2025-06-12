
from base_pages.Login_Smartcare import Login_Doctor_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.Book_Appointment import Book_Appointment

class Test_03_book_appointment:
    login_page_url = Read_Config.get_login_page_url()
    email = Read_Config.get_email()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    def test_book_appointment(self, setup):
        self.logger.info("******************Test_03_Appointment_Booking_Started*********************")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.login_page_url)

        self.doctor_lp = Login_Doctor_Page(self.driver)
        self.doctor_lp.enter_email(self.email)
        self.doctor_lp.enter_password(self.password)
        self.doctor_lp.click_login()
        self.driver.maximize_window()

        self.logger.info("***********Login completed *************")

        self.logger.info("***********Starting Appointment Booking*************")

        self.book_appmt = Book_Appointment(self.driver)
        self.book_appmt.select_role()
        self.book_appmt.doctor_consultation_btn()
        self.book_appmt.start_shift_btn()
        self.book_appmt.slot_time()
        self.book_appmt.patient_search("Prashant")
        self.book_appmt.select_patient()
        self.book_appmt.book_now_btn()
        self.book_appmt.payment_mode()
        self.book_appmt.receive_payment()
        self.book_appmt.start_consultation()
        self.book_appmt.select_medicine_btn()
        self.book_appmt.choose_medicine("dolo 650mg")
        self.book_appmt.select_medicine_dropdown()
        self.book_appmt.medicine_dosage()
        self.book_appmt.select_dosage()
        self.book_appmt.select_ngt()
        self.book_appmt.medicine_days("3")
        self.book_appmt.sign_btn()




        self.driver.close()

