from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#you can specify the line  path 
# driver=webdriver.chrome("your path")
driver = webdriver.Chrome()
#page load timeout  if page can't load in 30  than it give error page load error  
driver.set_page_load_timeout(30)
#call the web page 
driver.get("https://www.google.com.np/")
#maximize the window
driver.maximize_window()

#time that wait implicitly for 20 sec
driver.implicitly_wait(20)

#this will screen shot the page and if you didn't specify the path location it will be in ur project folder
# file location to save screenshot within project folder   screenshots is the folder
driver.get_screenshot_as_file("./screenshots/FirstPhase.png")

#print the title of page
print(driver.title)

assert "Google" in driver.title


#find the element by name  and send the custom message in that field by name
driver.find_element_by_name("q").send_keys("querrry")     

#find the element by id and send the keys to that element
#driver.find_element_by_id("lst-ib").send_keys("querry")

#find the element by xpath and send the keys to that element
#driver.find_element_by_xpath("  //input[@id='lst-ib']").send_keys("hello world")

#driver click the google search button by click method 
driver.find_element_by_name("btnK").click()

#this will screen shot the page and if you didn't specify the path location it will be in ur project folder
# file location to save screenshot within project folder   screenshots is the folder 
driver.get_screenshot_as_file("./screenshots/SecondPhase.png")
#stop the automate
driver.quit()