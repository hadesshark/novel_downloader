# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json
import sys

import downloader

from bs4 import BeautifulSoup

import re

def del_i_label():
    if temp_page.i:
        temp_page.i.decompose()

url = "https://ck101.com/thread-3814619-1-1.html"

web_page = downloader.get_web_page(url)
temp_page = web_page.find('td', {'id': re.compile('postmessage_')})
del_i_label()
del_i_label()

with open('temp.txt', 'w', encoding='utf-8') as f:
    f.write(temp_page.text)

# from opencc import OpenCC
# # 亂碼轉簡體再轉繁體
# url = 'http://www.xiaoqiangxs.com/modules/article/txtarticle.php?id=7072'
#
# response = requests.get(url)
# response.encoding = 'gb18030'
#
# with open("test.txt", mode='w') as file:
#     file.write(response.text)
#
# file = open("test.txt", mode='r')
#
# opencc = OpenCC('s2tw')
# content = ''
# for item in file.readlines():
#     content += opencc.convert(item)
#
# with open("test2.txt", mode='w') as file:
#     file.write(content)


"""
from opencc import OpenCC
from downloader import Novel 

def convert(string=""):
    return OpenCC('s2tw').convert(string)

Content(object):

    def __init__(self):
        self.file = open("test.txt", mode='r')
        self.content = ''

    def update(self):
        for item in self.file.readlines():
            self.content += convert(item)


class Novel(Novel):

    def save(self):
        with open("test2.txt", mode='w') as file:
            file.write(Content().update())

Novel().save()

"""
