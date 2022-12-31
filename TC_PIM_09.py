import data_01
import login1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
import pyautogui
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

    def JobDetail(self):
        JOb_btn= self.driver.find_element( by=By.XPATH, value=data_01.pim9.job_btn)
        JOb_btn.click()

        Jdate_btn= self.driver.find_element( by=By.XPATH, value=data_01.pim9.jDate_btn)
        Jdate_btn.click()
        for Jdate in  self.driver.find_elements( by=By.XPATH, value=data_01.pim9.jDate_drp):
            Jdates=Jdate.text
            if Jdates == "30":
                Jdate.click()
                break

        JTitile_btn=self.driver.find_element( by=By.XPATH, value=data_01.pim9.jTitle_btn)
        JTitile_btn.click()
        for Jtitle in  self.driver.find_elements( by=By.XPATH, value=data_01.pim9.jTitle_drp):
            Jtitls=Jtitle.text
            if Jtitls == "Content Specialist":
                Jtitle.click()
                break
        
    
        Jb_specific=self.driver.find_element( by=By.XPATH, value=data_01.pim9.Jspecfic)
        try:
            Jb_specific.click()
        except:
            print("job specification not enabled")    
        time.sleep(2)
        
        Jb_catabtn=self.driver.find_element( by=By.XPATH, value=data_01.pim9.Jcatago_btn)
        Jb_catabtn.click()
        time.sleep(3)
        for Jcata in  self.driver.find_elements( by=By.XPATH, value=data_01.pim9.Jcata_drp):
            jcatas=Jcata.text
            if jcatas == "Office and Clerical Workers":
                Jcata.click()

        try:

            save_btn =self.driver.find_element( by=By.XPATH, value=data_01.pim9.Save_btn)
            save_btn.click()
        except:
            print("SAVE BUTTON NOT WORK BECAUSE OF DOM HAS  REFRESHED")  

o =orange()
o.login()
o.pim4()
o.JobDetail()

