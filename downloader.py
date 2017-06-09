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

def show_download_info(url):
    sys.stdout.write("\rurl: {0}".format(url))

class SettingInfo(object):
    def __init__(self):
        with open("setting.json", encoding="utf-8") as json_file:
            self.json_data = json.load(json_file)[0]

        self.url = self.json_data.get('url')
        self.title = self.json_data.get('title')

    def get_url(self):
        return self.url

    def get_title(self):
        return self.title

    def show_title(self):
        print(self.title)


class downloader(object):
    __xpath_content = u"//td[@class='t_f']//text()"

    def get_page_chapters(self, url):
        etree_page = get_web_page(url).xpath(self.__xpath_content)
        content = ''
        for item in etree_page:
            content += item + '\n\n'
        return content


class Chapter(object):
    def __init__(self, url=SettingInfo().get_url()):
        self.url = url
        self.content = ''

    def collect(self):
        while self.url:
            show_download_info(self.url)

            self.content += downloader().get_page_chapters(self.url)
            self.url = get_next_url(self.url)

        return self.content


class Novel(object):
    def __init__(self):
        self.info = SettingInfo()
        self.url = self.info.get_url()
        self.title = self.info.get_title()

    def save(self):
        with open(self.title + '.txt', 'w', encoding='utf-8') as f:
            f.write(Chapter().collect())

    def show_title(self):
        self.info.show_title()

def main():
    novel = Novel()
    novel.show_title()
    novel.save()


if __name__ == '__main__':
    main()
