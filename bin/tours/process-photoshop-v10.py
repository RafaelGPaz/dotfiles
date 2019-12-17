#!/usr/bin/env python3

import argparse
import logging
import os
import subprocess

import colorlog


def main():
    parser = argparse.ArgumentParser(
        description='Run Import and Export scripts to build V10 Photoshop files')
    parser.add_argument('-i', '--import', action="store_true",
                        default="True", dest='importFile', help='Import Phoshop file')
    parser.add_argument('-e', '--export', action="store_true",
                        default="False", dest='exportFile', help='Export Phoshop file')
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
    photoshopPath = os.path.join('/', 'Applications', 'Adobe Photoshop CC 2018',
                                 'Adobe Photoshop CC 2018.app', 'Contents', 'MacOS', 'Adobe Photoshop CC 2018')
    scriptsDir = os.path.join('/', 'Users', 'rafael',
                              'Documents', 'Adobe Scripts')
    importPath = os.path.join(scriptsDir, 'import_v10.jsxbin')
    exportPath = os.path.join(scriptsDir, 'export_v10.jsxbin')
    importCall = ['open', '-a', photoshopPath, importPath]
    exportCall = ['open', '-a', photoshopPath, exportPath]

    if args.importFile:
        subprocess.call(importCall, stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    if args.exportFile:
        subprocess.call(exportCall, stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

    logger.info('EOL')


if __name__ == '__main__':
    main()
