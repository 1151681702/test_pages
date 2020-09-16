import sys

import pytest

class TestCalss():
    # def setup_class(self):
    #     print("在类的开始时执行一 次")
    #
    # def teardown_module(self):
    #     print("这是一个文件在结束时执行一次，不是按照现在方法所有位置顺序执行的")
    #
    # def teardown_class(self):
    #     print("在类的结束时执行一次")
    #
    # def setup_method(self):
    #     print("在有类的每 个方法 前执行一次，有几个方法就执行几次 ")
    #
    # def teardown_method(self):
    #     print("在有类的每个方法后执行一次，有几个方法就执行几次 ")
    #
    # @ pytest.mark.xfail# 跳过
    # def test_method_01(self):
    #     print("这 是类中的方法01")
    #     assert 3 == 2 + 1
    #     assert 3 > 2 == True
    #     assert 'linda' in 'lindafang'
    #     assert [1] ==['1']
    #
    # @pytest.mark.skip  # 跳过
    # def test_method_02(self):
    #     print("这 是类中的方法02")
    #     assert {'name': 'linda', 'age': 18} == {'name': 'linda', 'age': 38}


    # environment = 'android'
    # @pytest.mark.skipif(environment = 'android',reason='android平台没有')
    # def test_cart(self):
    #     print('这是mac-apple的环境所有不执行')

    @pytest.mark.skipif(sys.platform == 'win32',reason='不在win下运行')
    @pytest.mark.skipif(sys.version_info== (3,7), reason='3.9版本下不执行')
    def test_cart_01(self):
        print('如果py3.9以下不执行，win平台不执行，我这就执行')

    # @pytest.mark.skipif(reason="我不想执行了")
    # def test_method_03(self):
    #     print("这 是类中的方法03")
    #     assert '*' * 10 == '*' * 5

if __name__== '__main__':
    pytest.main()





