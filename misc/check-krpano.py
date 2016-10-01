#!/usr/bin/env python

from lxml import html
import requests
import time
import tweepy
# Import tweeter private keys
from private import cfg

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

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

    # print(version);
    # print(BuildDateClean);
    # print(today)

    if BuildDateClean == today :
        api = get_api(cfg)
        tweet = version + buildDate + ' released! Click on the link underneath to download #krpano http://krpano.com/download/'
        status = api.update_status(status=tweet)

        print(tweet)

if __name__ == "__main__":
    main()
