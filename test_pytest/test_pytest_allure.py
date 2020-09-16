# -*- coding: utf-8 -*-
# Auth ： Hming
# File ：test_pytest_allure.py
# Time ： 2020/9/10 14:26
# IDE ：PyCharm
import pytest
import  allure

# 单元自动化测试脚本
@allure.feature("这个是加法计算器，加数{0}与加数{1}相加功能")
def add_caculator(num1,num2):
    sum = num1 + num2
    return sum


@allure.description("这是假发计算器，测试加法有效各种情况，结果是否正确")
@allure.severity("critical")
@allure.story("正确的测试用例")
@allure.issue('www.baidu.com',"曾经的bug")
@allure.feature("www.baidu.com","加法的计算器测试")
@ pytest.mark.parametrize("num1,num2,result",[[1,2,3],
                                          [3,12,15],
                                          [11.8,2,13.8],
                                          [6,-2,4],
                                          ],ids=["10以内","10以外","复数","小数"])

def test_add_caculator_error(num1,num2,result):
    with allure.step("第一步：调用加法的方法"):
        sum = add_caculator(num1,num2)
    with allure.step("第二部：断言加法运算结果与预期是否一致"):
        assert  sum == result

@allure.description("这是假发计算器，测试加法无效各种情况，结果是否正确")
@allure.severity("normal")
@allure.story("无效的的测试用例")
@allure.feature("www.baidu.com","这是加法测试用例")
@ pytest.mark.parametrize("num1,num2,result",[[1,'2',3],
                                          [3,' ',15],
                                          ['>?<#',2,13.8],
                                          [6,-2,5],
                                          ],ids=["字符串","空格","符号","数字"])

def test_add_caculator(num1,num2,result):
    with allure.step("如果错误截图"):
        allure.attach.file("B9U0DQ{]Z3SNC_$FHE4H1[S.png",
                           attachment_type=allure.attachment_type.PNG)
    with allure.step("html网页的漂亮"):
        allure.attach("<html><body>这是我们要测试的加法<script type='text/javascript'>alert('这是一个惊喜');</script></body></html>",
                      "这是个网页", allure.attachment_type.HTML)
    with allure.step("执行了"):
        sum=add_caculator(num1,num2)
        allure.attach("加数1+加数2=", f"{0}+{1}={2}")
        assert sum ==result