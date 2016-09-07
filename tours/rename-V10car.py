#!/usr/bin/env python3
import argparse
import colorlog
import fileinput
import glob
import logging
import os

class readable_dir(argparse.Action):
    def __call__(self,parser, namespace, values, option_string=None):
        prospective_dir=values
        setattr(namespace,self.dest,prospective_dir)

def rename_item(path, item1, item2):
    if not os.path.exists(path + item1):
        logging.warn(path + item1 + ' cannot be found')
    else:
        logging.info(path + item1 + ' -> ' + item2)
        os.rename(path + item1,path + item2)

def replace_str(filePath, str1, str2):
    if not os.path.exists(filePath):
        logging.warn(filePath + ' cannot be found')
    else:
        logging.info(filePath)
        with fileinput.FileInput(filePath, inplace=True) as file:
            for line in file:
                print(line.replace(str1,str2), end='')

def main():
    # Use argparse to supply 'origin' and 'destination' of the car to rename
    parser = argparse.ArgumentParser(description='Rename a car and all the necessary files in the folders import, layers, masks, panos and the virtual tours themselver.')
    parser.add_argument('-o', '--origin', action=readable_dir, dest='origin', help='Name of the car to be renamed')
    parser.add_argument('-d', '--destination', dest='destination', help='New name')
    args = parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.INFO)

    logger.info("Started")

    name1=args.origin
    name2=args.destination

    # Folder .src/import/###.jpg
    path = '.src/import/'
    item1 = name1 + '.jpg'
    item2 = name2 + '.jpg'
    rename_item(path, item1, item2)

    # Folder .src/layers/###.psb
    path = '.src/layers/'
    item1 = name1 + '.psb'
    item2 = name2 + '.psb'
    rename_item(path, item1, item2)

    # Folder .src/masks/###.psb
    path = '.src/masks/'
    item1 = name1 + '.psb'
    item2 = name2 + '.psb'
    rename_item(path, item1, item2)

    # Folder .src/panos/###
    path = '.src/panos/'
    item1 = name1
    item2 = name2
    rename_item(path, item1, item2)

    # Folder ./###
    path = './'
    item1 = name1
    item2 = name2
    rename_item(path, item1, item2)

    # File ./###/files/tour.xml
    filepath = './' + name2 + '/files/tour.xml'
    str1 = name1
    str2 = name2
    replace_str(filepath, str1, str2)

    # File ./###/files/content/index.xml
    filepath = './' + name2 + '/files/content/index.xml'
    str1 = name1
    str2 = name2
    replace_str(filepath, str1, str2)

    # File ./###/files/scenes/*.xml
    str1 = name1
    str2 = name2
    scenesDir = glob.glob('./' + name2 + '/files/scenes/*.xml')
    for xmlFile in scenesDir:
        filepath = xmlFile
        replace_str(filepath, str1, str2)

    logger.warn('Open .src/layers/' + name2 + '.psd and manually change the Background Layer name')
    logger.info('EOL')

if __name__ == '__main__':
    main()
