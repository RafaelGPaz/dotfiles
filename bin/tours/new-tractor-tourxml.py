#!/usr/bin/env python

import argparse
import fileinput
import glob
import logging
import os
import shutil
import sys

import colorlog

from usefulfunctions import numericalSort, safeRm


def main():
    parser = argparse.ArgumentParser(description='Merges all the XML files into \
    "tour.xml"')
    parser.add_argument('-a', action='store_true', dest='alltractors', \
                              default=False, help='Create tour.xml files for all tractors')

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
    bad_folders = ['shared', '.DS_Store', 'files']
    bad_files = ['coordfinder', 'editor_and_options']
    shared_dir_here = os.path.join(os.getcwd(), "shared")
    shared_dir_prev = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), "shared")
    if os.path.exists(shared_dir_here):
        shared_dir = shared_dir_here
        all_tractors = True
    else:
        if os.path.exists(shared_dir_prev):
            shared_dir = shared_dir_prev
            all_tractors = False
        else:
            sys.exit(['You are not in the righ directory'])

    # shared_dir_abs = os.path.join(os.path.expanduser("~"), "virtual-tours", "tractor-media", "shared")
    plugins_dir = os.path.join(shared_dir, "plugins")
    include_dir = ''.join(glob.glob(os.path.join(shared_dir, "include")))

    if all_tractors:
        for brand in os.listdir(os.getcwd()):
            if (brand not in bad_folders):
                for tour in os.listdir(os.path.join(os.getcwd() ,brand)):
                    tour_path = os.path.join(os.getcwd(), brand, tour)
                    if os.path.isdir(tour_path):
                        if not tour.startswith('.'):
                            tour = os.path.join(os.getcwd(), brand, tour)
                            alltours.append(tour)
    else:
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

        # XML files inside plugins/ folder
        if os.path.exists(shared_dir):
            pluginsxmlfiles = sorted(glob.glob(plugins_dir + "/*.xml", recursive=True))
        else:
            pluginsxmlfiles = sorted(glob.glob(tour + "/files/plugins/*.xml", recursive=True))
        for item in pluginsxmlfiles:
                allxmlfiles.append(item)
                logger.info('[ -- ] ' + os.path.relpath(item,os.getcwd()))

        # XML files inside include/ folder
        if (os.path.exists(shared_dir)) and (os.path.exists(include_dir)):
            sharedxmlfiles = sorted(glob.glob(include_dir + "/**/*.xml", recursive=True))
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
        safeRm(tourxml)
        with open(tourxml, 'w', encoding='utf-8') as outfile:
            outfile.writelines('<?xml version="1.0" encoding="UTF-8"?>\n<krpano version="1.19">\n')
            for line in fileinput.input(allxmlfiles, mode="rU", openhook=fileinput.hook_encoded("utf-8-sig")):
                if not any(bad_word in line for bad_word in bad_words):
                    if line.rstrip():
                        outfile.write(line)
            outfile.writelines("</krpano>")
        logger.info('[ OK ] ' + tourxml)
        allxmlfiles = []

    logger.info("_EOF_")

if __name__ == '__main__':
    main()
