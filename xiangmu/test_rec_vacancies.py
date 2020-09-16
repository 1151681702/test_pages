# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path='D:\Developer\python projects\seleniumautotest\dirveir\chromedriver.exe')
        cls.driver.implicitly_wait(30)
        # 2.输入要测试地址登录页
        cls.base_url = "http://47.112.182.87"
        cls.verificationErrors = []
        cls.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.maximize_window()  # 网页变大
        driver.get("http://47.112.182.87/orangehrm/symfony/web/index.php/auth/login")  # 进入登录页
        # driver.find_element_by_xpath("//div[@id='divUsername']/span").click()
        driver.find_element_by_id("txtUsername").clear()# 清空用户名
        driver.find_element_by_id("txtUsername").send_keys("root")# 输入用户名
        driver.find_element_by_id("txtPassword").clear()# 清空密码
        driver.find_element_by_id("txtPassword").send_keys("root1234")# 输入密码
        driver.find_element_by_id("btnLogin").click()# 提交
        driver.find_element_by_xpath("//a[@id='menu_recruitment_viewRecruitmentModule']/b").click()
        driver.find_element_by_id("menu_recruitment_viewJobVacancy").click()# 点击recruitment_Vacancy"

        driver.find_element_by_id("btnAdd").click()                                                     # 点击添加按钮
        driver.find_element_by_id("addJobVacancy_jobTitle").click()                                     # 点击第一个下拉框
        Select(driver.find_element_by_id("addJobVacancy_jobTitle")).select_by_visible_text(u"测试工程师")# 输入Job Title
        driver.find_element_by_id("addJobVacancy_jobTitle").click()
        driver.find_element_by_id("addJobVacancy_name").click()                                         # 元素查找，找到元素后进行点击
        driver.find_element_by_id("addJobVacancy_name").clear()                                         # 清空Vacancy Name
        driver.find_element_by_id("addJobVacancy_name").send_keys(u"测试工程师1")                         # 输入Vacancy Name
        driver.find_element_by_id("addJobVacancy_hiringManager").click()                                # 元素查找，找到元素后进行点击
        driver.find_element_by_id("addJobVacancy_hiringManager").clear()                                # 清空Hiring Manager
        driver.find_element_by_id("addJobVacancy_hiringManager").send_keys(u"仲")                       # 输入Hiring Manager
        driver.find_element_by_xpath("//div[4]/ul/li").click()                                          # 定位
        driver.find_element_by_id("addJobVacancy_noOfPositions").click()                                # 元素查找，找到元素后进行点击
        driver.find_element_by_id("addJobVacancy_noOfPositions").clear()                                # 清空Number of Positions
        driver.find_element_by_id("addJobVacancy_noOfPositions").send_keys("5")                         # 输入Number of Positions
        driver.find_element_by_id("addJobVacancy_description").click()                                  # 元素查找，找到元素后进行点击
        driver.find_element_by_id("addJobVacancy_description").clear()                                  # 清空Description
        driver.find_element_by_id("addJobVacancy_description").send_keys(u"无")                         # 输入Description
        driver.find_element_by_id("btnSave").click()                                                    # 提交

    def tearDown(self):# 执行后关闭网页
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
