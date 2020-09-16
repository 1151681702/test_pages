
'''
 ui自动化

login是登录，添加到购物车和支付前，是他们的依赖，方法fixture（）
'''
import pytest


def test_search():
    print("admin")

@pytest.mark.usefixtures("login")
def test_cart():
    print("job")

@pytest.mark.usefixtures("login")
def test_pay():
    print("pim")