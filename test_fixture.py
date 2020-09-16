
'''
三个模块：查询不需要登录，购物车，支付，是登陆
登录时前提不是测试，seteup():写登录，必须所有模块都登陆
1.在需要方法的上面加上：@pytest.fixture()
2。在形参

login是登录，添加到购物车和支付前，是他们的依赖，方法fixture（）
'''
import pytest

@pytest.fixture()
def login():
    print("使用admin/root1234已经登录")

def test_search():
    print("搜索物品")


def test_cart(login):
    print("添加商品到购物车")


def test_pay(login):
    print("支付商品的订单")