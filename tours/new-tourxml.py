#!/usr/bin/env python

import os
import glob
import fileinput
from usefulfunctions import safeRm

def main():

    alltours = []
    allxmlfiles = []
    bad_words = ['<krpano', '</krpano>', '<krpano version', 'coordfinder']

    for tour in glob.glob(os.getcwd()):
        alltours.append(tour)
        if '.src' in alltours:
            alltours.remove('.src')
        print("Tour: " + os.path.basename(tour))

    for tour in alltours:
        # Find all XML files recursively
        xmlfiles = glob.glob(tour + "\\files\\**\\*.xml", recursive=True)

        # Remove unwanted XML files
        for item in xmlfiles:
            if "devel.xml" not in item and "tour.xml" not in item and "_design_" not in item:
                allxmlfiles.append(item)
                # TO DO: Add line to apend vtourskin at first
        allxmlfiles.sort(reverse=False)

        # Merge files into tour.xml
        tourxml = tour + '\\files\\tour.xml'
        safeRm(tourxml)
        with open(tourxml, 'w') as outfile:
            outfile.writelines('<?xml version="1.0" encoding="UTF-8"?>\n<krpano version="1.19">\n')
            for line in fileinput.input(allxmlfiles, mode="rU"):
                if not any(bad_word in line for bad_word in bad_words):
                    outfile.write(line[1:])
            outfile.writelines("</krpano>")
        print('[ OK ] tour.xml')

    print("_EOF_")

if __name__ == '__main__':
    main()
