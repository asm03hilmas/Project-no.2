import data_01
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time


class orange:

    url = 'https://opensource-demo.orangehrmlive.com/'

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    def login(self):

        # get the  input user lodin data
        username = 'Admin'
        password = 'admin123'

        # location of elements data

        user_name = 'username'
        password_name = 'password'
        login_class = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

        self.driver.get(self.url)
        time.sleep(5)
        # find the title of website name
        title = self.driver.title

        print(title)

        self.driver.find_element(By.NAME, value=user_name).send_keys(username)
        self.driver.find_element(
            By.NAME, value=password_name).send_keys(password)
        login = self.driver.find_element(By.XPATH, login_class)
        login.click()
        time.sleep(10)

    def pim3(self):

        pimbtn = self.driver.find_element(By.LINK_TEXT, data_01.pim3.pimbtn)
        pimbtn.click()

        addbtn = self.driver.find_element(
            By.XPATH, data_01.pim3.addbtn).click()

        fname_input = self.driver.find_element(By.XPATH, data_01.pim3.finput)
        fname_input.send_keys(data_01.pim3.finp_skey)

        # mname_input = self.driver.find_element(By.XPATH, data_01.pim3.minput)
        # mname_input.send_keys(data_01.pim3.minp_skey)
        # time.sleep(2)
        # mname_input.clear()

        lname_input = self.driver.find_element(By.XPATH, data_01.pim3.linput)
        lname_input.send_keys(data_01.pim3.linp_skey)

        radiobtn = self.driver.find_element(By.XPATH, data_01.pim3.radiobtn)
        radiobtn.click()

        username_input = self.driver.find_element(
            By.XPATH, data_01.pim3.username_input)
        username_input.send_keys(data_01.pim3.user_skey)

        pwd = self.driver.find_element(By.XPATH, data_01.pim3.pwdinput)
        pwd_text = pwd.send_keys(data_01.pim3.pwd_skey)

        cpwd = self.driver.find_element(By.XPATH, data_01.pim3.cpwdinput)
        cpwd_text = cpwd.send_keys(data_01.pim3.pwd_skey)
        savebtn = self.driver.find_element(By.XPATH, data_01.pim3.savebtn)
        if pwd_text == cpwd_text:
            savebtn.click()
            print("///////////////////////password has been matched////////////////////")
        else:
            print("/////// NOT MATCHED  ///////")

        emplist_name = self.driver.find_element(By.XPATH, data_01.pim3.emplist)
        print(emplist_name.text)


o = orange()
o.login()
o.pim3()
