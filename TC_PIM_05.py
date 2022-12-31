import data_01
import login1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

import time


class orange:
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(time_to_wait=20)

    def login(self):
        self.driver.maximize_window()

        userName = self.driver.find_element(by=By.NAME, value=login1.login.user_name)
        userName.send_keys("Admin")

        pwd = self.driver.find_element(by=By.NAME, value=login1.login.password_name)
        pwd.send_keys("admin123")

        login_btn = self.driver.find_element(by=By.XPATH,value=login1.login.login_class)
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

    def personalDetails(self):

        oth = self.driver.find_element(
            by=By.XPATH,
            value="//a[normalize-space()='Personal Details']").click()
        time.sleep(1)

        otherid = self.driver.find_element(by=By.XPATH,
                                           value=data_01.pim5_personal.otherid)
        otherid.send_keys(data_01.pim5_personal.othSkey)

        Dlisense = self.driver.find_element(
            by=By.XPATH, value=data_01.pim5_personal.Dlisence)
        Dlisense.send_keys(data_01.pim5_personal.DlisenSkey)

        # li_calendar = self.driver.find_element(
        #     by=By.XPATH, value=data_01.pim5_personal.licalbtn).click()
        # time.sleep(2)

        # yearbtn = self.driver.find_element(by=By.XPATH,
        #                                    value=data_01.pim5_personal.yearbtn)
        # yearbtn.click()

        # yeardrp = Select(yearbtn)
        # yeardrp.select_by_visible_text("2021")

        SSN_no = self.driver.find_element(
            by=By.XPATH, value=data_01.pim5_personal.SSNnumber)
        SSN_no.send_keys("8056")

        SIN_no = self.driver.find_element(
            by=By.XPATH, value=data_01.pim5_personal.SINnumber)
        SIN_no.send_keys("8056")

        NATIONdrp_btn = self.driver.find_element(
            by=By.XPATH, value=data_01.pim5_personal.NATdrp_btn)
        NATIONdrp_btn.click()

        for drp in self.driver.find_elements(
                by=By.XPATH, value=data_01.pim5_personal.NATLBOX):
            drptxt = drp.text
            print(drptxt)
            if drptxt == "Indian":
                drp.click()

                break

        marital_sts_btn = self.driver.find_element(
            by=By.XPATH, value=data_01.pim5_personal.martial_status)
        marital_sts_btn.click()

        marital_drp = self.driver.find_elements(
            by=By.XPATH, value=data_01.pim5_personal.marit_sts_list)
        for marital in marital_drp:
            maritaltxt = marital.text
            print(maritaltxt)
            if maritaltxt == "Single":
                marital.click()
                break
            else:
                print("not valied")

        dob_btn = self.driver.find_element(
            by=By.XPATH, value=data_01.pim5_personal.dob_btn).click()

        year_btn = self.driver.find_element(
            by=By.XPATH, value=data_01.pim5_personal.year_btn).click()

        yeardrp_list = self.driver.find_elements(
            by=By.XPATH, value=data_01.pim5_personal.year_list_btn)
        for years in yeardrp_list:
            year = years.text
            if year == "2021":
                years.click()
                break

        date_btn = self.driver.find_elements(
            by=By.XPATH, value=data_01.pim5_personal.dd_btn)
        for datePick in date_btn:
            dates = datePick.text
            if dates == "1":
                datePick.click()
                break
        dateClose_btn = self.driver.find_element(
            by=By.XPATH, value=data_01.pim5_personal.ddclose).click()

        gender_btn = self.driver.find_element(
            by=By.XPATH, value=data_01.pim5_personal.male_btn).click()

        smoker_btn = self.driver.find_element(
            by=By.XPATH, value=data_01.pim5_personal.smoker_btn).click()

        save_btn = self.driver.find_element(
            by=By.LINK_TEXT, value=data_01.pim5_personal.savebtnl).click()

        time.sleep(8)


# o = orange()
# o.login()
# o.pim4()
# o.personalDetails()
