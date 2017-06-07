# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
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
        return BeautifulSoup(response.text, 'lxml')
    else:
        return None

def get_web_page_lxml(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return etree.HTML(response.text.encode('utf-8'))
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
    # xpath_content =  u"//td[@class='t_f']"
    # etree_page = get_web_page_lxml(url).xpath(xpath_content)
    #
    # content = ''
    # for item in etree_page:
    #     for item_del in item.xpath(u"//i[@class='pstatus']"):
    #         item_del.getparent().remove(item_del)
    # for item in etree_page:
    #     for temp_content in item.xpath(u"//td[@class='t_f']//text()"):
    #         content += temp_content

    xpath_content = u"//td[@class='t_f']//text()"
    etree_page = get_web_page_lxml(url).xpath(xpath_content)
    content = ''
    for item in etree_page:
        content += item + '\n\n'

    return content

def get_next_url(url):
    soup = get_web_page(url)
    try:
        next_url = soup.find('a', {'class': 'nxt'})['href']
    except:
        next_url = None
    return next_url

def get_next_url_lxml(url):
    etree_page = get_web_page_lxml(url)
    try:
        next_url = etree_page.xpath(u"//div[@class='pg']/a[@class='nxt']/@href")[0]
    except:
        next_url = None
    return next_url

def total_novel(url):
    total_content = get_page_novel(url)
    temp_url = get_next_url(url)
    while temp_url:
        t_start = time.time()
        sys.stdout.write("\rurl: {0}".format(temp_url))
        total_content += get_page_novel(temp_url)
        temp_url = get_next_url(temp_url)
        t_end = time.time()
        print("sec: {0}".format(t_end - t_start))

    return total_content

def total_novel_lxml(url):
    total_content = get_page_novel_lxml(url)
    temp_url = get_next_url_lxml(url)
    while temp_url:
        t_start = time.time()
        sys.stdout.write("\rurl: {0}".format(temp_url))
        total_content += get_page_novel_lxml(temp_url)
        temp_url = get_next_url_lxml(temp_url)
        t_end = time.time()
        print("sec: {0}".format(t_end - t_start))
    return total_content

def main():
    with open("setting.json", encoding="utf-8") as json_file:
        json_data = json.load(json_file)[0]

    with open(title_name + '.txt', 'w', encoding='utf-8') as f:
        f.write(total_novel_lxml(url))


if __name__ == '__main__':
    main()
