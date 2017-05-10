#!/usr/bin/env python3

import argparse
import colorlog
import logging
import sys
import os
import xml.etree.ElementTree as ET
import glob
import shutil
import fileinput
import subprocess
from usefulfunctions import safeRm

def main():

    def replace_first_line( src_filename, target_filename, replacement_line):
        f = open(src_filename)
        first_line, remainder = f.readline(), f.read()
        t = open(target_filename,"w")
        t.write(replacement_line + "\n")
        t.write(remainder)
        t.close()

    def allXml (fList):
        fileNames = []
        for dRoot in fList:
            for fPath in glob.glob(os.path.join(dRoot, "*.xml")):
                fileNames.append(fPath)

            dPath = [d for d in os.listdir(dRoot)]
            for subDir in dPath:
                subDirPath = os.path.join(dRoot, subDir)
                fStr = subDirPath + '**/*.xml'

                for fPath in glob.glob(fStr, recursive=True):
                    fileNames.append(fPath)

        return(fileNames)

    def addToDevel(dRoot):
        rootBsName = os.path.basename(os.path.normpath(dRoot))
        # XML files in first level
        for fPath in glob.glob(os.path.join(dRoot, "*.xml")):
            if fPath:
                fBsName = os.path.basename(fPath)
                includeUrl = '    <include url="' + rootBsName + '/' + fBsName + '" />\n'
                with open(develPath, "a") as myfile:
                    myfile.write(includeUrl)
                    # XML files in second level
        dPath = [d for d in os.listdir(dRoot)]
        for subDir in dPath:
            subDirPath = os.path.join(dRoot, subDir)
            fStr = subDirPath + '**/*.xml'
            for fPath in glob.glob(fStr, recursive=True):
                if fPath:
                    fBsName = os.path.basename(fPath)
                    includeUrl = '    <include url="' + rootBsName + '/' + subDir + '/' + fBsName + '" />\n'
                    with open(develPath, "a") as myfile:
                        myfile.write(includeUrl)

    # Script only for python3
    if sys.version_info[0] < 3:
        sys.exit('Must be using Python 3')

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
    logger.setLevel(level=logging.INFO)

    logger.info("Started")

    # Check .src/ exists
    rootDir = os.getcwd()
    srcDir = os.path.dirname('.src/')
    templatesDir = os.path.join(srcDir, 'templates/')
    staticDir = os.path.join(srcDir, 'static/')
    sceneTemplate = os.path.join(templatesDir, 'scene_template.html')
    develTemplate = os.path.join(templatesDir, 'devel_template.html')
    contentTemplate = os.path.join(templatesDir, 'content_template.xml')
    includeStatic = os.path.join(staticDir, 'include/')
    pluginsStatic = os.path.join(staticDir, 'plugins/')
    jsStatic = os.path.join(staticDir, 'tour.js')
    swfStatic = os.path.join(staticDir, 'tour.swf')
    panosDir = os.path.join(srcDir, 'panos')
    if not os.path.exists(srcDir):
        sys.exit(logger.critical("There is no '.src' directory. Are you in the right directory?"))
        # Check .src/config.xml exists
    configXml = os.path.join(srcDir, 'config.xml')
    if not os.path.exists(configXml):
        sys.exit(logger.critical("Where is config.xml?"))
        # Parse .src/config.xml
    tree = ET.parse(configXml)
    root = tree.getroot()

    brandList = []
    for brand in tree.findall('brand'):
        brandID = brand.get('id')
        brandList.append(brandID)
        logging.debug(brandID)

    logging.debug(brandList)

    carList = []
    for car in tree.findall('brand/car'):
        carID = car.get('id')
        carList.append(carID)
        logging.debug(carID)

    logging.debug(carList)

    # For each tour
    for carTour in carList:

        logger.info('[ ] ' + carTour)

        # Check .src/panos/car/
        panoPath = os.path.join(panosDir, carTour)
        if not os.path.exists(panoPath):
            sys.exit(logger.critical('Pano "' + panoPath + '" NOT FOUND.'))

        # Check .src/panos/car/ has jpg files
        panorama = glob.glob(os.path.join(panoPath, "*.jpg"))
        if not panorama:
            sys.exit(logger.critical('Folder "' + panoPath + '" doesn\'t contain any JPG files.'))

        # Check car/
        tourPath = os.path.join(carTour)
        if not os.path.exists(tourPath):
            sys.exit(logger.critical('Folder "' + tourPath + '" NOT FOUND. Did you create the tiles correctly?'))

        # Check car/files/
        filesPath = os.path.join(carTour, 'files/')
        if not os.path.exists(filesPath):
            sys.exit(logger.critical('Folder "' + filesPath + '" NOT FOUND. Did you create the tiles correctly?'))

        # Check car/files/scenes/
        scenesPath = os.path.join(carTour, 'files/scenes/')
        if not os.path.exists(scenesPath):
            sys.exit(logger.critical('Folder "' + scenesPath + '" NOT FOUND. Did you create the tiles correctly?'))

        # Check car/files/scenes/tiles/
        for panoFile in panorama:
            panoFile = os.path.basename(panoFile)
            panoFile = os.path.splitext(panoFile)[0]
            tilesPath = os.path.join(scenesPath, panoFile)
            if not os.path.exists(tilesPath):
                sys.exit(logger.critical('Folder "' + tilesPath + '" NOT FOUND. Did you create the tiles correctly?'))

            # Check car/files/scenes/scene.xml
            tilesXml = panoFile + '.xml'
            tilesXmlPath = os.path.join(scenesPath, tilesXml)
            if not os.path.exists(tilesXmlPath):
                sys.exit(logger.critical('Folder "' + tilesXmlPath + '" NOT FOUND. Did you create the tiles correctly?'))

        # index.html
        tourIndex = os.path.join(tourPath, 'index.html')
        for file in os.scandir(tourPath):
            if file.name.endswith(".html"):
                os.unlink(file.path)
        shutil.copy(sceneTemplate, tourIndex)

        # devel/
        tourDevelPath = os.path.join(tourPath, 'devel/')
        if not os.path.exists(tourDevelPath):
            os.makedirs(tourDevelPath)

        # devel/index.html
        tourDevel = os.path.join(tourDevelPath, 'index.html')
        for file in os.scandir(tourDevelPath):
            if file.name.endswith(".html"):
                os.unlink(file.path)
        shutil.copy(develTemplate, tourDevel)

        # files/content/
        contentPath = os.path.join(filesPath, 'content/')
        if not os.path.exists(contentPath):
            os.makedirs(contentPath)
            # files/content/index.xml
        tourContent = os.path.join(contentPath, 'index.xml')
        if not os.path.exists(tourContent):
            shutil.copy(contentTemplate, tourContent)

        # files/content/*.jpg
        tourNumber = len(panorama)
        if tourNumber > 1:
            for panoFile in panorama:
                panoFile = os.path.basename(panoFile)
                panoFile = os.path.splitext(panoFile)[0]
                thumbs = panoFile + '.jpg'
                thumbsPath = os.path.join(contentPath,thumbs)
                # print(thumbsPath)
                if not os.path.exists(thumbsPath):
                    logger.warn('Thumbnail "' + thumbsPath + '" is missing.')

        # files/include/
        includePath = os.path.join(filesPath, 'include/')
        if os.path.exists(includePath):
            shutil.rmtree(includePath)
        shutil.copytree(includeStatic, includePath)

        # files/plugins/
        pluginsPath = os.path.join(filesPath, 'plugins/')
        if os.path.exists(pluginsPath):
            shutil.rmtree(pluginsPath)
        shutil.copytree(pluginsStatic, pluginsPath)

        # Edit first line of all scenes.xml files 

        i = 1
        for xmlF in glob.glob(os.path.join(scenesPath, "*.xml")):
            if os.name == 'nt':
                destF = os.path.join('C:\\', 'Users', 'Rafael', 'AppData', 'Local', 'Temp', 'tempfile')
            else:
                destF = os.path.join('/tmp', 'tempfile')
            sceneNo = 'scene' + str(i)
            newLine = '<scene name="' + sceneNo + '" thumburl="%FIRSTXML%/content/' + sceneNo + '.jpg" onstart="' + sceneNo + '();">'
            replace_first_line(xmlF, destF, newLine)
            shutil.copyfile(destF,xmlF)
            i = i + 1
            safeRm(destF)

        # files/tour.js
        jsPath = os.path.join(filesPath, 'tour.js')
        if os.path.exists(jsPath):
            os.remove(jsPath)
        shutil.copyfile(jsStatic, jsPath)

        # files/tour.swf
        swfPath = os.path.join(filesPath, 'tour.swf')
        if os.path.exists(swfPath):
            os.remove(swfPath)
        shutil.copyfile(swfStatic, swfPath)

        # files/devel.xml
        develPath = os.path.join(filesPath, 'devel.xml')
        if os.path.exists(develPath):
            os.remove(develPath)
            open(develPath, 'w+')
        with open(develPath, "a") as myfile:
            myfile.write('<?xml version="1.0" encoding="UTF-8"?>\n<krpano version="1.19">\n')

        scenesPath = os.path.join(filesPath, 'scenes/')
        addToDevel(pluginsPath)
        addToDevel(includePath)
        addToDevel(contentPath)
        addToDevel(scenesPath)

        with open(develPath, "a") as myfile:
            myfile.write('</krpano>')

        # files/tour.xml
        tourXml = os.path.join(filesPath, 'tour.xml')
        xmlList = [pluginsPath, includePath, contentPath, scenesPath]
        fileNms = allXml(xmlList)

        safeRm(tourXml)

        with open(tourXml, 'w') as outfile:
            outfile.write('<krpano version="1.19">\n')
            for fname in fileNms:
                with open(fname) as infile:
                    for line in infile:
                        if line.rstrip():
                            if '<krpano>' not in line and '</krpano>' not in line:
                                outfile.write(line)
            outfile.write('</krpano>')

        #subprocess.call(['tidy', '-modify', '--hide-comments', 'yes', '-wrap', '0', '-quiet', '-xml', tourXml])

        # Find obsolete folders
        ignored = {".no_scenes", ".src", ".env"}
        currentTours=[d for d in os.listdir(rootDir) if (os.path.isdir(d) and d not in ignored)]
        compareTours = set(currentTours).difference(carList)
        if compareTours:
            for obsoleteTour in compareTours:
                logger.critical("The following folder is obsolete: " + obsoleteTour)
            sys.exit()


    logger.info('EOF')

if __name__ == '__main__':
    main()
