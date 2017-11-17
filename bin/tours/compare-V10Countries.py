#!/usr/bin/env python3
import argparse
import colorlog
import logging
import os
import sys
import xml.etree.ElementTree as ET

def main():
    parser = argparse.ArgumentParser(
        description='This script makes sure all the duplicated cars has its corresponding intries in config.xml. It compares: 1. gb and ie (Audi, Seat and Volkswagen 2. gb and ae (Lexus)',
        usage='compare-V10Countries.py (Run form any directory)')
    args = parser.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level=logging.INFO)

    logger.info("Started")

    if os.name == 'nt':
        tree = ET.parse('E:\\virtual_tours\\gforces\\cars\\.src\\config.xml')
    else:
        tree = ET.parse('/media/e/virtual_tours/gforces/cars/.src/config.xml')

    root = tree.getroot()

    # Compare ie and gb

    # Make a list containing all the Audi, Seat and Volkswagen models in gb
    gbList = []
    for car in tree.findall('country/brand/model/car'):
        carID = car.get('id')
        if carID.startswith('gb_audi') or carID.startswith('gb_seat') or carID.startswith('gb_volkswagen'):
            # Remove the first 3 caracters = country code
            gbList.append(carID[3:])

    # Make a list containing all the Audi, Seat and Volkswagen models in ie
    ieList = []
    for car in tree.findall('country/brand/model/car'):
        carID = car.get('id')
        if carID.startswith('ie_audi') or carID.startswith('ie_seat') or carID.startswith('ie_volkswagen'):
            # Remove the first 3 caracters = country code
            ieList.append(carID[3:])

    comp1 = sorted(set(gbList).difference(ieList))
    if comp1:
        print('  ====================')
        print('  Ireland missing cars')
        print('  ====================')
        for ieCar in comp1:
            ieCar = '  ie_' + ieCar
            print(ieCar)

    comp2 = sorted(set(ieList).difference(gbList))
    if comp2:
        print('  ================')
        print('  GB missing cars:')
        print('  ================')
        for gbCar in comp2:
            gbCar = '  gb_' + gbCar
            print(gbCar)

    # Compare ae and gb

    # Make a list containing all the cars in <ignore>
    ignoreList = []
    for ignoredCar in tree.findall('ignore/car'):
        carID = ignoredCar.get('id')
        ignoreList.append(carID[3:])

    # Make a list containing all the Lexus models in ae
    aeList = []
    for car in tree.findall('country/brand/model/car'):
        carID = car.get('id')
        if carID.startswith('ae_lexus'):
            # Remove the first 3 caracters = country code
            aeList.append(carID[3:])

    # Make a list containing all the Lexus models in gb
    gbList = []
    for car in tree.findall('country/brand/model/car'):
        carID = car.get('id')
        if carID.startswith('gb_lexus'):
            # Remove the first 3 caracters = country code
            gbList.append(carID[3:])

    comp3a = set(aeList).difference(gbList)
    comp3b = comp3a.difference_update(ignoreList)
    if comp3b:
        sorted(comp3b)
        print('  ===================')
        print('  Dubai missing cars')
        print('  ===================')
        for aeCar in comp3b:
            aeCar = '  ae_' + aeCar
            print(aeCar)

    comp4a = set(aeList).difference(gbList)
    comp4b = comp4a.difference_update(ignoreList)
    if comp4b:
        sorted(comp4b)
        print('  ===============')
        print('  GB missing cars')
        print('  ===============')
        for gbCar in comp4b:
            gbCar = '  gb_' + gbCar
            print(gbCar)

    if not comp1 and not comp2 and not comp3b and not comp4b:
        print('  All OK!!!')
        logger.info('EOF')

if __name__ == '__main__':
    main()
