#!/usr/bin/env python
import argparse
import collections
import fileinput
import glob
import logging
import os
import shutil
import subprocess
import sys

def mkdirif(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def main():
    # Script only for Windows
    if sys.platform != 'win32':
        sys.exit('Script is only for Windows')

    # Script only for python3
    if sys.version_info[0] < 3:
        sys.exit('Must be using Python 3')

    parser = argparse.ArgumentParser(description='Creates tiles for cars with visualiser option.')
    parser.add_argument('-i', action='store_false', dest='ignoreunderscores', default=True, help='Skip checking 4 underscores')
    args = parser.parse_args()
    logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)

    logging.info("Started")

    # Delete any residual files or folders
    panosdir = '.src\\panos\\'
    for root, dirs, files in os.walk(panosdir):
        for filePath in glob.glob(os.path.join(root, "*.kro")):
            if os.path.isfile(filePath):
                os.remove(filePath)
        for dirPath in glob.glob(os.path.join(root, "output")):
            if os.path.isdir:
                shutil.rmtree(dirPath)

    # Check if the directory containing the panos is empty
    if not os.listdir(panosdir):
        sys.exit('ERROR: Panos directory is empty')

    # Build list 'allitems' with ALL the items inside .src/panos excluding 'output'
    allitems = []
    tours = glob.glob(panosdir + '/*')
    for item in tours:
        if os.path.isfile(item):
            allitems.append(item)
        if os.path.isdir(item):
            subtours = glob.glob(item + "/*")
            for subitem in subtours:
                allitems.append(subitem)
        if 'output' in item:
            allitems.remove('output')

    # Check there aren't duplicated items
    duplicates = []
    for i in tours:
        iname = os.path.basename(i)
        ibasename = os.path.splitext(iname)[0]
        duplicates.append(ibasename)

    repeatedcar = [item for item, count in collections.Counter(duplicates).items() if count > 1]
    if repeatedcar:
        sys.exit('ERROR: The following cars are repeated: ' + str(repeatedcar ))

    # Check that the panorama names has 3 underscores, unless this is ignored with the switch '-ignoreunderscores'
    for tourname in allitems:
        if args.ignoreunderscores != False:
            tourname = os.path.basename(i)
            tourbasename = os.path.splitext(iname)[0]
            underscores = len(tourbasename.split('_'))
            if underscores != 4:
                sys.exit('ERROR: File ' + tourbasename +  ' contains ' + str(underscores ) + ' underscores instead of 4. Please rename it.' )

    # Check if tiles are needed
    for car in allitems:
        carbasename = os.path.basename(os.path.dirname(car))
        tourbasename = os.path.splitext(os.path.basename(car))[0]
        filesdir = carbasename + '\\files'
        scenesdir = carbasename + '\\files\\scenes'
        parentdir = os.path.basename(os.path.abspath('..'))
        krdir = 'E:/documents/software/virtual_tours/krpano'
        krpath = krdir +'/bin/krpanotools64.exe'
        krconfig = '-config=' + krdir + '/krpano_conf/templates/tv_tiles_for_cars_ipad.config'
        kr = [krpath, "makepano", krconfig ,car]
        FNULL = open(os.devnull, 'w') # Run krpano silently
        # Special projects
        if "scene_" in tourbasename or parentdir == 'hr_owen':
            scenesdir = os.path.join(carbasename, "files\\scenes")
            tilesdir = os.path.join(scenesdir, carbasename)
            outputdir = panosdir + carbasename + '\\output'
            outputtilesdir = outputdir + '\\scenes\\' + tourbasename
            outputxmlfile = outputdir + "\\" + tourbasename + '.xml'
            # HROWEN cars
            if parentdir == 'hr_owen':
                replaceorigin = 'scenes/' + tourbasename
                replacedest = '%SWFPATH%/../../' + carbasename + '/files/scenes/' + tourbasename
            # Visualiser V10
            elif os.path.exists('./shared/'):
                replaceorigin = 'scenes/' + tourbasename
                replacedest = '%SWFPATH%/../' + carbasename + '/files/scenes/' + tourbasename
            # Scene Variation cars
            else:
                replaceorigin = 'scenes/' + tourbasename
                replacedest = '%CURRENTXML%/scenes/' + tourbasename
            tilesdir = carbasename + '\\files\\scenes\\' + tourbasename
            xmlfile = carbasename + '\\files\\scenes\\' + tourbasename + '.xml'
            message = carbasename + '/' + tourbasename
        # Normal car
        else:
            scenesdir = os.path.join(tourbasename, "files\\scenes")
            tilesdir = os.path.join(scenesdir, "tiles")
            outputdir = panosdir + 'output'
            outputtilesdir = outputdir + '\\scenes\\' + tourbasename
            outputxmlfile = outputdir + '\\' + tourbasename + '.xml'
            replaceorigin = 'scenes/' + tourbasename
            if os.path.exists('./shared/'):
                replacedest = '%SWFPATH%/../' + tourbasename + '/files/scenes/tiles'
            else:
                replacedest = '%CURRENTXML%/scenes/tiles'
            tilesdir = tourbasename + '\\files\\scenes\\tiles'
            xmlfile = tourbasename + '\\files\\scenes\\scene.xml'
            message = tourbasename

        if os.path.exists(tilesdir):
            logging.info('[ OK ] ' + message)
        else:
            logging.info('[    ] Making tiles for: ' + message)
            # Create folder structure
            mkdirif(tourbasename)
            mkdirif(filesdir)
            mkdirif(scenesdir)

            subprocess.call(kr, stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT)
            # subprocess.call(kr)

            for line in fileinput.input(outputxmlfile, inplace=True):
                print(line.replace(replaceorigin, replacedest), end="")
                # Move the folder containing the tiles
            if os.path.exists(outputtilesdir):
                shutil.move(outputtilesdir, tilesdir)
                # Move the scene.xml file
            if os.path.exists(outputxmlfile):
                shutil.move(outputxmlfile, xmlfile)
                # Delete output folder
            if os.path.exists(outputdir):
                shutil.rmtree(outputdir)

    logging.info('Finished')

if __name__ == '__main__':
    main()
