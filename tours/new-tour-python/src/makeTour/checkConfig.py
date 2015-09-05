#! /usr/bin/env python

import os

def checkConfig ():
    # Is there a configuration file?
    if not os.path.exists(configFile):
        vtPath = os.getcwd()
        currentDir = os.getcwd().split(os.sep)[-1]
        sceneDir = ''
        pluginsDir = "E:\\documents\\software\\virtual_tours\\krpano\\bin\\viewer\\plugins"
        #listPlugins = os.listdir(srcInclude)

        #file = open(config, "w")
        # For testing: overwrite
        file = open(configFile, "w+")
        file.write("#! /usr/bin/env python\n")
        file.write("\n# ========== Paths ==========\n")
        file.write('vtPath="' + vtPath +'"' + "\n")
        file.write('domainUrl="http://www.clients.tourvista.co.uk/vt/' + currentDir + '/' + sceneDir  +  '/files"' + "\n")
        file.write('crossDomain="http://www.clients.tourvista.co.uk/crossdomain.xml"' + "\n")
        file.write('#domainUrl=".\\files"' + "\n")
        file.write('#crossDomain=.' + "\n")
        file.write("\n# ========== Base ==========\n")
        #for krPlugin in listPlugins:
        #    print(krPlugin)
        file.write("\n# ========== Optional ==========\n")
        file.write("\n# ========== Optionsaha ==========\n")
        file.close(configFile)

        print ('-------> Make Config file')
    else:
        print ('-------> Sourced Config file')