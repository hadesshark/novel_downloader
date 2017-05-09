# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import sys

def get_web_page(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html5lib')
    else:
        return None

def get_page_novel(url):
    soup = get_web_page(url)
    content = ''

    for temp_content in soup.find_all('td', {'id': re.compile('postmessage_')}):
        content += temp_content.text + '\n\n'

    return content

def get_next_url(url):
    soup = get_web_page(url)
    if soup:
        try:
            next_url = soup.find('a', {'class': 'nxt'})['href']
        except:
            next_url = None
        return next_url

def total_novel(url):
    total_content = get_page_novel(url)
    temp_url = get_next_url(url)
    while temp_url:
        sys.stdout.write("\rurl: {0}".format(temp_url))
        total_content += get_page_novel(temp_url)
        temp_url = get_next_url(temp_url)

    return total_content

def main():
    url = "https://ck101.com/thread-3814619-1-1.html"

    with open('temp.txt', 'w', encoding='utf-8') as f:
        f.write(total_novel(url))


if __name__ == '__main__':
    main()
