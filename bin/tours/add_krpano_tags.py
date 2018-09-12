#!/usr/bin/env python3

import argparse
import glob
import logging
import os

import colorlog


def main():
    # Add description
    parser = argparse.ArgumentParser(description='Description')
    # parser.add_argument('-o', '--origin', action=readable_dir, dest='origin', help='Parameter which autocomplete directories')
    # parser.add_argument('-d', '--destination', dest='destination', help='Simple paramenter')
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
    panosdir = os.path.join(os.getcwd())
    allitems = []
    tours = sorted(glob.glob(panosdir + '/*'))
    bad_words = ['<krpano', '</krpano']
    for item in tours:
        if os.path.isdir(item):
            scenesdir = os.path.join(item, 'files', 'scenes')
            if(os.path.exists(scenesdir)):
                allitems.append(item)

    for tourdir in allitems:
        logger.info(' ' + os.path.basename(tourdir))
        scenesdir = os.path.join(tourdir, 'files', 'scenes')
        xmlfiles= glob.glob(scenesdir + '/*.xml')
        for xmlfile in xmlfiles:
            xmlfilebck = os.path.join(scenesdir) + '/xml_bck.txt'
            with open(xmlfile, encoding='utf-8-sig') as oldfile, open(xmlfilebck, 'w', encoding='utf-8') as newfile:
                newfile.writelines('<krpano>\n')
                for line in oldfile:
                    if not any(bad_word in line for bad_word in bad_words):
                        newfile.write(line)
                newfile.writelines("</krpano>")
            os.rename(xmlfilebck, xmlfile)
            if(os.path.exists(xmlfilebck)):
                os.remove(xmlfilebck)
            logger.info('   • ' + os.path.basename(xmlfile))

    logger.info('EOL')

if __name__ == '__main__':
    main()
