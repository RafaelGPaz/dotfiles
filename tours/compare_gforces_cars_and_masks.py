#!/usr/bin/env python3

import argparse
import colorlog
import logging
import glob
import os

def getbasename(name):
    iname = os.path.basename(name)
    ibasename = os.path.splitext(iname)[0]
    return ibasename

def main():
    # Use argparse to supply 'origin' and 'destination' of the car to rename
    parser = argparse.ArgumentParser(description='Compares files in .src/panos/ and .src/masks/ to make sure each car has its corresponding mask file.')
    # parser.add_argument('-o', '--origin', action=readable_dir, dest='origin', help='Name of the car to be renamed')
    # parser.add_argument('-d', '--destination', dest='destination', help='New name')
    args = parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.INFO)

    logger.info("Started")

    importFolder = '//media//e//virtual_tours//gforces//cars//.src//import'
    masksFolder = '//media//e//virtual_tours//gforces//cars//.src//masks'

    allimports = []
    imports = glob.glob(importFolder + '/*.jpg')
    for item in imports:
        newitem = getbasename(item)
        allimports.append(newitem)

    allmasks = []
    masks = glob.glob(masksFolder + '/*.psb')
    for item in masks:
        newitem = getbasename(item)
        allmasks.append(newitem)

    comparation1 = set(allmasks).difference(allimports)
    comparation2 = set(allimports).difference(allmasks)

    logger.info('No of items in IMPORT folder -------------> ' +  str(len(allimports)))
    logger.info('No of items in MASKS folder --------------> ' +  str(len(allmasks)))

    for missing1 in comparation1:
        logger.warn('Items missing in IMPORT folder: ' + missing1 + '.jpg')

    for missing2 in comparation1:
        logger.warn('Items missing in MASKS folder: ' + missing2 + '.psb')

    if not comparation1 and not comparation2:
        logger.info('All OK!!!')

    logger.info('EOL')

if __name__ == '__main__':
    main()
