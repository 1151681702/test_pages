from selenium import webdriver
import unittest, time
from ddt import ddt , file_data
from HTMLTestRunner import HTMLTestRunner
@ddt
class HRMjobtitle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 打开浏览器
        cls.driver = webdriver.Chrome(executable_path='D:\Developer\python projects\seleniumautotest\dirveir\chromedriver.exe')
        cls.driver.implicitly_wait(30)
        # 2.输入要测试地址登录页
        cls.base_url = "http://47.112.182.87"
        cls.verificationErrors = []
        cls.accept_next_alert = True
#
    def test_1login(self):
        driver = self.driver
        driver.maximize_window()  # 网页变大
        driver.get("http://47.112.182.87/orangehrm/symfony/web/index.php/auth/login")  # 进入登录页
        # driver.find_element_by_xpath("//div[@id='divUsername']/span").click()
        driver.find_element_by_id("txtUsername").click()
        driver.find_element_by_xpath('//*[@id="txtUsername"]').clear()
        driver.find_element_by_id("txtUsername").send_keys("root")  # 输入用户名
        driver.find_element_by_id("txtPassword").clear()  # 清空密码
        driver.find_element_by_id("txtPassword").send_keys("root1234")  # 输入密码
        driver.find_element_by_id("btnLogin").click()  # 提交
        time.sleep(2)
        driver.find_element_by_xpath("//a[@id='menu_admin_viewAdminModule']/b").click()
        driver.find_element_by_id("menu_admin_Job").click()                   # 点击管理员job
        driver.find_element_by_id("menu_admin_viewJobTitleList").click()      # 点击JobTitl

    @file_data("login.yaml")
    def test_2hrm_method(self, job):
        print(job)
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()                           # 点击添加
        driver.find_element_by_id("jobTitle_jobTitle").click()                # 点击jobtitle输入框
        driver.find_element_by_id("jobTitle_jobTitle").clear()                # 清空输入框
        driver.find_element_by_id("jobTitle_jobTitle").send_keys(job)         # 填写
        driver.find_element_by_id("btnSave").click()                          # 提交
       # assert jobtitle in driver.page_source

        filename = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))     # 截图以随时间命名
        driver.save_screenshot(str(filename) + ".png")                        #截图完成页

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    # unittest.main()
    # 添加报告
    # TestSuite套件，
    suite = unittest.TestSuite()
    # 通过类名把要测试类及类中方法加载到套件中
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(HRMjobtitle))
    # 执行用例--执行结果保存到html格式报告。
    with open("report.html", 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title="测试报告",
            description="UI测试"
        )
        runner.run(suite)
