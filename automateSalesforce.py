from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
 
data=json.load(open('jsonxpath.json'))
driver = webdriver.Chrome()
#your testing url
driver.get("https://www.google.com/")

driver.maximize_window()
driver.implicitly_wait(20)
#define in json to set path
driver.find_element_by_id(data["text"][0]["abc"]).send_keys(data["1"][0]["def"])
driver.find_element_by_id(data["loginSalesForce"][0]["password"]).send_keys(data["userdata"][0]["passworddetails"])

driver.find_element_by_id(data["clickAction"]["loginButton"]).click()
#advt dilogue box
driver.find_element_by_id("tryLexDialogX").click()
driver.find_element_by_link_text(data["someaction"]["actionname"]).click()
driver.find_element_by_name("new").click()





 

