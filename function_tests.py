# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json
import sys


import downloader
import unittest


class TestResponse(unittest.TestCase):

    # 把想要抓取的小說，給於基本資料
    def setUp(self):
        self.response = downloader.response


    # 傳送請求，存取小說在指定的位置
        # 傳送請求，獲得需要的小說


        # 內容需要修改的部分進行處理


        # 把獲得的小說內容存在指定的位置

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
