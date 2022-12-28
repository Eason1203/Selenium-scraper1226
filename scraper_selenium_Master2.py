from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
#http://localhost:8888/notebooks/Desktop/Python/Chapter01/Ch02_04.ipynb#

driver = webdriver.Chrome(executable_path='./chromedriver') #driver location with the same direction
driver.implicitly_wait(20) # wait for browser to respond 20 second at most
driver.get(url='https://bank.sinopac.com/mma8/bank/html/rate/bank_ExchangeRate.html#tab2')

# Below method is removded after Selenium 4.0 
#driver.find_element_by_id("SearchDateBegin").clear()
#driver.find_element_by_id("SearchDateBegin").send_keys('2022/01/01')
#driver.find_element_by_id("SearchDateEnd").clear()
# driver.find_element_by_id("ETSListSearch").click()

driver.find_element(By.ID, "SearchDateBegin").clear()
driver.find_element(By.ID,"SearchDateBegin").send_keys('2022/01/01')
time.sleep(1)
driver.find_element(By.ID, "SearchDateEnd").clear()
driver.find_element(By.ID, "SearchDateEnd").send_keys('2022/12/27')
time.sleep(1)
driver.find_element(By.ID, "ETSListSearch").click() # 查詢按鈕
time.sleep(1)
#有時候無法用Id or Class 取得 元素 就要用Xpath - 對著按鈕按檢查 copy xpath and paste it
driver.find_element(By.XPATH, '//*[@id="tab2"]/div[2]/div[2]/ul/li[1]/a').click() # 數據選項
time.sleep(1)
# element = driver.find_element(By.XPATH, '//*[@id="SearchPair"]/li[7]').click() #下拉選單 澳幣
# driver.execute_script("arguments[0].click();")
# write script
# script = "alert('Alert via selenium')"
# generate a alert via javascript
# driver.execute_script(script)


html_source = driver.page_source
soup = BeautifulSoup(html_source, 'lxml')
# table = soup.select('table')[0]
# for tr in table.select('tr'): # capture 3rd 
#    print(tr.div.text)
#    for td in tr.select('.bwc10'):
#     print(td.text)

table = soup.select('table#ETSListHist')[0]
for tr in table.select('tr')[1:]:
    for td in tr.select('td'):
        print(td.text, end='｜')
    print('')

table = soup.select('table#ETSListHist_TWO')[0]
for tr in table.select('tr')[1:]:
    for td in tr.select('td'):
        print(td.text, end='｜')
    print('')

time.sleep(1)
driver.find_element(By.ID, "ETSListSearch").click()


