from bs4 import BeautifulSoup as Bs
import requests as rq
# import os
from meta import meta

from db import db_write, db_read, db_show_table

# os.system('clear')

url_list = ['https://google.com']

good_list = []
bad_list = []

print("start")


def links(_url):
    response = rq.get(_url)
    html = response.content

    # provide the response and the parser
    soup = Bs(html, 'lxml')

    # Get all the links in a webpage
    '''
    1.use find all with an a tag get href from each   
    2.check weather href = None (To avoid none type error)
    3.check good link (properly formatted) else format it 
    4.links are cleaned and separated into good and bad links

  '''
    for i in soup.find_all('a'):
        i = i.get('href')
        if i is not None:
            good_link = i.startswith('https://') or i.startswith('http://') or i.startswith('//www')
            if good_link is True:
                good_list.append(i)
                print("good link is ", i)

            else:
                print("bad list is", _url + i)
                bad_list.append(_url + i)

        else:
            continue


# TODO: best database structure


# execute link() twice for main and sub url lists
for x in url_list:
    try:
        links(x)

    except Exception as e:
        print(e)

# meta data
meta_data_list = []
for i in good_list:
    meta_data = meta(i)
    meta_data_list.append(meta_data)
print(meta_data_list)

for i in meta_data_list:
    try:
        db_write(i, "hai", "how")
    except Exception as e:
        print(e)

# try:
#     db_read()
# except Exception as e:
#     print(e)
