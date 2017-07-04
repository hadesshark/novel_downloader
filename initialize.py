# -*- coding: utf-8 -*-
import json


class JsonFile(object):
    def __init__(self):
        with open("setting.json", encoding="utf-8") as json_file:
            self.json_data = json.load(json_file)[0]

        self.title = self.json_data.get('title')
        self.url = self.json_data.get('url')
        self.author = self.json_data.get('author')

    def get_title(self):
        return self.title

    def set_title(self, title=''):
        self.title = title

    def get_url(self):
        return self.url

    def get_author(self):
        return self.author

    def set_author(self, author=''):
        self.author = author

    def __str__(self):
        if len(self.author):
            return ("{0} 作者：{1}.txt").format(self.get_title(), self.get_author())
        else:
            return ("{0}.txt").format(self.get_title())

    def data(self):
        return [{'title': self.title, 'url': self.url, 'author': self.author}]

    def __del__(self):
        with open("setting.json", mode="w", encoding="utf-8") as json_file:
            json.dump(self.data(), json_file)
