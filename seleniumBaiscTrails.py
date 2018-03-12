from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()

driver.get('https://www.google.com/')

#now we wait for 5 seconds to make broswer ready to click link
driver.implicitly_wait(5)
 #now click the link and the browser will be navigated to about page 


try:
    driver.find_elements_by_partial_link_text('Gmail')
    #about  = driver.find_element_by_link_text('About')
    #about.click()
    print('Test pass :partial  link text  found ')

except Exception as e:
    print ('Exception Found ', format(e))


id = driver.find_elements_by_xpath("//*[@class]")

#get all class of google 
#for i in id :
  #  print(i.get_attribute('class'))


# first method refresh
time.sleep(2)
driver.refresh()

#second method : keyboard shortcut f5
time.sleep(2)
driver.find_element_by_tag_name('body').send_keys(Keys.F5)

querry=driver.find_element_by_name("q").send_keys("querrry")  
## browser  version   
print ('Version of chrome',driver.capabilities['version'])
#give you the current url  in which ur in 
print('Current url --',driver.current_url)
body = driver.find_element_by_tag_name('body')
body.send_keys(Keys.CONTROL+'t')


#time.sleep(2)
#driver.close()    