# -*- coding: utf-8 -*-
import json
import os
import shutil

from tqdm import *


class JsonFile(object):
    def __init__(self):
        with open("setting.json", encoding="utf-8") as json_file:
            self.json_data = json.load(json_file)[0].get('title')
            self.title = self.name()

    def name(self):
        return self.json_data + ".txt"

    def __str__(self):
        return ("{0} size: {1}".format(
            self.json_data, os.path.getsize(self.name())))


def show_information(file_name, system_name):
    print("{0} size: {1}".format(file_name, os.path.getsize(system_name)))


def main():

    txt_space = r"./txt_file//"
    if os.path.exists(txt_space):
        os.mkdir(txt_space)

    if os.path.isfile(txt_space + "temp.txt"):
        os.remove(txt_space + "temp.txt")

    if os.path.isfile(txt_space + "temp2.txt"):
        os.remove(txt_space + "temp2.txt")

    json_file = JsonFile()
    shutil.copy(txt_space + json_file.title, txt_space + "temp.txt")
    show_information(json_file.json_data, txt_space + json_file.title)

    file = open(txt_space + "temp.txt", "rb")
    # file.seek

    content = "".encode('utf-8')
    for item in tqdm(file.readlines()):
        if len(item) == 1:
            continue
        elif "  ".encode('utf-8') in item:  # 多空格行
            continue
        elif "本帖最後由".encode('utf-8') in item:
            continue
        # 某些技術性空格無法處理
        # elif "\r\n".encode('utf-8') in item:
        #     continue
        else:
            content += item
    file.close()

    with open(txt_space + "temp2.txt", "wb") as file:
        file.write(content)

    shutil.copy(txt_space + "temp2.txt", txt_space + json_file.title)
    show_information(json_file.json_data, txt_space + json_file.title)


if __name__ == '__main__':
    main()
