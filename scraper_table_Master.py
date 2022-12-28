from bs4 import BeautifulSoup
import requests
import time

url = 'https://tw.stock.yahoo.com/q/q'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

stock_id_list = ['3058', '2601', '2022','1313']

def get_stock_price(stock_id):
    payload = {
        's': stock_id
    }
    
    response = requests.get(url, params=payload, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'lxml')
    tables = soup.find_all('table')
    table = tables[2]

    tds = table.find_all('td')
    
    for td in tds[:-1]:
        print(td.text.strip().replace('加到投資組合', ''))
    
for stock_id in stock_id_list:
    
    try:
        get_stock_price(stock_id)
    except Exception as err:
        print('{}失敗：{}'.format(stock_id, err))
      
    print('-'*20)
    time.sleep(3)