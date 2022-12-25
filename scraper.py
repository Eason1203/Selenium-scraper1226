from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains #關閉彈跳視窗

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://shopee.tw/mall/%E5%B1%85%E5%AE%B6%E7%94%9F%E6%B4%BB-cat.11040925')

time.sleep(5)

ActionChains(driver).move_by_offset(100,100).click().perform() #關閉彈跳視窗

cards = driver.find_elements(By.CSS_SELECTOR, "div[class='col-xs-2 recommend-products-by-view__item-card-wrapper']")

#cards = driver.find_elements(By.TAG_NAME, "div")
print(cards)

items = []
for card in cards:
    ActionChains(driver).move_to_element(card).perform()
    title = card.find_elements(By.CSS_SELECTOR, "div[class='S-VCpK JFJ4OD _88FgR3']").text
    price = card.find_elements(By.CSS_SELECTOR, "div[class='A9okRS']").text
    link = card.find_elements(By.TAG_NAME, "a").get_sttribute('href')

    items.append((title,price,link))

print(items)
