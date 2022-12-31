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

    def Dependents(self):
        btn= self.driver.find_element(by=By.XPATH,value=data_01.pim8.dependents_btn).click()

        Add_btn=self.driver.find_element(by=By.XPATH,value=data_01.pim8.Add_btn).click()

        Name = self.driver.find_element(by=By.XPATH,value=data_01.pim8.Name)
        Name.send_keys("unknown")

        relation_btn=self.driver.find_element(by=By.XPATH,value=data_01.pim8.relation_btn).click()
        for relation in self.driver.find_elements(by=By.XPATH,value=data_01.pim8.relation_drp):
            relatiotxt=relation.text
            if relatiotxt == "Child":
                relation.click()
                break

        Dob_btn=self.driver.find_element(by=By.XPATH,value=data_01.pim8.Dob_btn).click()
        for date in self.driver.find_elements(by=By.XPATH,value=data_01.pim8.Dob_drp):
            datetxt=date.text
            if datetxt == "30":
                date.click()
                break        

        save_btn= self.driver.find_element(by=By.XPATH,value=data_01.pim8.save_btn).click()
        self.driver.quit()
        
o = orange()
o.login()
o.pim4()
o.Dependents()
