# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import sys
import time
from lxml import etree
import json

old_url = ''
flag = 0

system = {'lxml', 'bs4'}

def get_web_page(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        if flag:
            return etree.HTML(response.text.encode('utf-8'))
        else:
            return BeautifulSoup(response.text, 'lxml')
    else:
        print(response.status_code)
        return None

def get_next_url(url):
    try:
        if flag:
            etree_page = get_web_page(url)
            next_url = etree_page.xpath(u"//div[@class='pg']/a[@class='nxt']/@href")[0]
        else:
            soup = get_web_page(url)
            next_url = soup.find('a', {'class': 'nxt'})['href']
    except:
        next_url = None
    print(next_url)
    return next_url

def main():
    with open("setting.json", encoding="utf-8") as json_file:
        json_data = json.load(json_file)[0]

    print(json_data)

    url = json_data.get('url')
    title_name = json_data.get('title')

    url_list = []
    temp_url = url

    while temp_url:
        url_list.append(temp_url)
        temp_url = get_next_url(temp_url)

    print(url_list)

if __name__ == '__main__':
    main()
