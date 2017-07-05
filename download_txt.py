# -*- coding: utf-8 -*-

import requests
from tqdm import *

from initialize import JsonFile
from downloader import Downloader
from opencc import OpenCC
from content_fix import Content


class Downloader(Downloader):

    def get_web_page(self):
        response = requests.get(self.url)
        response.encoding = 'gb18030'
        self.json_file = JsonFile()

        self.set_title()

        self.txt_space = r"./txt_file//"

        with open(self.txt_space + self.json_file.__str__(), mode="w", encoding="utf-8") as file:
            file.write(response.text)

    def set_title(self):
        self.json_file.set_title(OpenCC('s2tw').convert(self.json_file.get_title()))


class SimpleToTW(Content):

    def check(self):
        file = open(self.before_update, "r", encoding="utf-8")

        opencc = OpenCC('s2tw')
        for item in tqdm(file.readlines()):
            self.content += opencc.convert(item).encode('utf-8')

        file.close()


def main():
    Downloader().get_web_page()
    SimpleToTW().update()

if __name__ == '__main__':
    main()
