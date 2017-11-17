#!/usr/bin/env python3

import argparse
import fileinput
import glob
import logging
import os
import colorlog
import shutil

class readabledir(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir = values
        setattr(namespace, self.dest, prospective_dir)

def new_file(item):
    logging.info('Touch -> ' + item)
    try:
        open(item, 'x')
    except FileExistsError:
        pass

def replace_str(filepath, str1, str2):
    if not os.path.exists(filepath):
        logging.warning(filepath + ' cannot be found')
    else:
        logging.info('Replace STR ->' + filepath)
        with fileinput.FileInput(filepath, inplace=True) as file:
            for line in file:
                print(line.replace(str1, str2), end='')

def main():
    # Use argparse to supply 'origin' and 'destination' of the car to rename
    parser = argparse.ArgumentParser(
        description='Duplicate a car and all the necessary files in the folders \
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
        rootdir = os.path.join('/media', 'e', 'virtual_tours', 'gforces')

    # File .src/import/###.jpg
    path = os.path.join(rootdir, 'cars', '.src', 'import')
    item = path + '\\' + name2 + '.jpg'
    new_file(item)

    # File .src/layers/###.psb
    path = os.path.join(rootdir, 'cars', '.src', 'layers')
    item = path + '\\' + name2 + '.psb'
    new_file(item)

    # File .src/masks/###.psb
    path = os.path.join(rootdir, 'cars', '.src', 'masks')
    item = path + '\\' + name2 + '.psb'
    new_file(item)

    # Folder .src/panos/###
    path = os.path.join(rootdir, 'cars', '.src', 'panos')
    item = path + '\\' + name2
    logging.info('New Folder ->' + item)

    if not os.path.exists(item):
        os.makedirs(item)

    # Folder .src/panos/scene_#_#.jpg
    item1 = path + '\\' + name2 + '\\scene_1_a.jpg'
    item2 = path + '\\' + name2 + '\\scene_1_b.jpg'
    item3 = path + '\\' + name2 + '\\scene_1_c.jpg'
    item4 = path + '\\' + name2 + '\\scene_2_a.jpg'
    item5 = path + '\\' + name2 + '\\scene_2_b.jpg'
    item6 = path + '\\' + name2 + '\\scene_2_c.jpg'
    new_file(item1)
    new_file(item2)
    new_file(item3)
    new_file(item4)
    new_file(item5)
    new_file(item6)

    # Folder ./###
    item1 = os.path.join(rootdir, 'cars', name1)
    item2 = os.path.join(rootdir, 'cars', name2)
    # Delete the folder for the new car if it alreday exists
    if os.path.exists(item2):
        logging.info('Remove -> ' + item2)
        shutil.rmtree(item2)
    # duplicate folder  folder
    logging.info('Copy -> ' + item1 + ' -> ' + item2)
    shutil.copytree(item1, item2)

    # File ./###/index.html
    filepath = os.path.join(rootdir, 'cars', name2, 'index.html')
    str1 = name1
    str2 = name2
    replace_str(filepath, str1, str2)

    # File ./###/devel.html
    filepath = os.path.join(rootdir, 'cars', name2, 'devel.html')
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
    scenesdir = glob.glob(filepath + '\\*.xml')
    for xmlfile in scenesdir:
        filepath = xmlfile
        replace_str(filepath, str1, str2)

    logger.info('EOL')

if __name__ == '__main__':
    main()