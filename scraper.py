from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://shopee.tw/mall/%E5%B1%85%E5%AE%B6%E7%94%9F%E6%B4%BB-cat.11040925')

time.sleep(5)

cards = driver.find_element(By.CSS_SELECTOR, "div[class='UpbuCz']")

Items = []
for card in cards:
    title = card.find_element(By.CSS_SELECTOR, "div[class='S-VCpK JFJ4OD _88FgR3']").text
    price = card.find_element(By.CSS_SELECTOR, "div[class='A9okRS']").text
    link = card.find_element(By.TAG_NAME, "a").get_sttribute('href')

    Items.append((title,price,link))

print(Items)
