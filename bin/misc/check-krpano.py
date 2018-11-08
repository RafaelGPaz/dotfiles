#!/usr/bin/env python

from lxml import html
import requests
import time

def main():
    page = requests.get('http://krpano.com/download/')
    tree = html.fromstring(page.content)

    version = tree.xpath('//div[@class="paragraph"]//h2/text()')
    buildDate = tree.xpath('//span[@class="smallcomment"]/text()')

    # Comver list to string
    version = ''.join(version)
    buildDate = ''.join(buildDate)

    # Remove 7 first characters "(build "
    BuildDateClean = buildDate[7:]
    # Remove last character ")"
    BuildDateClean = BuildDateClean[:-1]

    today = time.strftime("%Y-%m-%d")
    # today = BuildDateClean

    # print(version)
    # print(BuildDateClean)
    # print(today)

    if BuildDateClean == today :
        message = version + buildDate + ' released!'
        print(message)

if __name__ == "__main__":
    main()

# Cron:
# cronttab -e
# 59 23 * * * /home/USERNAME/bin/check-krpano.py