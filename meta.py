import requests as rq
from bs4 import BeautifulSoup as Bs

'''
function finds the meta data tag and return a string 
uses (soup.meta) method form bs4 to extract meta tag
extract content using meta["content"]

'''

# TODO: NoneType object error has to be handled

key_list = []


def meta(_url):
    try:

        response = rq.get(_url)
        html = response.content

        soup = Bs(html, 'lxml')

        meta_data = soup.find(attrs={"name": "description"})
        print(meta_data['content'])

    except Exception as e:
        print(e)
