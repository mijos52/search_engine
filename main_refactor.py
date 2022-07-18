from bs4 import BeautifulSoup
import requests
from meta import meta_data
import config
from pprint import pprint


def get_webpage_data(url: str) -> requests.Response.content:
    return requests.get(url).content


def soupify_webpage(webpage: requests.Response.content) -> BeautifulSoup:
    return BeautifulSoup(webpage, "lxml")


def find_full_urls(soup_data: BeautifulSoup) -> list:

    good_list = []

    for link in soup_data.find_all("a"):
        i = link.get("href")
        if i is None:
            pass
        elif (
            i.startswith("https://") or i.startswith("http://") or i.startswith("//www")
        ):
            good_list.append(i)
    return good_list


html_data = get_webpage_data("https://youtube.com")
soup_data = soupify_webpage(html_data)
url_list = find_full_urls(soup_data=soup_data)
pprint(url_list)
