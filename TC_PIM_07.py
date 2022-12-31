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

    def EmerContact(self):
        Emer_btn =self.driver.find_element(By.XPATH, data_01.pim7.EMERcontact).click()

        Add_btn = self.driver.find_element(By.XPATH, data_01.pim7.add_btn).click()

        Name =self.driver.find_element(By.XPATH, data_01.pim7.name)
        Name.send_keys("mom")

        Relationship=self.driver.find_element(By.XPATH, data_01.pim7.relation)
        Relationship.send_keys("mother")

        mobileNo= self.driver.find_element(By.XPATH, data_01.pim7.mobile).send_keys("224242")

        WorkNo =self.driver.find_element(By.XPATH, data_01.pim7.wrkmobile).send_keys('374687')

        HomeNo= self.driver.find_element(By.XPATH, data_01.pim7.homeno).send_keys("34343")

        Save_btn=self.driver.find_element(By.XPATH, data_01.pim7.save_btn).click()

        time.sleep(2)


                



o = orange()    
o.login()
o.pim4()
o.EmerContact()

