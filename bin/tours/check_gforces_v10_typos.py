#!/usr/bin/env python

# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import argparse
import glob
import logging
import os
import sys
import xml.etree.ElementTree as ET

import colorlog


def main():

    # def checkSceneXml(xmlPathMulti):
    #     print(xmlPath)
    #     tree = ET.parse(xmlPath)
    #     root = tree.getroot()
    #     for carName in root.findall('scene'):
    #         sceneName = carName.get('name')
    #        print(sceneName)

    def checkSceneXml(xmlPath, carBasename):
        # print(xmlPath)
        tree = ET.parse(xmlPath)
        root = tree.getroot()
        for carName in root.iter('scene'):
            sceneNameXml =(carName.get('name'))
            if sceneNameXml != carBasename:
                # print(xmlPath + ' >>> OK')
            # else:
                logger.info('Typo in file: ' + xmlPath)
                logger.info('    XML : ' + sceneNameXml)
                logger.info('    HTML: ' + carBasename)
            # return returnName
            #print(sceneName)

    # Add description
    parser = argparse.ArgumentParser(description='Description')
    # parser.add_argument('-o', '--origin', action=readable_dir, dest='origin', help='Parameter which autocomplete directories')
    # parser.add_argument('-d', '--destination', dest='destination', help='Simple paramenter')
    args = parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.NOTSET)

    logger.info("Started")

    # List all gb_* folders

    tours = sorted(glob.glob('/Users/rafael/virtual-tours/gforces/cars/gb_*'))
    for item in tours:
        itemBasename = os.path.basename(item)

        # For each gb_folder search for the file files/scenes/scene.xml and scene_1_a.xml
        tourXml = os.path.join(item, 'files', 'tour.xml')
        sceneFile = os.path.join(item, 'files', 'scenes', 'scene.xml')
        sceneFileAlt = os.path.join(item, 'files', 'scenes', 'scene_1_a.xml')
        sceneFileOne = os.path.join(item, 'files', 'scenes', 'scene1.xml')
        develHtml = os.path.join(item, 'devel.html')
        if os.path.exists(sceneFile):
            sceneXml = sceneFile
            checkSceneXml(sceneXml, itemBasename)
            # print(checkSceneXml(sceneXml))
        else:
            if os.path.exists(sceneFileAlt):
                sceneXml = sceneFileAlt
                checkSceneXml(sceneXml, itemBasename)
            elif os.path.exists(sceneFileOne):
                sceneXml = sceneFileOne
                checkSceneXml(sceneXml, itemBasename)
            else:
                if os.path.exists(develHtml):
                    sys.exit('Error: ' + item)



    # In XML FILE, Get <scene name> attribute

    # If basename is equal sceneName OK, else throw error

    logger.info('EOL')

if __name__ == '__main__':
    main()
