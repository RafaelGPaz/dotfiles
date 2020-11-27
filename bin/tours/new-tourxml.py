#!/usr/bin/env python

import argparse
import fileinput
import glob
import logging
import os
import shutil

import colorlog

from usefulfunctions import numericalSort, safeRm


def main():
    parser = argparse.ArgumentParser(description='Merges all the XML files into \
    "tour.xm". It also creates languages XML files if they already exists, or if \
    it is secified in the arguments')
    parser.add_argument('-a', action='store_true', dest='arxmlfile', \
                              default=False, help='Create ar.xml file')
    parser.add_argument('-d', action='store_true', dest='dexmlfile', \
                              default=False, help='Create de.xml file')
    parser.add_argument('-e', action='store_true', dest='enxmlfile', \
                              default=False, help='Create en.xml file')
    parser.add_argument('-i', action='store_true', dest='itxmlfile', \
                              default=False, help='Create it.xml file')
    parser.add_argument('-n', action='store_true', dest='nlxmlfile', \
                              default=False, help='Create nl.xml file')
    parser.add_argument('-s', action='store_true', dest='skxmlfile', \
                              default=False, help='Create sk.xml file')

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
    bad_files = ['coordfinder', 'editor_and_options','toolbox']
    shared_dir = os.path.join(os.getcwd(), "shared")
    plugins_dir = os.path.join(shared_dir, "plugins")
    include_dir = ''.join(glob.glob(os.path.join(shared_dir, "include*")))
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
        enxml = os.path.join(tour, 'files' ,'en.xml')
        enusxml = os.path.join(tour, 'files' ,'en_us.xml')
        arxml = os.path.join(tour, 'files' ,'ar.xml')
        itxml = os.path.join(tour, 'files' ,'it.xml')
        nlxml = os.path.join(tour, 'files' ,'nl.xml')
        skxml = os.path.join(tour, 'files' ,'sk.xml')
        dexml = os.path.join(tour, 'files' ,'de.xml')
        safeRm(tourxml)
        with open(tourxml, 'w', encoding='utf-8') as outfile:
            outfile.writelines('<?xml version="1.0" encoding="UTF-8"?>\n<krpano version="1.19">\n')
            for line in fileinput.input(allxmlfiles, mode="rU", openhook=fileinput.hook_encoded("utf-8-sig")):
                if not any(bad_word in line for bad_word in bad_words):
                    if line.rstrip():
                        outfile.write(line)
            outfile.writelines("</krpano>")
        logger.info('[ OK ] ' + tourxml)
        if (os.path.isfile(enxml)) or (os.path.isfile(enusxml)) or (args.enxmlfile == True):
            shutil.copyfile(tourxml,enxml)
            shutil.copyfile(tourxml,enusxml)
            logger.info('[ OK ] ' + enxml)
            logger.info('[ OK ] ' + enusxml)
        if (os.path.isfile(arxml)) or (args.arxmlfile == True):
            shutil.copyfile(tourxml,arxml)
            for linenum,line in enumerate( fileinput.FileInput(arxml,inplace=1) ):
                if linenum==2 :
                    print('    <config arab="true" />')
                    print(line.rstrip())
                else:
                    print(line.rstrip())
            logger.info('[ OK ] ' + arxml)
        if (os.path.isfile(itxml)) or (args.itxmlfile == True):
            shutil.copyfile(tourxml,itxml)
            for linenum,line in enumerate( fileinput.FileInput(itxml,inplace=1) ):
                if linenum==2 :
                    print('    <config italian="true" />')
                    print(line.rstrip())
                else:
                    print(line.rstrip())
            logger.info('[ OK ] ' + itxml)
        if (os.path.isfile(nlxml)) or (args.nlxmlfile == True):
            shutil.copyfile(tourxml,nlxml)
            for linenum,line in enumerate( fileinput.FileInput(nlxml,inplace=1) ):
                if linenum==2 :
                    print('    <config dutch="true" />')
                    print(line.rstrip())
                else:
                    print(line.rstrip())
            logger.info('[ OK ] ' + nlxml)
        if (os.path.isfile(skxml)) or (args.skxmlfile == True):
            shutil.copyfile(tourxml,skxml)
            for linenum,line in enumerate( fileinput.FileInput(skxml,inplace=1) ):
                if linenum==2 :
                    print('    <config slovakian="true" />')
                    print(line.rstrip())
                else:
                    print(line.rstrip())
            logger.info('[ OK ] ' + skxml)
        if (os.path.isfile(dexml)) or (args.dexmlfile == True):
            shutil.copyfile(tourxml,dexml)
            for linenum,line in enumerate( fileinput.FileInput(dexml,inplace=1) ):
                if linenum==2 :
                    print('    <config german="true" />')
                    print(line.rstrip())
                else:
                    print(line.rstrip())
            logger.info('[ OK ] ' + dexml)

        allxmlfiles = []

    logger.info("_EOF_")

if __name__ == '__main__':
    main()
