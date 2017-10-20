#!/usr/bin/env python

import argparse
import fileinput
import glob
import logging
import os
import shutil
import colorlog
from usefulfunctions import safeRm

def main():
    parser = argparse.ArgumentParser(description='Merges all the XML files into \
    "tour.xm" and creates a new "en.xml" file if it already exists.')
    args = parser.parse_args()

    logger = colorlog.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(
        colorlog.ColoredFormatter('%(log_color)s%(levelname)s:%(message)s'))
    logger.addHandler(handler)

    logger.info("Started")

    alltours = []
    allxmlfiles = []
    bad_words = ['<krpano', '</krpano>', '<krpano version', 'coordfinder']

    for tour in os.listdir(os.getcwd()):
        if not tour.startswith('.'):
            alltours.append(tour)

    for tour in alltours:
        logger.info("Tour: " + os.path.basename(tour))
        # Find all XML files recursively
        xmlfiles = glob.glob(tour + "\\files\\**\\*.xml", recursive=True)

        # Remove unwanted XML files
        for item in xmlfiles:
            if "devel.xml" not in item and "tour.xml" not in item and "_design_" not in item and "en.xml" not in item  and "ar" not in item:
                allxmlfiles.append(item)
                logger.debug('[ -- ] ' + item)
                # TO DO: Add line to apend vtourskin at first
        allxmlfiles.sort(reverse=False)

        # Merge files into tour.xml
        tourxml = tour + '\\files\\tour.xml'
        enxml = tour + '\\files\\en.xml'
        safeRm(tourxml)
        with open(tourxml, 'w', encoding='utf-8') as outfile:
            outfile.writelines('<?xml version="1.0" encoding="UTF-8"?>\n<krpano version="1.19">\n')
            for line in fileinput.input(allxmlfiles, mode="rU", openhook=fileinput.hook_encoded("utf-8-sig")):
                if not any(bad_word in line for bad_word in bad_words):
                    if line.rstrip():
                        outfile.write(line)
            outfile.writelines("</krpano>")
        logger.info('[ OK ] ' + tourxml)
        if os.path.isfile(enxml):
            shutil.copyfile(tourxml,enxml)
            logging.info('[ OK ] ' + enxml)
        allxmlfiles = []

    logger.info("_EOF_")

if __name__ == '__main__':
    main()
