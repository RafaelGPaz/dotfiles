#!/usr/bin/env python3

import argparse
import logging
import os

import colorlog
import requests


def main():

    def check_url(carname, filename):
        underscores = carname.split('_')
        brand = underscores[1]
        server = 'https://s3-eu-west-1.amazonaws.com/autofs/shared/interiors/projects/'
        url = server + brand + '_manufacturer/' + \
            carname + '/files/' + filename + '.xml'
        request = requests.get(url)
        if request.status_code == 200:
            logger.info('[ OK ] ' + filename + '.xml')
        else:
            logger.warning('Missing ' + filename + '.xml')

    parser = argparse.ArgumentParser(description='For each car folder in the current directory, it \
    checks which language XML files are in the server.')

    parser.add_argument(dest='language', type=str,
                        const='all', nargs='?', default='all',
                        help='Enter the name of an specific XML file without the extension')

    args = parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s',
        log_colors={
            'DEBUG': 'green',
            'WARNING': 'red',
            'INFO': 'cyan'
        }))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.INFO)

    logger.info("Started")
    alltours = []
    allfiles = ['ar', 'de', 'en', 'en_us', 'it', 'nl', 'sk']
    bad_folders = ['shared']
    for tour in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), tour)):
            if not tour.startswith('.'):
                if not any(bad_folder in tour for bad_folder in bad_folders):
                    alltours.append(tour)
    alltours.sort(reverse=False)

    for tour in alltours:
        carname = os.path.basename(tour)
        logger.info("Tour: " + carname)

        if args.language == 'all':
            for file in allfiles:
                check_url(carname, file)
        else:
            check_url(carname, args.language)

    logger.info("_EOF_")


if __name__ == '__main__':
    main()
