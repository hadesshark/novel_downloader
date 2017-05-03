# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json
import sys


headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36'}


url = "https://ck101.com/thread-3845788-1-1.html"

response = requests.get(url, headers=headers)
