# -*- coding: utf-8 -*-
# Auth ： Hming
# File ：test_fixture_param.py
# Time ： 2020/9/10 11:01
# IDE ：PyCharm

import pytest
test_uesr_data = [{'name':'hming','password':'root1234'},
                  {'name':'gaoyongqiang','password':'root1234'},
                  {'name':'duxincheng','password':'root1234'},]

@pytest.fixture(scope="module")
def login(request):
    # 这个接收传入的参数，接收一个参数
    username = request.param['name']
    password = request.param['password']
    print(f"\n打开首页准备登录，登录用户:{'username'},密码：{'password'}")
    return request.param

# 这是pytest的参数化数据驱动 ， indirect = True 是吧login当作函数去执行
@pytest.mark.parametrize("login",test_uesr_data,indirect=True,ids=["仲浩","高","肚肚"])
def test_login(login):
    # 登录用例
    name = login['name']
    print(f"本次 登陆的：{name}")
    assert name != ""