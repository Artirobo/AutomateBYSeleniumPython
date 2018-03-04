import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
# setup is the method which contain the variable driver  setUp is part of initialization, 
def setUp(self):
self.driver = webdriver.Chrome()

# This is the test case method. The test case method should always start with characters test.
def test_search_in_python_org(self):
driver = self.driver
#driver.get method will navigate to a page given by the URL.
driver.get("http://www.google.com")
# next line is an assertion to confirm that title has “Google”
self.assertIn("Google", driver.title)
#WebDriver offers a number of ways to find elements using one of the find_element_by_* methods.
elem = driver.find_element_by_name("q")
#Sending keys, this is similar to entering keys using your keyboard
elem.send_keys("pycon")
#submission of the page, you should get the result as per search if there is any
elem.send_keys(Keys.RETURN)
#if there is any. To ensure that some results are found, make an assertion:
assert "No results found." not in driver.page_source

#tearDown method will get called after every test method.
def tearDown(self):
self.driver.close()
#Final lines are some boiler plate code to run the test suite:
if __name__ == "__main__":
unittest.main()