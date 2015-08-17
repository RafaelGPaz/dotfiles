#!/usr/bin/env python

import os
import errno

def main():
    pass

root_dir = '.'
panos_dir = root_dir + '/.src/panos'
krdir = '~/bin/krpano/bin'
krpath = krdir + '/krpanotool makepano'

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

for tour in os.listdir(panos_dir):
    print (tour)
    make_sure_path_exists(tour)
    make_sure_path_exists(tour + '/files')
    make_sure_path_exists(tour + '/files/scenes')
    for scene in os.listdir(panos_dir + '/' + tour):
        print (scene)

# -config=$krdir\krpano_conf\templates\tv_tiles_2_levels_all_devices.config

if __name__ == '__main__':
    main()
