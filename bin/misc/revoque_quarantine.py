#!/usr/bin/env python3

import subprocess
import argparse
import logging
import colorlog

class readabledir(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir = values
        setattr(namespace, self.dest, prospective_dir)

def main():
    # Add description
    parser = argparse.ArgumentParser(description='Revoques quarantine status from all the files \
    inside a directory.')
    parser.add_argument('-d', '--directory', action=readabledir, dest='directory', help='Directory \
    to which apply the command')
    args = parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.NOTSET)

    try:
        result = subprocess.call(["sudo", "xattr", "-r", "-d", "com.apple.quarantine", \
        args.directory], stderr=subprocess.STDOUT)
        if result == 0:
            logger.info(" Success!!!")
    except subprocess.CalledProcessError:
        logger.error("Something went wrong")

if __name__ == '__main__':
    main()

# sudo xattr -r -d com.apple.quarantine ../krpano-1.19-pr14