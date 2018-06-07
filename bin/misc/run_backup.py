#!/usr/bin/env python3

import argparse
import logging
import subprocess

import colorlog


def main():
    # Add description
    parser = argparse.ArgumentParser(description='Run backup for Mac and the white hard drive using Free File Sync')
    parser.add_argument('-a', '--all', dest='backupall', help='Makes a full backup')
    parser.add_argument('-mi', '--macimg', dest='macimg', help='Makes an Image Backup of the Mac')
    parser.add_argument('-mp', '--macplus', dest='macplus', help='Makes an Incremental Backup of the Mac')
    parser.add_argument('-ei', '--extraimg', dest='extraimg', help='Makes an Image Backup of the white hard drive')
    parser.add_argument('-ep', '--extraplus', dest='extraplus', help='Makes an Incremental Backup of the white hard drive')
    args = parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s',
        log_colors={
            'DEBUG': 'green',
            'INFO': 'cyan'
        }))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.INFO)

    logger.info("Started")

    # Things to backup

    # Mac IMG
    if args.macimg == True:
            subprocess.call(krcall, stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT)


    # Mac PLUS

    # Extra IMG

    # Extra Plus ?

    logger.info('EOL')

if __name__ == '__main__':
    main()
