# -*- coding: utf-8 -*-
import pytest
from _pytest import unittest
from selenium import webdriver
import time
import allure

#
# class TestBaidu(object):
#
#     @allure.feature('打开百度')
#     @pytest.fixture(scope='module', autouse=True)
#     def start(self):
#         with allure.step('step one:打开浏览器输入百度网址'):
#             driver = webdriver.Chrome("D:\pythondor\HRM\dirver\chromedriver.exe")
#             driver.get('http://www.baidu.com')
#             time.sleep(1)
#     #     yield
#     #
#     # def tearDownClass(cls):
#     #     cls.driver.quit()
#
#     # @allure.feature('百度搜索功能')
#     @allure.story('搜索验证-字母')
#     # @pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
#     def test_soso(self, driver, test_data1):
#         with allure.step("step two：在搜索栏输入{0},并点击百度一下".format(test_data1)):
#             driver.find_element_by_id('kw').send_keys("ke")
#             driver.find_element_by_id('su').click()
#             time.sleep(3)
#             print(driver.title)
#             assert test_data1 in driver.title
#         with allure.step('截图保存到项目中'):
#             driver.save_screenshot("./result/b.png")
#             allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)

    # @allure.feature('百度new功能')
    # @allure.story('搜索打开新闻页')
    # def test_news(self, driver):
    #     with allure.step('step three：点击新闻，验证是否跳转'):
    #         driver.find_element_by_link_text('新闻').click()
    #         print(driver.title)
    #         assert '新闻' in driver.title
    #
    #     with allure.step('截图验证'):
    #         driver.save_screenshot("./result/c.png")
    #         allure.attach.file("./result/c.png", attachment_type=allure.attachment_type.PNG)

@allure.testcase("https:/ /www. baidu. com的搜索功能")
# @pytest.mark.parametrize('test_data1',['allure','pytest','unittest'])
def test_steps_demo():
    with allure.step('step one:打开浏览器输入百度网址'):
        driver = webdriver.Chrome(executable_path='D:\pythondor\HRM\dirver\chromedriver.exe')
    with allure.step("打开百度"):
        driver.get('https://www.baidu.com')
    with allure.step('step two: 在搜索栏输入allure,并点击百度一下'):
        driver.find_element_by_id('kw').send_keys("可乐")
        time. sleep(2)
        driver. find_element_by_id('su').click()
        time. sleep(5)
    with allure. step('step three: 截图保存到项目中'):
        driver.save_screenshot("./result/b.png")
        # f= open(' ./ result/b.png', 'rb'). read( )
        allure. attach. file("./result/b.png", attachment_type=allure.attachment_type.PNG)
        # allure. attach( '<head></head><body>首页</body>','Attach with HTML type',
        #                 allure. attachment_type.HTML)
    with allure.step('step four:关闭浏览器，退出'):
        driver.quit()