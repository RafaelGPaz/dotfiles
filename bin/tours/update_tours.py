#!/usr/bin/env python3

import argparse
import logging
import colorlog
import os
import shutil
import fileinput
import sys
from distutils.dir_util import copy_tree

def main():
    # Add description
    parser = argparse.ArgumentParser(description='It copies all the files from the first virtual tour folder to the others')
    # parser = argparse.ArgumentParser(description='Description')
    # parser.add_argument('-o', '--origin', action=readable_dir, dest='origin', help='Parameter which autocomplete directories')
    # parser.add_argument('-d', '--destination', dest='destination', help='Simple paramenter')
    parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s',
        log_colors={
            'DEBUG': 'green',
            'INFO': 'cyan'
        }))

    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.NOTSET)

    logger.info("Started")

    # List all directories excluding files starting with '.' or 'shared'
    alltours = []
    bad_folders = ['shared']
    root = os.getcwd()

    for tour in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(root, tour)):
            if not tour.startswith('.'):
                if not any(bad_folder in tour for bad_folder in bad_folders):
                    alltours.append(tour)
    alltours.sort(reverse=False)

    first_tour = alltours[0]
    alltours.remove(first_tour)

    devel_html_orig = os.path.join(root, first_tour, "devel.html")
    index_html_orig = os.path.join(root, first_tour, "index.html")
    devel_xml_orig = os.path.join(root, first_tour, "files" ,"devel.xml")
    en_xml_orig = os.path.join(root, first_tour, "files" ,"en.xml")
    content_dir_orig = os.path.join(root, first_tour, "files", "content")

    logger.info('First Tour: ' + first_tour)

    for item in alltours:
        logger.info("[TOUR] " + item)

        # interior.html
        # This script expects that 'index.html' is a virtual tour.
        # In tours that support languages, 'index.html' is a list, not a tour.
        # This will create wrong 'index.html' files in the rest of the tours, so the script needs to be stoped.
        # TODO: Find a workorund to use interior.html instead of index.html if it exists
        interior_html = os.path.join(root, item, "interior.html")
        if os.path.exists(interior_html):
            logger.critical("ERROR")
            sys.exit("The first tour contains a file name 'interior.html' which brakes this script")

        # index.html
        index_html_dest = os.path.join(root, item, "index.html")
        testing = "0"
        with open(index_html_orig, "rt") as fin:
            with open(index_html_dest, "wt") as fout:
                for line in fin:
                    if (first_tour in line) and (testing == "0"):
                        testing = "1"
                    fout.write(line.replace(first_tour, item))

        if(testing == "0"):
            logger.critical("ERROR")
            sys.exit("Tour name doesn't match. Check 'index.html' and 'content/index.xml' files")
        else:
            logger.info("[ -- ] index.html")

         # devel.html
        devel_html_dest = os.path.join(root, item, "devel.html")
        shutil.copyfile(devel_html_orig, devel_html_dest)
        logger.info("[ -- ] devel.html")

         # devel.xml
        devel_xml_dest = os.path.join(root, item, "files", "devel.xml")
        shutil.copyfile(devel_xml_orig, devel_xml_dest)
        logger.info("[ -- ] files/devel.xml")

        # en.xml
        if os.path.exists(en_xml_orig):
           tour_xml_dest = os.path.join(root, item, "files","tour.xml")
           en_xml_dest = os.path.join(root, item, "files","en.xml")
           shutil.copyfile(tour_xml_dest, en_xml_dest)
           logger.info("[ -- ] files/en.xml")

        # content/ directory if it doesn't exists
        content_dir_dest = os.path.join(root, item, "files", "content")
        if not os.path.exists(content_dir_dest):
            copy_tree(content_dir_orig, content_dir_dest)
            logger.info("[ -- ] files/content/")


        logger.info("[ OK ]")


    logger.info('[DONE]')

if __name__ == '__main__':
    main()
