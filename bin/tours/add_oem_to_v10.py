#!/usr/bin/env python3

import argparse
import glob
import logging
import os
from os.path import expanduser
import shutil
import sys
import colorlog

class readable_dir(argparse.Action):
    def __call__(self,parser, namespace, values, option_string=None):
        prospective_dir=values
        setattr(namespace,self.dest,prospective_dir)

def main():
    # Add description
    parser = argparse.ArgumentParser(description='Deletes the specified virtual tour folder and the panoramas in the .SRC/PANOS folder')
    parser.add_argument('-c', '--carname', action=readable_dir, dest='carname', help='Car name to be deleted')
    args = parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.DEBUG)

    name1 = args.carname
    underscores = name1.split('_')
    countries = ['gb', 'ae', 'ie', 'nl', 'za']
    if underscores[0] not in countries:
        sys.stdout.write('Country missing. Enter manually:')
        # TODO

    logger.info("Started")

    v10path = os.path.join(expanduser('~'), 'virtual-tours', 'gforces', 'cars')
    v10 = os.path.join(v10path, name1)
    v10files = os.path.join(v10path, name1, 'files')
    v10scenes = os.path.join(v10path, name1, 'files', 'scenes')
    v10content = os.path.join(v10files, 'content')
    oem = os.path.join(os.getcwd(), name1)
    oemfiles = os.path.join(oem, 'files')
    oemcontent = os.path.join(oemfiles, 'content')
    oemscenes = os.path.join(oemfiles, 'scenes')
    oemindex = os.path.join(oem, 'index.html')
    oemdevel = os.path.join(oem, 'devel.html')
    oeminterior = os.path.join(os.getcwd(), name1, 'interior.html')
    oeminteriordevel = os.path.join(os.getcwd(), name1, 'interiordevel.html')
    v10index = os.path.join(v10, 'index.html')
    v10devel = os.path.join(v10, 'devel.html')
    v10scenesxmlarray = glob.glob(os.path.join(oemscenes, '*.xml'))

    if os.path.exists(v10):
        shutil.rmtree(v10)
        logger.debug('- ' + v10)

    os.makedirs(v10)
    logger.debug('+ ' + v10)
    if os.path.exists(oeminterior):
        shutil.copy(oeminterior,v10index)
        logger.debug('+ ' + v10index)
        shutil.copy(oeminteriordevel,v10devel)
        logger.debug('+ ' + v10devel)
    else:
        shutil.copy(oemindex,v10index)
        logger.debug('+ ' + v10index)
        shutil.copy(oemdevel,v10devel)
        logger.debug('+ ' + v10devel)
    os.makedirs(v10files)
    logger.debug('+ ' + v10files)
    shutil.copytree(oemcontent, v10content)
    logger.debug('+ ' + v10content)
    os.makedirs(v10scenes)
    logger.debug('+ ' + v10scenes)
    for item in v10scenesxmlarray:
        shutil.copy(item, v10scenes)
        logger.debug('+ ' + v10scenes + '/' + os.path.basename(item))

    os.chdir(v10)
    logger.info('EOL')

if __name__ == '__main__':
    main()
