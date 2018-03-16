#!/usr/bin/env python

import argparse
import fileinput
import glob
import logging
import os
import shutil
import colorlog
from usefulfunctions import safeRm
from usefulfunctions import numericalSort

def main():
    parser = argparse.ArgumentParser(description='Merges all the XML files into \
    "tour.xm" and creates a new "en.xml" file if it already exists.')
    parser.add_argument('-e', action='store_false', dest='enxmlfile', \
                              default=False, help='Create en.xml file')
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
    alltours = []
    bad_words = ['<krpano', '</krpano>', '<krpano version', 'coordfinder']
    bad_folders = ['shared']
    bad_files = ['coordfinder', 'editor_and_options']
    shared_dir = ''.join(glob.glob(os.path.join(os.getcwd(), "shared*")))
    for tour in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), tour)):
            if not tour.startswith('.'):
                if not any(bad_folder in tour for bad_folder in bad_folders):
                    alltours.append(tour)
    alltours.sort(reverse=False)

    for tour in alltours:
        logger.info("Tour: " + os.path.basename(tour))
        allxmlfiles = []
        # XML files inside content/ folder
        contentxmlfiles = sorted(glob.glob(tour + "/files/content/*.xml", recursive=True))
        for item in contentxmlfiles:
            allxmlfiles.append(item)
            logger.info('[ -- ] ' + os.path.relpath(item,os.getcwd()))

        # XML files inside include/ folder
        if os.path.exists(shared_dir):
            sharedxmlfiles = sorted(glob.glob(shared_dir + "/include/**/*.xml", recursive=True))
        else:
            sharedxmlfiles = sorted(glob.glob(tour + "/files/include/**/*.xml", recursive=True))
        for item in sharedxmlfiles:
            if not any(bad_file in item for bad_file in bad_files):
                allxmlfiles.append(item)
                logger.info('[ -- ] ' + os.path.relpath(item,os.getcwd()))

        # XML files inside scenes/ folder
        scenesxmlfiles = sorted(glob.glob(tour + "/files/scenes/*.xml", recursive=True), key=numericalSort)
        for item in scenesxmlfiles:
            allxmlfiles.append(item)
            logger.info('[ -- ] ' + os.path.relpath(item,os.getcwd()))

        # Merge files into tour.xml
        tourxml = os.path.join(tour, 'files', 'tour.xml')
        enxml = os.path.join(tour, 'files' ,'en.xml')
        safeRm(tourxml)
        with open(tourxml, 'w', encoding='utf-8') as outfile:
            outfile.writelines('<?xml version="1.0" encoding="UTF-8"?>\n<krpano version="1.19">\n')
            for line in fileinput.input(allxmlfiles, mode="rU", openhook=fileinput.hook_encoded("utf-8-sig")):
                if not any(bad_word in line for bad_word in bad_words):
                    if line.rstrip():
                        outfile.write(line)
            outfile.writelines("</krpano>")
        logger.info('[ OK ] ' + tourxml)
        if (os.path.isfile(enxml)) or (args.enxmlfile == True):
            shutil.copyfile(tourxml,enxml)
            logger.info('[ OK ] ' + enxml)
        allxmlfiles = []

    logger.info("_EOF_")

if __name__ == '__main__':
    main()
