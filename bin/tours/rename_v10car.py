#!/usr/bin/env python3

import argparse
import fileinput
import glob
import logging
import os
from os.path import expanduser
import colorlog

class readabledir(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir = values
        setattr(namespace, self.dest, prospective_dir)

def rename_item(path, item1, item2):
    if not os.path.exists(os.path.join(path, item1)):
        logging.warning(os.path.join(path, item1) + ' cannot be found')
    else:
        logging.info(path + '/' + item1 + ' -> ' + item2)
        os.rename(os.path.join(path, item1), os.path.join(path, item2))

def replace_str(filepath, str1, str2):
    if not os.path.exists(filepath):
        logging.warning(filepath + ' cannot be found')
    else:
        logging.info(filepath)
        with fileinput.FileInput(filepath, inplace=True) as file:
            for line in file:
                print(line.replace(str1, str2), end='')

def main():
    # Use argparse to supply 'origin' and 'destination' of the car to rename
    parser = argparse.ArgumentParser(
        description='Rename a car and all the necessary files in the folders \
        import, layers, masks, panos and the virtual tours themselver.')
    parser.add_argument(
        '-o', '--origin', action=readabledir, dest='origin', help='Name of the car to be renamed')
    parser.add_argument('-d', '--destination', dest='destination', help='New name')
    args = parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.INFO)

    logger.info("Started")

    name1 = args.origin
    name2 = args.destination

    if os.name == 'nt':
        rootdir = os.path.join('E:\\', 'virtual_tours', 'gforces')
    else:
        rootdir = os.path.join(os.path.join(expanduser('~')), 'virtual-tours', 'gforces')

    # Folder .src/import/###.jpg
    path = os.path.join(rootdir, 'cars', '.src', 'import')
    item1 = name1 + '.jpg'
    item2 = name2 + '.jpg'
    rename_item(path, item1, item2)

    # Folder .src/layers/###.psb
    path = os.path.join(rootdir, 'cars', '.src', 'layers')
    item1 = name1 + '.psb'
    item2 = name2 + '.psb'
    rename_item(path, item1, item2)

    # Folder .src/masks/###.psb
    path = os.path.join(rootdir, 'cars', '.src', 'masks')
    item1 = name1 + '.psb'
    item2 = name2 + '.psb'
    rename_item(path, item1, item2)

    # Folder .src/panos/###
    path = os.path.join(rootdir, 'cars', '.src', 'panos')
    item1 = name1
    item2 = name2
    rename_item(path, item1, item2)

    # Folder ./###
    path = os.path.join(rootdir, 'cars')
    item1 = name1
    item2 = name2
    rename_item(path, item1, item2)

    # Folder /media/e/virtual_tours/gforces/html/list/latest.html
    filepath = os.path.join(rootdir, 'html', 'list', 'latest.html')
    str1 = name1
    str2 = name2
    replace_str(filepath, str1, str2)

    # File ./###/files/tour.xml
    filepath = os.path.join(rootdir, 'cars', name2, 'files', 'tour.xml')
    str1 = name1
    str2 = name2
    replace_str(filepath, str1, str2)

    # File ./###/files/content/index.xml
    filepath = os.path.join(rootdir, 'cars', name2, 'files', 'content', 'index.xml')
    str1 = name1
    str2 = name2
    replace_str(filepath, str1, str2)

    # File ./###/files/scenes/*.xml
    filepath = os.path.join(rootdir, 'cars', name2, 'files', 'scenes')
    str1 = name1
    str2 = name2
    scenesdir = glob.glob(os.path.join(filepath, '*.xml'))
    for xmlfile in scenesdir:
        filepath = xmlfile
        replace_str(filepath, str1, str2)

    logger.warning(
        'Open .src/layers/' + name2 + '.psd and manually change the Background Layer name')
    logger.info('EOL')

if __name__ == '__main__':
    main()
