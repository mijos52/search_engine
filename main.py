from bs4 import BeautifulSoup 
import requests 
from meta import meta_data

url_list = ['https://google.com']

good_list = []
bad_list = []

print("start")


def links(_url):
    response = requests.get(_url)
    html = response.content

    # provide the response and the parser
    soup = BeautifulSoup(html, 'lxml')


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


# execute link() twice for main and sub url lists
for x in url_list:
    try:
        links(x)

    except Exception as e:
        print(e)

# meta data
meta_data_list = []
for i in good_list:
    meta_data = meta_data(i)
    meta_data_list.append(meta_data)
print(meta_data_list)


