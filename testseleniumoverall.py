#pip install requests
import requests
#pip install beautifulsoup4
#this is used to get a page format style page
from bs4 import BeautifulSoup
#lxml is a pretty extensive library written for parsing XML and HTML documents 
# very quickly, even handling messed up tags in the process
from lxml import html


page=requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

print 'page -- with response',page  # output is <Response[200]>

print'status code',page.status_code # 200 


#this will distplay a page formate style 
soup = BeautifulSoup(page.content, 'html.parser')
#display format page 
print (soup)
#formate the style 
print(soup.prettify())


page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

#<div title="buyer-name">Carson Busses</div>
#<span class="item-price">$29.95</span>
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
prices = tree.xpath('//span[@class="item-price"]/text()')
print 'Buyers: ', buyers

print 'prices', prices
