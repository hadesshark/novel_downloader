# -*- coding: utf-8 -*-
import requests
import re
import sys
import time
from lxml import etree
import json

def get_web_page(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return etree.HTML(response.text.encode('utf-8'))
    else:
        return None

def get_page_chapters(url):
    xpath_content = u"//td[@class='t_f']//text()"
    etree_page = get_web_page(url).xpath(xpath_content)
    content = ''
    for item in etree_page:
        content += item + '\n\n'
    return content

# 全部頁數
def get_all_page_num(url):
    xpath_all_num = u"//div[@class='pg']/a[@class='last']//text()"
    etree_page = get_web_page(url)
    all_num = etree_page.xpath(xpath_all_num)[0]

    print(all_num.split(' ')[-1])

def get_next_url(url):
    try:
        xpath_next_url = u"//div[@class='pg']/a[@class='nxt']/@href"
        etree_page = get_web_page(url)
        next_url = etree_page.xpath(xpath_next_url)[0]
    except:
        next_url = None
    return next_url

def total_novel(url):

    total_content = get_page_chapters(url)

    temp_url = get_next_url(url)

    while temp_url:
        sys.stdout.write("\rpage: {0}".format(temp_url.split('-')[-2]))

        total_content += get_page_chapters(temp_url)
        temp_url = get_next_url(temp_url)

    return total_content

def main():
    with open("setting.json", encoding="utf-8") as json_file:
        json_data = json.load(json_file)[0]

    print(json_data.get('title'))

    url = json_data.get('url')
    title_name = json_data.get('title')

    with open(title_name + '.txt', 'w', encoding='utf-8') as f:
        f.write(total_novel(url))


if __name__ == '__main__':
    main()
