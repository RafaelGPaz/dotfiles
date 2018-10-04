#!/usr/bin/env python3

import argparse
import json
import logging
import os
from json import loads
from pprint import pprint

import requests

def main():
    parser = argparse.ArgumentParser(description='Script to extract V10 latest models')
    args = parser.parse_args()

    # Download interiors.json
    file_name = 'https://s3-eu-west-1.amazonaws.com/autofs/shared/interiors/v10setup/interiors.json'
    r = requests.get(file_name)
    open('interiors.json', 'wb').write(r.content)
    data = json.load(open('interiors.json'))

    print("Fetch interiors.json")

    # Step into "TOURS" item
    tours = data.get("TOURS")

    # Build list with items like 'countrycode_make_model', removing duplicates
    allcars = []
    for key in tours:
        model = '_'.join((key.split('_', 3))[:3])
        if model not in allcars:
            allcars.append(model)

    # List to populate with old models
    to_be_removed = []

    for item in allcars:
        result = [i for i in tours if i.startswith((item + "_"))]
        # Cars with multiple models
        if len(result) > 1:
            last4 = [l[-4:] for l in result]
            year = [y for y in last4 if y.isdigit()]
            # Multiple models all ending in string
            # Action: Delete the first item
            if len(year) == 0:
                exclude = result[0]
                to_be_removed.append(exclude)
            # Multiple models with only 1 car ending in year AND the rest in string
            # Action: Delete all the cars ending in string
            if len(year) == 1:
                notyear = [e for e in result if e[-4] != "2"]
                for exclude in notyear:
                    to_be_removed.append(exclude)
            # Multiple models ending in year
            if len(year) > 1:
                highest = max(year)
                # Models don't end in the same year
                # Action: Delete all the cars smaller than highest year
                notlatest = [e for e in result if e[-4:] != highest]
                for exclude in notlatest:
                    to_be_removed.append(exclude)
                # Multiple models end in the highest yeear
                # Action: Delete all the cars but the one last in the list
                multiple = [l for l in result if l[-4:] == highest]
                if len(multiple) > 1:
                    multipledelete = len(multiple) - 1
                    for item in range(0,multipledelete):
                        exclude = multiple[item]
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

   # Tidy up
    try:
        os.remove("interiors.json")
    except OSError:
        pass

    print('EOL')

if __name__ == '__main__':
    main()
