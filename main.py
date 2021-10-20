from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint


url_list = ['https://www.youtube.com','https://www.google.com','https://www.bing.com']

def links(Url):
  response = requests.get(Url)
  html = response.content

  #provide the response and the parser
  soup = bs(html , 'lxml')

  #Get all the links in a webpage 
  '''
  for each item in object collection of all tags with a 
  print href in each a tag

  '''
  for link in soup.find_all('a'):
    print(link.get('href'))

# go through the list and fetch all the links in the page
for i in url_list:
   links(i)