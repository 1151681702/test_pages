# Auth ： Hming
# File ：base_operate.py
# Time ： 2020/9/11 13:40
# 鸡肋界面

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    def save_picture(self,file_path):
        self.driver.save_screenshot(file_path)

