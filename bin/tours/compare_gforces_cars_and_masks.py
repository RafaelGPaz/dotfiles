#!/usr/bin/env python3

import argparse
import logging
import glob
import os
import colorlog

def getbasename(name):
    iname = os.path.basename(name)
    ibasename = os.path.splitext(iname)[0]
    return ibasename

def main():
    parser = argparse.ArgumentParser(description='Compares files in .src/import/ and \
    .src/masks/ to make sure each car has its corresponding mask file.')

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.INFO)

    logger.info("Started")

    importfolder = os.path.join('/', 'Users', 'rafael', 'virtual-tours', 'gforces', 'cars',\
     '.src', 'import')
    masksfolder = os.path.join('/', 'Users', 'rafael', 'virtual-tours', 'gforces', 'cars',\
     '.src', 'masks')

    allimports = []
    imports = glob.glob(importfolder + '/*.jpg')
    for item in imports:
        newitem = getbasename(item)
        allimports.append(newitem)

    allmasks = []
    masks = glob.glob(masksfolder + '/*.psb')
    for item in masks:
        newitem = getbasename(item)
        allmasks.append(newitem)

    comparation1 = set(allmasks).difference(allimports)
    comparation2 = set(allimports).difference(allmasks)

    logger.info('No of items in IMPORT folder -------------> ' +  str(len(allimports)))
    logger.info('No of items in MASKS folder --------------> ' +  str(len(allmasks)))

    for missing1 in comparation1:
        logger.info('Items missing in IMPORT folder: ' + missing1 + '.jpg')

    for missing2 in comparation2:
        logger.info('Items missing in MASKS folder: ' + missing2 + '.psb')

    if not comparation1 and not comparation2:
        logger.info('All OK!!!')

    logger.info('EOL')

if __name__ == '__main__':
    main()
