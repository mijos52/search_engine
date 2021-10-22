import requests as rq
from bs4 import BeautifulSoup as bs

'''
function finds the meta data tag and return a string 
uses (soup.meta) methord form bs4 to extract meta tag
extract content using meta["content"]

'''

#TODO: NoneType object error has to be handled

key_list = []

def meta(Url):

  try:

    response = rq.get(Url)
    html = response.content
  

    soup = bs(html , 'lxml')
   
    meta_data = soup.find(attrs={"name":"description"})  
    print(meta_data['content'])
  
  except Exception as e:
    print(e)


  except AttributeError:
    print('its an atribute error')


