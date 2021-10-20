import requests
from pprint import pprint

x = requests.get('https://pokeapi.co/api/v2/generation/?limit=2')
pprint(x.json())