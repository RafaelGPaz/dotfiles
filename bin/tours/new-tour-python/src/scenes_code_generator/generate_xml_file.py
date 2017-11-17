#! /usr/bin/env python

# 10/10/2011
# Loop to generate the code for the scenes tiles, asking the number of scenes. Folding marks are included'
# Required: 'tiles.xml' with a single scene code. The nome of the folder (usually pano1,etc...) is substituted by the text 'changethis'
# Need to go to same directory where the files is to run it

# Import required modules
from shutil import copyfile
import os
# Questions
scenes_no = raw_input ("How many scenes have the virtual tour? ")
if scenes_no == '':
    print "Introduce number of scenes."
    exit()
if int(scenes_no)<=0:
    print "Number of scenes needs to be at least 1"
    exit()
if int(scenes_no)>100:
    print "Too many scenes."
    exit()
# Loop to generate the temporary xml files, 1 per scene
for i in range(0, int(scenes_no)):
    #variables
    new_xml_file = "include/xml/tiles%d.xml" % (i + 1,)
    pano_folder = "pano%d" % (i + 1,)
    copyfile('include/xml/tiles.xml', new_xml_file)
    s = open(new_xml_file).read()
    s = s.replace('changethis', pano_folder)
    f = open(new_xml_file, 'w')
    f.write(s)
    f.close()
# Generate all_tiles.xml file
fout=open("include/xml/all_tiles.xml","a")
# Write tiles1 content into all_tiles.xml. Then delete it
for line in open("include/xml/tiles1.xml"):
    fout.write(line)
os.remove("include/xml/tiles1.xml")
# Same for the nest of the files
for num in range(2, i + 2):
    f = open("include/xml/tiles"+str(num)+".xml")
    f.next() # skip first line
    for line in f:
        fout.write(line)
    f.close() # not really needed
    os.remove("include/xml/tiles"+str(num)+".xml")
# add this to the end of the file
fout.write("<!--}}}-->")
fout.close()
# End
print "Thank you"
