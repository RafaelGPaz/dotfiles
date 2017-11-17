#! /usr/bin/env python

# 9/10/2011
# Loop to generate several html files to open the different scenes in a virtual tour
# Required: 'scene1.html' file with the following line: viewer.addVariable("xml", "files/panos/pano1.xml");

#Import copyfile command from shutil module
from shutil import copyfile
#loop between 2 and 20
for i in range(2, 21):
    #variables 
    htmlfile = "scene%d.html" % (i,)
    pano = "pano%d" % (i,)
    copyfile("scene1.html", htmlfile)
	#look for 'pano1' and replace for 'panoi'
    s = open(htmlfile).read()
    #print "Opening:", (htmlfile) 
    s = s.replace('pano1', pano)
    #print "Replacing pano1 for: ", (pano) 
    f = open(htmlfile, 'w')
    #print "Saving: ", (htmlfile) 
    f.write(s)
    #print "Closing: ", (htmlfile) 
    f.close()
    
print "How cool is that?"
