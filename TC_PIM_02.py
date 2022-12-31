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

    def dropdown(self):

        admin_btn = self.driver.find_element(
            By.LINK_TEXT, value=data_01.adminbtn2.admin_btn)
        admin_btn.click()

        self.driver.find_element(
            By.XPATH, value=data_01.adminbtn2.usermgn_bt).click()
        self.driver.find_element(
            By.XPATH, value=data_01.adminbtn2.user_drp).click()
        user = self.driver.find_element(
            By.XPATH, value=data_01.adminbtn2.user_role).click()
        admintext = self.driver.find_element(
            By.XPATH, value=data_01.adminbtn2.admindrp).text
        esstext = self.driver.find_element(
            By.XPATH, value=data_01.adminbtn2.essdrp).text

        statusdrp = self.driver.find_element(
            By.XPATH, data_01.adminbtn2.status_role).click()
        enabledrp = self.driver.find_element(
            By.XPATH, data_01.adminbtn2.enabled).text
        disabledrp = self.driver.find_element(
            By.XPATH, data_01.adminbtn2.disbled).text
        print(admintext)
        print(esstext)
        print(enabledrp)
        print(disabledrp)

        # act = ActionChains(self.driver)
        # btn = act.move_to_element(admintext)
        # btn.perform()


o = orange()
o.login()
o.dropdown()
