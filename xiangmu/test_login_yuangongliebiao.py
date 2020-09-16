# -*- coding: utf-8 -*-
# Auth ： Hming
# File ：test_login_yuangongliebiao.py
# Time ： 2020/9/11 11:08
# IDE ：PyCharm

from selenium import webdriver
import unittest, time
from ddt import ddt , file_data

@ddt
class HRMjobtitle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 打开浏览器
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
        driver.find_element_by_id("txtUsername").click()
        driver.find_element_by_xpath('//*[@id="txtUsername"]').clear()
        driver.find_element_by_id("txtUsername").send_keys("root")  # 输入用户名
        driver.find_element_by_id("txtPassword").clear()  # 清空密码
        driver.find_element_by_id("txtPassword").send_keys("root1234")  # 输入密码
        driver.find_element_by_id("btnLogin").click()  # 提交
        time.sleep(2)
        driver.find_element_by_xpath("//a[@id='menu_pim_viewPimModule']/b").click()
        driver.find_element_by_id("menu_pim_viewEmployeeList").click()# 点击个人信息管理系统


        self.driver.execute_script("window.scrollBy(0,500)")  # 页面向上滚动
        time.sleep(2)
        ohrmList_chkSelectRecord = self.driver.find_elements_by_name(("chkSelectRow[]"))
        ohrmList_chkSelectRecord[-1].click()
        self.driver.save_screenshot('1.png')
        time.sleep(2)

        # driver.find_element_by_id("ohrmList_chkSelectRecord_8").click() # 勾选框框



if __name__ == "__main__":
    unittest.main()
