#!/usr/bin/env python3

import argparse
import logging
import os
import subprocess

import colorlog

class readable_dir(argparse.Action):
    def __call__(self,parser, namespace, values, option_string=None):
        prospective_dir=values
        setattr(namespace,self.dest,prospective_dir)

def main():

    def embeddata(dirname):
            logger.info('[   ] ' + dirname)
            filenames = sorted(os.listdir(dirname))

            for filename in filenames:
                if filename.endswith('.jpg') or filename.endswith('.JPG')\
                        or filename.endswith('.jpeg') or filename.endswith('.JPEG'):
                    filepath = os.path.join(dirname, filename)
                    filename_base, filename_ext = os.path.splitext(filename)
                    logger.info('[ - ] ' + filename_base)

                    correct_input = False
                    while not correct_input:
                        try:
                            ath = int(input("INFO [ > ] H: "))
                            atv = int(input("INFO [ > ] V: "))
                        except ValueError:
                            print("Please enter integers only")
                        else:
                            correct_input = True

                    posehead = '-PoseHeadingDegrees=' + str(ath)
                    initialheading = '-InitialViewHeadingDegrees=' + str(ath)
                    initialpitch = '-InitialViewPitchDegrees=' + str(atv)

                    subprocess.run(['exiftool',
                                    '-overwrite_original',
                                    '-Make=RICOH',
                                    '-Model=RICOH THETA S',
                                    '-ProjectionType=equirectangular',
                                    '-UsePanoramaViewer=True',
                                    '-CroppedAreaImageWidthPixels=6000',
                                    '-CroppedAreaImageHeightPixels=3000',
                                    '-FullPanoWidthPixels=6000',
                                    '-FullPanoHeightPixels=3000',
                                    '-CroppedAreaLeftPixels=0',
                                    '-CroppedAreaTopPixels=0',
                                    posehead,
                                    initialheading,
                                    initialpitch,
                                    '-InitialViewRollDegrees=0',
                                    '-InitialHorizontalFOVDegrees=75',
                                    filepath])

    # Add description
    parser = argparse.ArgumentParser(description='Embeds some metadata to turn a panorama \
    into interactive image in Facebook, Google+, etc...')
    parser.add_argument('-d', '--directory', action=readable_dir, dest='dirname', help='Search for files only in this directory')
    # parser.add_argument('-d', '--destination', dest='destination', help='Simple paramenter')
    args = parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.NOTSET)

    logger.info("Started")

    dirname = args.dirname
    path = '.'

    if dirname:
        embeddata(dirname)
    else:
        dirs=[d for d in os.listdir(path) if os.path.isdir(os.path.join(path,d))]
        for dirname in dirs:
            embeddata(dirname)

    logger.info('EOL')

if __name__ == '__main__':
    main()