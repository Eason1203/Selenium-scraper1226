from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.implicitly_wait(15)
driver.get(url='https://shopee.tw/mall/%E5%B1%85%E5%AE%B6%E7%94%9F%E6%B4%BB-cat.11040925')

html_source=driver.page_source
#driver.quit

soup =BeautifulSoup(html_source, 'lxml')

table = soup.select('table')[0]

print(table)