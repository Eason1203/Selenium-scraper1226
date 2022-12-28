# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://tw.stock.yahoo.com/quote/2330')
# soup = BeautifulSoup(response.text, 'lxml')
# filter1 = soup.find('ul', {'class':'D(f) Fld(c) Flw(w) H(192px) Mx(-16px)'})
# filter2 = filter1.find_all('li', {'class':'price-detail-item H(32px) Mx(16px) D(f) Jc(sb) Ai(c) Bxz(bb) Px(0px) Py(4px) Bdbs(s) Bdbc($bd-primary-divider) Bdbw(1px)'})

# result = []
# index = 0
# for filter3 in filter2:
#     print("\n")
#     print(filter3)
#     print(type(filter3))
#     Title = filter3.find('span', {'class':'C(#232a31) Fz(16px)--mobile Fz(14px)'}).getText()
#     Content = filter3.find().getText()
#     print(Title)
#     print(Content)
#     index = index+1

# print(index)


import requests
from bs4 import BeautifulSoup
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

stock_id_list = ['2330', '2486', '3058', '3490']



def get_stock_price(stock_id):
    url = f'https://tw.stock.yahoo.com/quote/{stock_id}'

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'lxml')

    # 透過class為【D(f) Fld(c) Flw(w) H(192px) Mx(-16px)】來取得ul標籤，裡面包含了成交價、開盤價、最高價等等所需資訊
    company = soup.find('h1',{'class':'C($c-link-text) Fw(b) Fz(24px) Mend(8px)'}).getText()
    ul = soup.find('ul', {'class': 'D(f) Fld(c) Flw(w) H(192px) Mx(-16px)'})
    print(company)
    
    # test = soup.find('li', {'class':'price-detail-item H(32px) Mx(16px) D(f) Jc(sb) Ai(c) Bxz(bb) Px(0px) Py(4px) Bdbs(s) Bdbc($bd-primary-divider) Bdbw(1px)'}).getText()
    # print("test"+test)
    # 使用 for 迴圈將所有 li 標籤內容給 print 出來
    print('股票代號', stock_id)
    for li in ul:
        print(li.text)

for stock_id in stock_id_list:

    try:
        get_stock_price(stock_id)
    except Exception as err:
        #print('{}失敗：{}'.format(stock_id, err))
        print(f'{stock_id}失敗：{err}')
    print('-'*20)
    time.sleep(2)
