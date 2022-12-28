from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path='./chromedriver') #driver location with the same direction
driver.implicitly_wait(20) # wait for browser to respond 20 second at most
driver.get(url='https://bank.sinopac.com/mma8/bank/html/rate/bank_ExchangeRate.html')

html_source = driver.page_source
driver.quit # close driver

print(html_source)

soup = BeautifulSoup(html_source, 'lxml')
table = soup.select('table')[0]

for tr in table.select('tr')[2:]: # capture 3rd 
   print(tr.div.text)
   for td in tr.select('.bwc10'):
    print(td.text)