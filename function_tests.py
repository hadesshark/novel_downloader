# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json
import sys

import downloader

from bs4 import BeautifulSoup

import re

# 把想要抓取的小說，給於基本資料
print(downloader.soup.find('h1', {'id': re.compile('thread')}).text)



"""
    傳送請求，存取小說在指定的位置
        傳送請求，獲得需要的小說
"""
        # 抓取下一頁 url


        # 抓取文章



        # 內容需要修改的部分進行處理


        # 把獲得的小說內容存在指定的位置
