# 小橘子登录
import time
from selenium import webdriver
# # 1.打开浏览器
# driver = webdriver.Chrome("D:\Developer\python projects\seleniumautotest\dirveir\chromedriver.exe")
# # 2.输入要测试的地址
# driver.get("http://47.112.182.87/orangehrm/symfony/web/index.php/auth/login")
# # 3.输入用户名，密码，找到用户名所有文本框，定位id ， name ，xpath ， css ，
# driver.find_element_by_id("txtUsername").send_keys("root")
# driver.find_element_by_id("txtPassword").send_keys("root1234")
# # 4.点击登录
# driver.find_element_by_id("btnLogin").click()
# time.sleep(2)
# # 5.定位admin 断言
# assert  "欢迎Admin" == driver.find_element_by_id("welcome").text
# # 6.关闭浏览器
# driver.close()


# 1、打开浏览器
driver = webdriver.Chrome("D:\Developer\python projects\seleniumautotest\dirveir\chromedriver.exe")
# 2、打开必应
driver.get("https://cn.bing.com/")
# 输入搜索关键字
driver.find_element_by_id("sb_form_q").send_keys("Python")
# 4、点击搜索
driver.find_element_by_id("sb_form_go").click()
time.sleep(2)
# 5、定位到断言
assert 'python' in driver.page_source


time.sleep(2)
# 6、关闭浏览器
driver.close()