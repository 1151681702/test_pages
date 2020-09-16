import pytest

# # 通过fixture自带的参数进行数据驱动，形参名字必须是request
# @pytest.fixture(params=[1,2,3,'hming'])
# def data_param(request):
#     return request.param
#
# # 测试方法需要一些数据通过装饰器的方式加载
# def test_fixture_param(data_param):
#     print(data_param)

# ----------------------------------------------------------------------------------------------------------------------

# @ pytest.mark.parametrize("num12,result",[('1,2',3),
#                                           ('3+12',15),
#                                           ('6*2',12),
#                                           ('3/1',3),
#                           ])
# def test_coculator(num12,result):
#     assert eval(num12)  == result

# ----------------------------------------------------------------------------------------------------------------------

@ pytest.mark.parametrize("num1,num2,result",[[1,2,3],
                                          [3,12,15],
                                          [11.8,2,3.8],
                                          [6,-2,4],
                                          ],ids=["10以内","10以外","复数","小数"])
def dest_coculator2(num1,num2,result):
    assert num1+num2 == result

# ----------------------------------------------------------------------------------------------------------------------