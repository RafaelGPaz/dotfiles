#!/usr/bin/env python3

import argparse
import logging
import glob
import os
import sys
import colorlog

def main():
    # Add description
    parser = argparse.ArgumentParser(
        description='This script scans the "layers" directory in external hard drive \
        and create an empty file in the corresponding folder in my laptop', \
        usage='Run the script from any directory')
    parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.INFO)

    logger.info("Started")

    # First of all make sure external is plugged
    drive = os.path.join(os.sep, 'Volumes', 'Backup IMG')
    if not os.path.exists('/Volumes/Backup IMG'):
        logger.critical(drive + ': volume is not mounted')
        sys.exit(0)

    folder = os.path.join(os.sep, 'Volumes', 'Backup IMG', 'work_img', 'virtual_tours', 'gforces', 'cars', '.src', 'layers')
    counter = 0

    allpsb = glob.glob(os.path.join(folder, "*.psb"))

    for psb in allpsb:
        basename = os.path.basename(psb)
        dest = os.path.join(os.sep, 'Users', 'rafael', 'virtual-tours', 'gforces', 'cars', '.src', 'layers')
        movefile = os.path.join(dest, basename)
        open(movefile, 'w').close()  # Create empty file to substitute original one
        logger.info('[    ] Making ' + basename)
        counter += 1
    logger.info('Total: ' + str(counter))

    logger.info('EOL')

if __name__ == '__main__':
    main()