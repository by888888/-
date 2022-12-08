"""
===============================
 Time  :  
 Author:   baiyu
===============================
"""
import csv
import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}
url = 'https://www.cnhnb.com/hangqing/cdlist-2000586-580/'
# print(url)
message = requests.get(url,headers=headers)
soup = BeautifulSoup(message.text,'lxml')
if soup.title.string == '请验证':
    print(message.url)
    # break
else:
    mess = []
    mess_dict = {}
    for ul in soup.select('.product')[1:]:
        mess_dict['产品']=ul.get_text()
        mess.append(mess_dict)
    for ul in soup.select('.place')[1:]:
        mess_dict['所在地']=ul.get_text()
        mess.append(mess_dict)
    for ul in soup.select('.price')[1:]:
        mess_dict['价格']=ul.get_text()
        mess.append(mess_dict)
    # print(mess)
    mess1 = []
    for i in mess:
        if len(i) == 3:
            mess1.append(i)
    print(mess1)