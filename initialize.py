# -*- coding: utf-8 -*-
import json


class JsonFile(object):
    def __init__(self):
        with open("setting.json", encoding="utf-8") as json_file:
            self.json_data = json.load(json_file)[0]

    def get_title(self):
        return self.json_data.get('title')

    def get_url(self):
        return self.json_data.get('url')

    def get_author(self):
        return self.json_data.get('author')

    def __str__(self):
        return ("{0} 作者：{1}.txt").format(self.get_title(), self.get_author())
