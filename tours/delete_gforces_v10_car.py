#!/usr/bin/env python3

import argparse
import colorlog
import logging
from usefulfunctions import query_yes_no

class readable_dir(argparse.Action):
    def __call__(self,parser, namespace, values, option_string=None):
        prospective_dir=values
        setattr(namespace,self.dest,prospective_dir)

def main():
    # Add description
    parser = argparse.ArgumentParser(description='Deletes the specified virtual tour folder and the panoramas in the .SRC/PANOS folder')
    parser.add_argument('-c', '--carname', action=readable_dir, dest='carname', help='Car name to be deleted')
    args = parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.INFO)

    name1=args.carname

    logger.info("Started")

    message = 'Are you sure you want to delete: ' + name1 + '?'

    if query_yes_no(message) == True:
        webvr = "yes"
    else:
        webvr = "no"

    tourpath = '//media/e//virtual_tours//gforces//cars//' + name1
    panospath = '//media/e//virtual_tours//gforces//.src//panos//' + name1

    # print(tourpath)
    # print(panospath)

    os.remove(tourpath)
    os.remove(panospath)

    logger.info('EOL')

if __name__ == '__main__':
    main()
