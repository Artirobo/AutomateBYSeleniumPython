import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)
#its like static void main method in java 
if __name__ == '__main__':
    #Verbose is a general programming term for produce lots of logging output
    #log 
    unittest.main(verbosity=2)