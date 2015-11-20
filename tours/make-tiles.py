#!/usr/bin/env python

import os
import subprocess

def main():

    krpath = "/home/rafael/bin/krpano/bin/krpanotools"
    krconfig = "-config=/home/rafael/bin/krpano/krpano_conf/templates/tv_tiles_2_levels_all_devices.config"
    panopath = "./.src/panos/tour1/scene1.jpg"
    kr = [krpath, "makepano", krconfig ,panopath]
    subprocess.call(kr)

if __name__ == '__main__':
    main()
