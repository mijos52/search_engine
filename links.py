from bs4 import BeautifulSoup as Bs
import aiohttp
import asyncio
from pprint import pprint

url_list = ['https://youtube.com', 'https://bing.com']

full_link = []


def get_tasks(session):
    task_list = []
    try:
        for url in url_list:
            task_list.append(session.get(url))
            return task_list
    except Exception as e:
        print(e)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            html = await response.text()
            soup = Bs(html, 'lxml')

            meta_data = soup.find(attrs={"name": "description"})
            print(meta_data['content'])

        for i in soup.find_all('a'):
            i = i.get('href')
            if i is not None:
                good_link = i.startswith('https://') or i.startswith('http://') or i.startswith('//www')
                if good_link is True:
                    full_link.append(i)


                else:

                    full_link.append(i)

            else:
                continue
        pprint(full_link)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
