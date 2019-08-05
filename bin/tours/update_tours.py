#!/usr/bin/env python3

import argparse
import fileinput
import logging
import os
import shutil
import sys
from distutils.dir_util import copy_tree

import colorlog

from bs4 import BeautifulSoup

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
            'INFO': 'cyan',
            'WARNING': 'red'
        }))

    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.NOTSET)

    logger.info("Started")

    def replace_tourname(file_orig, file_dest):
        soup = BeautifulSoup(open(file_orig), "html.parser")
        # <h4>Chevrolet Tahoe Midnight Editon 2017</h4>
        titleorig = soup.find('h4')
        # <h4>ae_chevrolet_traverse-3lt-awd_2018</h4>
        titledest = '<h4>' + os.path.basename(os.path.dirname(file_dest)) + '</h4>'
        # Name of the dest HTML file
        filename = os.path.basename(file_dest)

        testing = "0"
        with open(file_orig, "rt") as fin:
            with open(file_dest, "wt") as fout:
                for line in fin:
                    if (first_tour in line) and (testing == "0"):
                        testing = "1"
                    fout.write(line.replace(first_tour, item).replace(str(titleorig), str(titledest)))
        if(filename == 'index.html'):
            if(testing == "0"):
                logger.critical("ERROR")
                sys.exit("Tour name doesn't match. Check first car 'index.html' and 'content/index.xml' files")

        logger.info("[ -- ] " + filename)

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
    interior_html_orig = os.path.join(root, first_tour, "interior.html")
    interiordevel_html_orig = os.path.join(root, first_tour, "interiordevel.html")
    devel_xml_orig = os.path.join(root, first_tour, "files" ,"devel.xml")
    en_xml_orig = os.path.join(root, first_tour, "files" ,"en.xml")
    content_dir_orig = os.path.join(root, first_tour, "files", "content")

    logger.info('First Tour: ' + first_tour)

    for item in alltours:
        logger.info("[TOUR] " + item)

        interior_html_dest = os.path.join(root, item, "interior.html")
        interiordevel_html_dest = os.path.join(root, item, "interiordevel.html")
        scenes_path = os.path.join(root, '.src', 'panos', item )
        if os.path.isdir(scenes_path):
            numscenes = len([f for f in os.listdir(scenes_path)if os.path.isfile(os.path.join(scenes_path, f))])

        # index.html
        if not os.path.exists(interior_html_dest):
            index_html_dest = os.path.join(root, item, "index.html")
            replace_tourname(index_html_orig,index_html_dest)

         # devel.html
        if not os.path.exists(interiordevel_html_dest):
            devel_html_dest = os.path.join(root, item, "devel.html")
            replace_tourname(devel_html_orig,devel_html_dest)

         # interior.html
        if os.path.exists(interior_html_orig):
            replace_tourname(interior_html_orig,interior_html_dest)

         # interiordevel.html
        if os.path.exists(interiordevel_html_orig):
            replace_tourname(interiordevel_html_orig,interiordevel_html_dest)

         # devel.xml
         # Don't copy it if there are more than 1 scene
        if numscenes > 1:
            logger.warning("[ NO ] files/devel.xml")
        else:
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
