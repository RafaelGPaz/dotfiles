#!/usr/bin/env python

import os
import glob
import fileinput
import shutil
from usefulfunctions import safeRm

def main():

    alltours = []
    allxmlfiles = []
    bad_words = ['<krpano', '</krpano>', '<krpano version', 'coordfinder']

    for tour in os.listdir(os.getcwd()):
        alltours.append(tour)
        if '.src' in alltours:
            alltours.remove('.src')
        if 'shared' in alltours:
            alltours.remove('shared')
        if '.git' in alltours:
            alltours.remove('.git')
        if '.custom' in alltours:
            alltours.remove('.custom')
        if '.gitignore' in alltours:
            alltours.remove('.gitignore')

    for tour in alltours:
        print("Tour: " + os.path.basename(tour))
        # Find all XML files recursively
        xmlfiles = glob.glob(tour + "\\files\\**\\*.xml", recursive=True)

        # Remove unwanted XML files
        for item in xmlfiles:
            if "devel.xml" not in item and "tour.xml" not in item and "_design_" not in item and "en.xml" not in item  and "ar" not in item:
                allxmlfiles.append(item)
                print(item)
                # TO DO: Add line to apend vtourskin at first
        allxmlfiles.sort(reverse=False)

        # Merge files into tour.xml
        tourxml = tour + '\\files\\tour.xml'
        enxml = tour + '\\files\\en.xml'
        safeRm(tourxml)
        with open(tourxml, 'w', encoding='utf-8') as outfile:
            outfile.writelines('<?xml version="1.0" encoding="UTF-8"?>\n<krpano version="1.19">\n')
            for line in fileinput.input(allxmlfiles, mode="rU", openhook=fileinput.hook_encoded("utf-8-sig")):
                if not any(bad_word in line for bad_word in bad_words):
                    if line.rstrip():
                        outfile.write(line)
            outfile.writelines("</krpano>")
        print('[ OK ] ' + tourxml)
        if os.path.isfile(enxml):
            shutil.copyfile(tourxml,enxml)
            print('[ OK ] ' + enxml)
        allxmlfiles = []

    print("_EOF_")

if __name__ == '__main__':
    main()
