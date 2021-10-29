from meta import meta
from links import links
from db import db_write_multiple, db_read

# TODO:Get text from all pages and create keywords
# TODO:Make url fetch asynchronous

# Global variables
url_list = ['https://google.com', 'https://youtube.com']
full_list = []

# execute link() twice for main and sub url lists
for _url in url_list:
    try:
        full_list = links(_url)

    except Exception as e:
        print(e)

# meta data
meta_data_list = []

for i in full_list:
    meta_data = meta(i)
    try:
        val = (meta(i), None, i)
        db_write_multiple(val)

    except Exception as e:
        print(e)

try:
    db_read()
except Exception as e:
    print(e)

"""
    Enter values in multiple groups into the database 
    Uses the sql write multiple rows query
"""
