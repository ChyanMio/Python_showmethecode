# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 09:35:02 2018

@author: zhang
"""
from bs4 import BeautifulSoup
from urllib import request

def search_body(url):
    with request.urlopen(url) as page:
        content = BeautifulSoup(page, 'lxml')
        urls = content.find_all('a')
        for u in urls:
            print(u['href'])
        text = content.get_text().strip('\n')
    print("-----THIS IS THE TAXT PART-----")
    return text

url = "https://www.pythonforbeginners.com"
print(search_body(url))

