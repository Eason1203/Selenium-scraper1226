from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.google.com/search'

stock_id_list = ['2330', '1101', '1102', '2324']

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

def get_stock_info(stock_id):
    payload = {'q': stock_id}
    response = requests.get(url, params=payload, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    #-----------------Method 1-------------------------------------
    company = soup.select('div.kno-rdesc span')[0].text
    Web_address = soup.select('div.kno-rdesc a')[0].get('href')
    print(company)
    print(Web_address)
    print("-"*20)
    #-----------------Method 2-------------------------------------

    div_list = soup.find_all('div',{'class':'kno-rdesc'})
    # print(div_list)
    # print("-"*20)
    for div in div_list:
            print(div.getText())
            web_address = div.find('a',{'class':'ruhjFe NJLBac fl'}).get('href')
            print(web_address)
            print("-"*20)
    #-----------------Method 3-------------------------------------
    print(div_list[0].span.text)
    print(div_list[0].a.get('href'))
    print("-"*20)

for stock_id in stock_id_list:

    try:
        get_stock_info(stock_id)
    except Exception as err:
        #print('{}失敗：{}'.format(stock_id, err))
        print(f'{stock_id}失敗：{err}')
    #print('-'*20)
    time.sleep(2)
   