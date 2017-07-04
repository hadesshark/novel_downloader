# -*- coding: utf-8 -*-

import requests

from initialize import JsonFile
from downloader import Downloader
from opencc import OpenCC
from content_fix import Content

# url = 'http://www.xiaoqiangxs.com/modules/article/txtarticle.php?id=7072'
#
# response = requests.get(url)
# response.encoding = 'gb18030'
#
# with open("test.txt", mode='w') as file:
#     file.write(response.text)

# file = open("test.txt", mode='r')
#
# opencc = OpenCC('s2tw')
# content = ''
# for item in file.readlines():
#     content += opencc.convert(item)
#
# with open("test2.txt", mode='w') as file:
#     file.write(content)

class Downloader(Downloader):

    def get_web_page(self):
        response = requests.get(self.url)
        response.encoding = 'gb18030'
        self.json_file = JsonFile()

        self.set_title()

        self.txt_space = r"./txt_file//"

        with open(self.txt_space + self.json_file.__str__(), mode="w") as file:
            file.write(response.text)

    def set_title(self):
        self.json_file.set_title(OpenCC('s2tw').convert(self.json_file.get_title()))


class SimpleToTW(Content):

    def check(self):
        file = open(self.before_update, "rb")

        opencc = OpenCC('s2tw')
        for item in file.readlines():
            self.content += opencc.convert(item)

        file.close()


def main():
    # Downloader().get_web_page()
    SimpleToTW().update()

if __name__ == '__main__':
    main()
