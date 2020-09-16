# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:\Developer\python projects\seleniumautotest\dirveir\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "http://47.112.182.87"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://47.112.182.87/orangehrm/symfony/web/index.php/auth/login")
        driver.find_element_by_xpath("//div[@id='divUsername']/span").click()
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("root")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("root1234")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_xpath("//a[@id='menu_admin_viewAdminModule']/b").click()
        driver.find_element_by_id("menu_admin_Job").click()
        driver.find_element_by_id("menu_admin_viewJobTitleList").click()
        driver.find_element_by_id("btnAdd").click()
        driver.find_element_by_id("jobTitle_jobTitle").click()
        driver.find_element_by_id("jobTitle_jobTitle").clear()
        driver.find_element_by_id("jobTitle_jobTitle").send_keys(u"测试结果2")
        driver.find_element_by_id("btnSave").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
