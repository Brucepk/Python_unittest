import unittest
from selenium import webdriver
from time import sleep
import HTMLTestRunner


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://baidu.com')
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.find_element_by_id('kw').clear()

    def test1(self):
        self.driver.find_element_by_id('kw').send_keys('Python')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.assertIn('百度为您找到相关结果约', self.driver.page_source, '验证失败')

    def test2(self):
        self.driver.find_element_by_id('kw').send_keys('Go')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.assertIn('百度为您找到相关结果约', self.driver.page_source, '验证失败')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    test_suite = unittest.TestSuite()  # 创建一个测试集合
    test_suite.addTest(MyTest('test1'))  # 测试套件中添加测试用例
    test_suite.addTest(MyTest('test2'))  # 测试套件中添加测试用例
    fp = open('pk.html', 'wb')  # 打开一个保存结果的html文件
    # 生成执行用例的对象
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='pk哥测试报告', description='Python知识圈制作')
    runner.run(test_suite)   # 执行测试套件


















