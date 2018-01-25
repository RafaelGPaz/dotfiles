#!/usr/bin/env python3

import argparse
import logging
import glob
import os
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

    folder = os.path.join(os.path.expanduser('~'), 'virtual-tours', 'gforces', 'cars', '.src', 'layers')
    limit = (1 * 30 * 24 * 60 * 60) # 1 month in seconds
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

    logger.info('EOL')

if __name__ == '__main__':
    main()
