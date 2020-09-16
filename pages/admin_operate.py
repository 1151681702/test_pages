# Auth ： Hming
# File ：admin_operate.py
# Time ： 2020/9/11 15:57
# 添加操作
from selenium.webdriver.support.wait import WebDriverWait
from pages.Locators import LoginPageLocators,WelcomePageLocators
from pages.base_operate import BasePage

class LoginPage(BasePage):
    # 输入用户名  密码  点击登录
    def enter_usename(self,username):
        # 加个等待点击用户名清楚输入
        WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*LoginPageLocators.txtUsername))
        usernameele = self.driver.find_element(*LoginPageLocators.txtUsername)
        usernameele.click()
        usernameele.clear()
        usernameele.send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*LoginPageLocators.txtPassword))
        usernameele = self.driver.find_element(*LoginPageLocators.txtPassword)
        usernameele.click()
        usernameele.clear()
        usernameele.send_keys(password)

    def click_login(self):
        clickele = self.driver.find_element(*LoginPageLocators.btnLogin)
        clickele.click()

    def login_sucess_result(self):
        WebDriverWait(self.driver,10)\
            .until(lambda driver:driver.find_element(*WelcomePageLocators.welcome))
        return self.driver.find_element(WelcomePageLocators.welcome).text









