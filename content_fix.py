# -*- coding: utf-8 -*-
import json
import os
import shutil

from tqdm import *

from initialize import JsonFile as JsonFile


def show_information(file_name, system_name):
    print("{0} size: {1}".format(file_name, os.path.getsize(system_name)))


class Content(object):

    def __init__(self):
        self.txt_space = r"./txt_file//"
        self.before_update = self.txt_space + "temp.txt"
        self.after_update = self.txt_space + "temp2.txt"

        self.json_file = JsonFile()
        self.finish_version = self.txt_space + self.json_file.__str__()
        self.file_name = self.json_file.json_data

        self.content = "".encode('utf-8')

    def txt_space_fix(self):
        if not(os.path.exists(self.txt_space)):
            os.mkdir(self.txt_space)

        if os.path.isfile(self.before_update):
            os.remove(self.before_update)

        if os.path.isfile(self.after_update):
            os.remove(self.after_update)

    def check(self):
        file = open(self.before_update, "rb")

        for item in tqdm(file.readlines()):
            if len(item) == 1:
                continue
            elif "  ".encode('utf-8') in item:  # 多空格行
                continue
            elif "本帖最後由".encode('utf-8') in item:
                continue
            else:
                self.content += item
        file.close()

    def update(self):
        self.txt_space_fix()

        shutil.copy(self.finish_version, self.before_update)
        show_information(self.file_name, self.finish_version)

        self.check()

        with open(self.after_update, "wb") as file:
            file.write(self.content)

        shutil.copy(self.after_update, self.finish_version)
        show_information(self.file_name, self.finish_version)


def main():
    Content().update()

if __name__ == '__main__':
    main()
