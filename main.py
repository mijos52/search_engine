from bs4 import BeautifulSoup as Bs
import requests as rq
# import os
# from meta import meta
from db import db

# os.system('clear')

url_list = ['https://www.google.com', 'https://www.yahoo.com/']

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

            else:
                bad_list.append(_url + i)
        else:
            continue


# TODO: find a way to get meta data of each page
# TODO: best database structure


# execute link() twice for main and sub url lists
for x in url_list:
    try:
        links(x)

    except Exception as e:
        print(e)

# meta data
# for i in bad_list:
#     meta(i)

try:
    db()
except Exception as e:
    print(e)
