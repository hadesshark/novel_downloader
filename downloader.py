# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


url = "https://ck101.com/thread-3845788-1-1.html"

def get_web_page(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def main():
    soup = get_web_page(url)


if __name__ == '__main__':
    main()
