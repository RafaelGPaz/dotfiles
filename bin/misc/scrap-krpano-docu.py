# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import argparse
import logging

import colorlog

from requests_html import HTMLSession


def main():
    # Add description
    parser = argparse.ArgumentParser(description='Description')
    # parser.add_argument('-o', '--origin', action=readable_dir, dest='origin', help='Parameter which autocomplete directories')
    # parser.add_argument('-d', '--destination', dest='destination', help='Simple paramenter')
    args = parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.NOTSET)

    logger.info("Started")

    session = HTMLSession()

    r = session.get('https://krpano.com/docu/xml/')

    page = r.html.find('.selflink')

    for p in page: print(p.text)

    logger.info('EOL')

if __name__ == '__main__':
    main()
