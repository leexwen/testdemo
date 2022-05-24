import time
import unittest
from selenium import webdriver
from page.searchPage import SearchPage


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = SearchPage.url
        self.driver.maximize_window()
        self.page = SearchPage(self.driver)
        self.page.get(self.url)

    def tearDown(self):
        self.driver.close()

    def test_search_01(self):
        # 错误的断言导致测试用例failed
        self.page.search = self.page.search_content
        self.page.search_btn.click()
        time.sleep(2)
        self.assertIn(self.page.search_content_assert, self.driver.page_source)

    def test_search_02(self):
        # 元素值错误导致的自动化测试用例error
        self.page.search = self.page.search_content
        self.page.search_btn.click()
        time.sleep(2)
        self.assertIn(self.page.search_content_assert, self.driver.page_source)


if __name__ == '__main__':
    unittest.main()