
import data_01
import login1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
import pytest
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
       

    def contactdetails(self):

        Contact_tab=self.driver.find_element(by=By.XPATH, value=data_01.pim6.contact_btn).click()
        
        Add_btn= self.driver.find_element(by=By.XPATH, value=data_01.pim6.street1)
        Add_btn.send_keys("new street")

        city =self.driver.find_element(by=By.XPATH, value=data_01.pim6.city)
        city.send_keys("Mayilsduthurai")

        state =self.driver.find_element(by=By.XPATH, value=data_01.pim6.state)
        state.send_keys("TamilNadu")

        mobile =self.driver.find_element(by=By.XPATH, value=data_01.pim6.mobile)
        mobile.send_keys("74837284")
        
        pincode =self.driver.find_element(by=By.XPATH, value=data_01.pim6.pincode)
        pincode.send_keys("609001")

        save_btn =self.driver.find_element(by=By.XPATH, value=data_01.pim6.save_btn).click()
        
        
                
        


o = orange()
o.login()
o.pim4()
o.contactdetails()
