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

def etree_way():
    return etree.HTML(response.text.encode('utf-8'))

def bsf_way():
    return BeautifulSoup(response.text, 'lxml')

def get_web_page(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:

        if flag:
            etree_way()
        else:
            bsf_way()
    else:
        return None

def del_i_label(dom):
    if dom.i:
        dom.i.decompose()
    return dom

def get_page_novel(url):
    soup = get_web_page(url)
    content = ''

    for temp_content in soup.find_all('td', {'id': re.compile('postmessage_')}):
        temp_content = del_i_label(temp_content)
        content += temp_content.text + '\n\n'

    return content

def get_page_novel_lxml(url):
    xpath_content = u"//td[@class='t_f']//text()"
    etree_page = get_web_page(url).xpath(xpath_content)
    content = ''
    for item in etree_page:
        content += item + '\n\n'
    return content

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
    return next_url

def total_novel(url):
    global old_url
    old_url = url
    if flag:
        total_content = get_page_novel_lxml(url)
    else:
        total_content = get_page_novel(url)

    temp_url = get_next_url(url)

    while temp_url:
        t_start = time.time()
        sys.stdout.write("\rurl: {0}".format(temp_url))
        if flag:
            total_content += get_page_novel_lxml(temp_url)
        else:
            total_content += get_page_novel(temp_url)

        temp_url = get_next_url(temp_url)
        t_end = time.time()
        print("sec: {0}".format(t_end - t_start))
    return total_content

def main():
    with open("setting.json", encoding="utf-8") as json_file:
        json_data = json.load(json_file)[0]

    print(json_data)

    url = json_data.get('url')
    title_name = json_data.get('title')

    with open(title_name + '.txt', 'w', encoding='utf-8') as f:
        f.write(total_novel(url))


if __name__ == '__main__':
    main()
