#! /usr/bin/env python

import os
import sys
import glob
import fileinput
import shutil
import subprocess
from shortForHumans import *
from mkdir import *

# Use the next line only for debugging
#os.chdir('C:\\Users\\rafaelgp\\Desktop\\makeTiles')
#os.chdir('E:\\virtual_tours\\gforces\\allcars')

def main():

    krdir = 'E:/documents/software/virtual_tours/krpano'
    krpath = krdir +'/bin/krpanotools64.exe'
    # Quick and dirty: use a different template for Krpano
    # krconfig = ' makepano -config=' + krdir + '/krpano_conf/templates/tv_tiles_2_levels_all_devices.config'
    krconfig = ' makepano -config=' + krdir + '/krpano_conf/templates/tv_tiles_for_cars_ipad.config'

    mkdirif('.src')
    mkdirif('.src\\panos')

    # Is .src/panos empty?
    currentDir = os.getcwd()
    if currentDir == 'E:\\virtual_tours\\gforces\\allcars':
        panosDir = 'E:\\virtual_tours\\gforces\\cars\\.src\\panos'
    else:
        panosDir = '.src\\panos'
        if not os.listdir(panosDir):
            sys.exit('[ ERROR ] Panos directory is empty')

    # Dive into .src/panos directory
    tourDir = os.listdir(panosDir)
    for tourName in tourDir:
        print('[ TOUR ] ' + tourName)
        tourPath = os.path.join(panosDir,tourName)
        if not os.listdir(tourPath):
            sys.exit('[ ERROR ] ' +  tourPath + 'directory is empty')
        sceneList = []
        for panoName in glob.glob(tourPath + "/*.jpg"):
            sceneList.append(os.path.basename(panoName))
        sort_nicely(sceneList)
        for panoName in sceneList:
            sceneName = os.path.splitext(panoName)[0]
            # Do we need to create tiles?
            tilesDir = tourName + '\\files\\scenes\\' + sceneName
            if os.path.exists(tilesDir):
                print('[  OK  ] ' + sceneName)
            else:
                print('-------> Making tiles for: ' + sceneName)
                mkdirif(tourName)
                mkdirif(tourName + '\\files')
                mkdirif(tourName + '\\files\\scenes')
                panoPath = ' ' + os.path.abspath(tourPath + '\\' + panoName)
                krpano = krpath + krconfig + panoPath
                # Run Krpanotools without autput
                FNULL = open(os.devnull, 'w')
                subprocess.call(krpano, stdout=FNULL, stderr=subprocess.STDOUT)
                xmlFile = tourPath + '\\output\\' + sceneName + '.xml'
                # Replace 'scenes/' for my custom path in the scene.xml file
                for line in fileinput.input(xmlFile, inplace=True):
                    print(line.replace('scenes/', '%SWFPATH%/scenes/'), end='')
                # Move the folder containing the tiles
                shutil.move(tourPath +'\\output\\scenes\\' + sceneName, tilesDir)
                # Move the scene.xml file
                shutil.move(tourPath +'\\output\\' + sceneName + '.xml', tourName + '\\files\\scenes')
                # Delete output folder
                shutil.rmtree(tourPath + '\\output')

    print ("[FINISH]")

if __name__ == '__main__': main()

# TO DO

# Check if there is any car missing comparing the JPG files in '.src/panos/' and  the file '.src/config.xml'


