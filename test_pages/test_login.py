# Auth ： Hming
# File ：test_login.py
# Time ： 2020/9/11 14:40

import unittest
from selenium import webdriver
from pages import base_operate, login_operate
import sys

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='D:\\Developer\\python projects\\seleniumautotest\\dirveir\\chromedriver.exe')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://47.112.182.87/orangehrm/symfony/web/index.php/auth/login")
        # 初始鸡肋页
        cls.base_page = base_operate.BasePage(cls.driver)

    def test_login_correct(self):
        # 初始化登录页，（元素定位操作），按照测试用例书或许编写代码加断言
        login_page = login_operate.LoginPage(self.driver)
        login_page.enter_usename("root")
        login_page.enter_password("root1234")
        login_page.click_login()
        self.base_page.save_picture("2.png")
        # assert 'Welcome Admin' in login_page.login_sucess_result()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


