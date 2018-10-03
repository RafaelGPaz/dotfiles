#!/usr/bin/env python3

import argparse
import json
import logging
from json import loads
from pprint import pprint

import requests


def main():
    parser = argparse.ArgumentParser(description='Script to extract V10 latest models')
    args = parser.parse_args()

    # Download interiors.json
    # testfile = urlopen.open()
    file_name = 'https://s3-eu-west-1.amazonaws.com/autofs/shared/interiors/v10setup/interiors.json'
    requests.get(file_name, "interiors.json")
    print("Fetch interiors.json")

    data = json.load(open('interiors.json'))

    # Step into "TOURS" item
    tours = data.get("TOURS")

    # Build list with items like 'countrycode_make_model', removing duplicates
    allcars = []
    for key in tours:
        model = '_'.join((key.split('_', 3))[:3])
        if model not in allcars:
            allcars.append(model)

    # List containing old models
    to_be_removed = []

    for item in allcars:
        result = [i for i in tours if i.startswith((item + "_"))]
        # Cars with multiple models
        if len(result) > 1:
            year = [y[-4:] for y in result]
            # Exclude cars without year
            clean = [c for c in year if c.isdigit()]
            # For cars without year, choose last item in the list
            if (clean == []):
                highest = result[-1]
            else:
                highest = max(clean)
            # Add old cars to a list
            for exclude in result:
                if exclude[-4:] != highest:
                    to_be_removed.append(exclude)

    # Remove old models from dictionary
    for old_model in to_be_removed:
        del tours[old_model]

    # Export dictionary as JSON
    with open('interiors-filtered.json', 'w') as f:
        json.dump(data, f)
    print("Export: interiors-filtered.json")

    # Export list of cars as TXT
    with open('latest-cars.txt', 'w') as f:
        for key in data.get("TOURS"):
            f.write(key + '\n')
    print("Export: interiors-filtered.txt")

    print('EOL')

if __name__ == '__main__':
    main()
