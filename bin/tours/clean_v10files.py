# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import argparse
import logging
import glob
import os
import time
import shutil
import sys
import colorlog

def main():
    # Add description
    parser = argparse.ArgumentParser(
        description='This script helps to reduce space in hard drive.\
        It search for PSB files older than 6 months and move them from \
        \'gforces/cars/.src/layers\' to \'H:/gforces_v10_layers/\'. \
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

    # First of all make sure external drive (H:) is plugged
    drive = 'H'
    if os.system("vol %s: 2>nul>nul" % (drive)) != 0:
        logger.critical(drive + ': volume is not mounted')
        sys.exit(0)

    if os.name == 'nt':
        rootdir = os.path.join('E:\\')
    else:
        rootdir = os.path.join('/media', 'e')

    folder = os.path.join(rootdir, 'virtual_tours', 'gforces', 'cars', '.src', 'layers')
    limit = (6 * 30 * 24 * 60 * 60) # 6 months in seconds
    today = time.time() # current date in seconds
    num_all = 0 # number of cars older than the limet
    num_real = 0

    allpsb = glob.glob(os.path.join(folder, "*.psb"))

    for psb in allpsb:
        psb_age = os.path.getmtime(psb)
        old = today - psb_age > limit
        size = os.path.getsize(psb)
        not_empty = size > 0
        basename = os.path.basename(psb)
        dest = os.path.join('H:\\', 'gforces_v10_layers', basename)
        if old and not_empty:
            logger.info('[    ] Moving ' + basename)
            shutil.copy2(psb, dest) # Copy preserving metadata
            os.remove(psb) # Delete original copy
            open(psb, 'w').close()  # Create empty file to substitute original one
            num_all += 1
        if not_empty:
            num_real += 1

    logger.info('[----] Cars moved: ' + str(num_all))
    logger.info('[----] PSB: ' + str(len(allpsb)))
    logger.info('[----] Real: ' + str(num_real))
    logger.info('[----] Empty: ' + str(len(allpsb) - num_real))

    logger.info('EOL')

if __name__ == '__main__':
    main()
