from selenium import webdriver
import unittest

class TestStringMethods(unittest.TestCase):


    def test_search(self):
    self.browser = webdriver.Firefox()
        self.browser.get('https://www.python.org/')
        text = self.browser.find_element_by_id("id-search-field")
        text.send_keys("python")
        click(find_element_by_id("submit"))
        

if __name__ == '__main__':
    unittest.main()

