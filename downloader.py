# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json
import sys


url = "https://ck101.com/thread-3845788-1-1.html"

class Response(object):

    __headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36'}

    def __init__(self, url=""):
        self.response = requests.get(url, headers=self.__headers)

    def status_code(self):
        return self.response.status_code
