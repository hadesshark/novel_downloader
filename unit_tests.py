# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json
import sys

import unittest
from downloader import *


class TestResponse(unittest.TestCase):

    def setUp(self):
        self.response = downloader.response

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
