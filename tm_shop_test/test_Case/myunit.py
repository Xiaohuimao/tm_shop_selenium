import unittest,sys
from selenium import webdriver
from driver import Browser

class MyTest(unittest.TestCase):
        def setUp(self):
            self.driver = Browser.browser()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
        unittest.main()