from selenium import webdriver
#you can specify the line  path 
# driver=webdriver.chrome("your path")
driver = webdriver.Chrome()

driver.get("http://econpy.pythonanywhere.com/ex/001.html")

#extract list of  buyers and price  based on xpath find elements by xpath
buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

print (buyers )
print (prices)

num_of_items_in_page = len(buyers)
for i in range(num_of_items_in_page):
    print(buyers[i].text + " : " + prices[i].text)


driver.quit()