

from data_01 import *
from selenium import webdriver
from selenium.webdriver.common.by import By

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

    def search_box(self):

        search_title = self.driver.find_element(
            By.XPATH, value=data_01.menu.search_menu)
        search_title.click()
        # ad_vari = search_title.send_keys(data_01.key_data.search_admin)
        l_data = data_01.key_data.list
        lists = self.driver.find_elements(By.XPATH, data_01.menu.list_menu)
        for loc_list in l_data:
            search_title.send_keys(loc_list)

            for list in lists:

                if list.text == loc_list:
                    search_title.clear()
                    print('user data is :' + loc_list,
                          'web data is : ', print(list.text))
                    self.driver.close()


o = orange()
o.login()
o.search_box()
