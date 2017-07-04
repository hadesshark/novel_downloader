# -*- coding: utf-8 -*-

import requests
from opencc import OpenCC

# url = 'http://www.xiaoqiangxs.com/modules/article/txtarticle.php?id=7072'
#
# response = requests.get(url)
# response.encoding = 'gb18030'
#
# with open("test.txt", mode='w') as file:
#     file.write(response.text)

file = open("test.txt", mode='r')

opencc = OpenCC('s2tw')
content = ''
for item in file.readlines():
    content += opencc.convert(item)

with open("test2.txt", mode='w') as file:
    file.write(content)
