from selenium import webdriver
import unittest

class TestSearchMethods(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('https://www.python.org/')

    def test_search(self):
        text = self.browser.find_element_by_id("id-search-field")
        text.send_keys("python")
        button_go = self.browser.find_element_by_id("submit")
        button_go.click()
        self.browser.find_element_by_xpath("//h3[text()='Results']")

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
#    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

