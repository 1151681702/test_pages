# import pytest
#
# @pytest.fixture(scope = "module",autouse=True)
# # @pytest.fixture()
# def open_browser():
#     print("打开浏览器,登录")
#     yield
#     print("关闭浏览器")
#
# @pytest.fixture()
# def login():
#     print("登录")
#
# @pytest.fixture()
# def jiaren():
#     print("加人")



# import pytest
# class TestHrm():
#
#     @pytest.mark.usefixtures("addpeople")
#     @pytest.mark.usefixtures("login")
#     def test_kongque(self):
#         print("添加空缺")