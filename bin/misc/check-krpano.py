#!/usr/bin/env python

from lxml import html
import requests
import time
import sys

def main():
    page = requests.get('http://krpano.com/news/')
    tree = html.fromstring(page.content)

    version = tree.xpath('(//div[@class="newstitle"])[1]/a/text()')
    buildDate = tree.xpath('(//span[@class="newsdate"])[1]/a/text()')
    version = ''.join(version)
    buildDate = ''.join(buildDate)
    today = time.strftime("%Y-%m-%d")

    if buildDate == today :
        message = version + ' (' + buildDate + ') released!'
        print(message)

if __name__ == "__main__":
    main()

# Cron:
# cronttab -e
# 59 23 * * * /home/USERNAME/bin/check-krpano.py
