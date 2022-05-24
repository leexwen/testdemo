import HTMLTestRunner
import time
import unittest
import os

# dirpath是存放测试用例的文件路径
from common.SendEmail import SendEmail

def get_test_cases(dirpath):
    # 测试用例均使用 "test_"开头命名
    test_cases = unittest.TestSuite()
    suites = unittest.defaultTestLoader.discover(dirpath, 'test_*.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTest(suite)
    return test_cases


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    testpath=base_dir+'\\testcase'
    #print('testpath:',testpath)
    cases = get_test_cases(testpath)
    # 报告生成时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 测试报告存放位置
    test_reports_address ="./report/"
    print('test_reports_address:',test_reports_address)
    # 设置报告文件名
    filename = test_reports_address+now + 'report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'Web自动化测试', description=u'详细测试结果如下:')
    runner.run(cases)
    time.sleep(6)
    # 查找最新生成的测试报告地址
    new_report_address = SendEmail().acquire_report_address(test_reports_address)
    # 自动发送邮件
    SendEmail().send_email(new_report_address)