#!/usr/bin/env python3

import argparse
import glob
import logging
import os
import shutil
import sys
import time

import colorlog

def main():
    # Add description
    parser = argparse.ArgumentParser(
        description='This script helps to reduce space in the hard drive.\
        It searchs for PSB files older than 1 month and deletes them. \
        Then it creates an empty file so it doesn\'t break the script \
        to manage the V10 cars', usage='Run the script from any directory')
    parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.NOTSET)

    logger.info("Started")

    # ---------------------
    # PSB layers
    # ---------------------

    folder = os.path.join(os.path.expanduser('~'), 'virtual-tours', 'gforces', 'cars', '.src', 'layers')
    limit = (1 * 30 * 24 * 60 * 60) # 1 month in seconds
    today = time.time() # current date in seconds
    num_all = 0 # number of cars older than the limet
    num_real = 0

    allpsb = sorted(glob.glob(os.path.join(folder, "*.psb")))

    for psb in allpsb:
        psb_age = os.path.getmtime(psb)
        old = today - psb_age > limit
        size = os.path.getsize(psb)
        not_empty = size > 0
        basename = os.path.basename(psb)
        if old and not_empty:
            os.remove(psb) # Delete original copy
            logger.info('[    ] Deleted ' + basename)
            open(psb, 'w').close()  # Create empty file to substitute original one
            num_all += 1
        if not_empty:
            num_real += 1

    logger.info('[----] Cars deleted: ' + str(num_all))
    logger.info('[----] PSB: ' + str(len(allpsb)))
    logger.info('[----] Real: ' + str(num_real))
    logger.info('[----] Empty: ' + str(len(allpsb) - num_real))

    # ---------------------
    # NL cars
    # ---------------------

    # First of all make sure external drive (H:) is plugged
    drive = '/Volumes/Extra/'
    if not os.path.ismount(drive):
        logger.critical(drive + ': volume is not mounted')
        sys.exit(0)

    toursfolder = os.path.join(os.path.expanduser('~'), 'virtual-tours', 'gforces', 'cars')
    allnltours = sorted(glob.glob(os.path.join(toursfolder, "nl_*")))
    num_all = 0
    for tour in allnltours:
        basename = os.path.basename(tour)
        dest = os.path.join(drive, 'virtual-tours', 'gforces', 'cars', basename)
        if not os.path.exists(dest):
            shutil.copytree(tour, dest) # Copy preserving metadata
            shutil.rmtree(tour) # Delete original copy
            os.makedirs(tour)
            os.makedirs(os.path.join(tour, 'files' ))
            os.makedirs(os.path.join(tour, 'files', 'scenes' ))
            os.makedirs(os.path.join(tour, 'files', 'scenes', 'tiles' ))
            num_all += 1

    logger.info('[----] NL virtual tour folders moved: ' + str(num_all))

    panosfolder = os.path.join(os.path.expanduser('~'), 'virtual-tours', 'gforces', 'cars', '.src', 'panos')
    panosfolderdrive = os.path.join(drive, 'virtual-tours', 'gforces', 'cars', '.src', 'panos')
    allnlpanos = sorted(glob.glob(os.path.join(panosfolder, "nl_*")))
    num_all = 0
    if not os.path.exists(panosfolderdrive):
        os.makedirs(panosfolderdrive)
    for pano in allnlpanos:
        basename = os.path.basename(pano)
        dest = os.path.join(panosfolderdrive, basename)
        if not os.path.exists(dest):
            shutil.copy2(pano, dest)
            os.remove(pano)
            open(pano, 'w').close()  # Create empty file to substitute original one
            num_all += 1

    logger.info('[----] NL folders in .src/panos/ moved: ' + str(num_all))

    # ---------------------
    # import cars
    # ---------------------

    importfolder = os.path.join(os.path.expanduser('~'), 'virtual-tours', 'gforces', 'cars', '.src', 'import')
    importfolderdrive = os.path.join(drive, 'virtual-tours', 'gforces', 'cars', '.src', 'import')
    years = ('*2011.jpg', '*2012.jpg', '*2013.jpg', '*2014.jpg', '*2015.jpg', '*2016.jpg')
    allimportpanos = []
    for importfiles in years:
        allimportpanos.extend(sorted(glob.glob(os.path.join(importfolder,importfiles))))
    num_all = 0
    if not os.path.exists(importfolderdrive):
        os.makedirs(importfolderdrive)
    for pano in allimportpanos:
        basename = os.path.basename(pano)
        dest = os.path.join(importfolderdrive, basename)
        if not os.path.exists(dest):
            shutil.copy2(pano, dest)
            os.remove(pano)
            open(pano, 'w').close()  # Create empty file to substitute original one
            num_all += 1

    logger.info('[----] files in .src/import/ moved: ' + str(num_all))

    # ---------------------
    # masks cars
    # ---------------------

    masksfolder = os.path.join(os.path.expanduser('~'), 'virtual-tours', 'gforces', 'cars', '.src', 'masks')
    masksfolderdrive = os.path.join(drive, 'virtual-tours', 'gforces', 'cars', '.src', 'masks')
    years = ('*2011.psb', '*2012.psb', '*2013.psb', '*2014.psb', '*2015.psb', '*2016.psb')
    allmaskspanos = []
    for maskfiles in years:
        allmaskspanos.extend(sorted(glob.glob(os.path.join(masksfolder,maskfiles))))
    num_all = 0
    if not os.path.exists(masksfolderdrive):
        os.makedirs(masksfolderdrive)
    for mask in allmaskspanos:
        basename = os.path.basename(mask)
        dest = os.path.join(masksfolderdrive, basename)
        if not os.path.exists(dest):
            shutil.copy2(mask, dest)
            os.remove(mask)
            open(mask, 'w').close()  # Create empty file to substitute original one
            num_all += 1

    logger.info('[----] files in .srrc/masks/ moved: ' + str(num_all))

    # ---------------------
    # panos cars
    # ---------------------

    panosfolder = os.path.join(os.path.expanduser('~'), 'virtual-tours', 'gforces', 'cars', '.src', 'panos')
    panosfolderdrive = os.path.join(drive, 'virtual-tours', 'gforces', 'cars', '.src', 'panos')
    years = ('*generic*', '*2008*', '*2009*', '*2010*', '*2011*', '*2012*', '*2013*', '*2014*', '*2015*', '*2016*')
    allpanos = []
    for panofiles in years:
        allpanos.extend(sorted(glob.glob(os.path.join(panosfolder,panofiles))))
    num_all = 0
    if not os.path.exists(panosfolderdrive):
        os.makedirs(panosfolderdrive)
    for pano in allpanos:
        basename = os.path.basename(pano)
        dest = os.path.join(panosfolderdrive, basename)
        if os.path.isfile(pano):
            if not os.path.exists(dest):
                shutil.copy2(pano, dest)
                os.remove(pano)
                open(pano, 'w').close()  # Create empty file to substitute original one
                num_all += 1
        if os.path.isdir(pano):
            if not os.path.exists(dest):
                shutil.copytree(pano, dest) # Copy preserving metadata
                shutil.rmtree(pano) # Delete original copy
                os.makedirs(pano)
                open(os.path.join(panosfolder, basename, 'scene_1_a.jpg'), 'w').close()
                open(os.path.join(panosfolder, basename, 'scene_1_b.jpg'), 'w').close()
                open(os.path.join(panosfolder, basename, 'scene_1_c.jpg'), 'w').close()
                open(os.path.join(panosfolder, basename, 'scene_2_a.jpg'), 'w').close()
                open(os.path.join(panosfolder, basename, 'scene_2_b.jpg'), 'w').close()
                open(os.path.join(panosfolder, basename, 'scene_2_c.jpg'), 'w').close()
                num_all += 1

    logger.info('[----] folders in .src/panos/ moved: ' + str(num_all))

    logger.info('EOL')

if __name__ == '__main__':
    main()
