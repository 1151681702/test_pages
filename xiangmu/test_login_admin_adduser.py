# Auth ： Hming
# File ：test_login_admin_adduser.py
# Time ： 2020/9/11 8:49
# IDE ：PyCharm
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.select import Select




class TestHrmLoginAddUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='D:\\Developer\\python projects\\seleniumautotest\\dirveir\\chromedriver.exe')
        cls.driver.get("http://47.112.182.87/orangehrm/symfony/web/index.php/auth/login")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



    def setUp(self):
        self.driver.find_element_by_id("txtUsername").send_keys("root")
        # 把所有的定位封装find——element(顶给方式，定位值)
        self.driver.find_element(By.ID,"txtPassword").send_keys("root1234")
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(2)
        # assert 'Welcome Admin' in self.driver.find_element(By.ID,'welcome').text

    def test_adduser(self):
        menu_admin_viewAdminModule=self.driver.find_element_by_id("menu_admin_viewAdminModule")
        menu_admin_UserManagement=self.driver.find_element_by_id("menu_admin_UserManagement")
        menu_admin_viewSystemUsers=self.driver.find_element_by_id('menu_admin_viewSystemUsers')
        ActionChains(self.driver)\
            .move_to_element(menu_admin_viewAdminModule)\
            .move_to_element(menu_admin_UserManagement)\
            .click(menu_admin_viewSystemUsers).perform()
        assert 'Username' in self.driver.page_source
        self.driver.find_element_by_id("btnAdd").click()
        systemUser_userType = self.driver.find_element_by_id("systemUser_userType")
        Select(systemUser_userType).select_by_value("1")
        # Select(systemUser_userType).select_by_visible_text("管理员")
        # Select(systemUser_userType).select_by_index(0)
        self.driver.find_element_by_id("systemUser_employeeName_empName").send_keys("sa 自行车 sa'd")
        self.driver.find_element_by_id("systemUser_userName").send_keys("sjkdsasqsa2sak ")
        systemUser_status = self.driver.find_element_by_id("systemUser_status")
        Select(systemUser_status).select_by_index(1)
        self.driver.find_element_by_id("systemUser_password").send_keys("root1234")
        self.driver.find_element_by_id("systemUser_confirmPassword").send_keys("root1234")
        time.sleep(2)
        self.driver.find_element_by_id("btnSave").click()
        time.sleep(2)

    # def gun(cls):
    #     cls.driver.find_element_by_xpath("//a[@id='menu_pim_viewPimModule']/b").click()
    #     cls.driver.find_element_by_id("menu_pim_viewEmployeeList").click()  # 点击个人信息管理系统
    #     cls.driver.execute_script("window.scrollBy(0,500)")  # 页面向上滚动
    #     cls.driver.find_element_by_id("ohrmList_chkSelectRecord_8").click()  # 勾选框框



