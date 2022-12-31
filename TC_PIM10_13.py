import data_01
import login1
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class orange:
    driver = webdriver.Firefox()
    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(time_to_wait=20)
    
    def login(self):
        self.driver.maximize_window()

        userName = self.driver.find_element(by=By.NAME,value=login1.login.user_name)
        userName.send_keys("Admin")

        pwd = self.driver.find_element(by=By.NAME,value=login1.login.password_name)
        pwd.send_keys("admin123")

        login_btn = self.driver.find_element(by=By.XPATH, value=login1.login.login_class)
        login_btn.click()
        time.sleep(3)


    def pim4(self):

        pimbtn = self.driver.find_element(by=By.LINK_TEXT,value=data_01.pim4.pimbtn).click()
        time.sleep(8)

        empdrp_id = self.driver.find_element(by=By.XPATH,value=data_01.pim4.emp_name)
        empdrp_id.click()
        time.sleep(2)
        skey = empdrp_id.send_keys("324324")
        
        savebtn = self.driver.find_element(by=By.XPATH,value=data_01.pim4.SAVE).click()

        edit_btn = self.driver.find_element( by=By.XPATH, value=data_01.pim4.editbtn).click()
        time.sleep(3)

    def jobdetails(self):
        JOb_btn= self.driver.find_element( by=By.XPATH, value=data_01.pim1011.job_btn)
        JOb_btn.click()
        
        emp_act_btn=self.driver.find_element( by=By.XPATH, value=data_01.pim1011.Emp_termi_btn)
        emp_act_btn.click()
        time.sleep(1)

        Termi_btn=self.driver.find_element( by=By.XPATH, value=data_01.pim1011.Ter_btn)
        Termi_btn.click()

        Termi_drp=self.driver.find_elements( by=By.XPATH, value=data_01.pim1011.ter_drp)
        for Terminate in Termi_drp:
            Termidatetxt =Terminate.text
            if Termidatetxt == "29":
                Terminate.click()
                break


        Termi_Reson=self.driver.find_element( by=By.XPATH, value=data_01.pim1011.Ter_res_btn)
        Termi_Reson.click()

        Termi_res_drp=self.driver.find_elements( by=By.XPATH, value=data_01.pim1011.Ter_res_drp)
        for Terminate in Termi_res_drp:
            Termidatetxt =Terminate.text
            if Termidatetxt == "Other":
                Terminate.click()
                break

        save =self.driver.find_element( by=By.XPATH, value=data_01.pim1011.save)
        save.click()
        time.sleep(2)
        Termi_act_btn =self.driver.find_element( by=By.XPATH, value=data_01.pim1011.act_emp)
        print(Termi_act_btn.text)
        dateverified =self.driver.find_element( by=By.XPATH, value=data_01.pim1011.act_date)
        print(dateverified)


    def active_terminate(self):
        Termi_act_btn =self.driver.find_element( by=By.XPATH, value=data_01.pim1011.act_emp)
        Termi_act_btn.click()      


o= orange()
o.login()
o.pim4()
o.jobdetails()
o.active_terminate()
