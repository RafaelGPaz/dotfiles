#! /usr/bin/env python

import os

def defineGlobal ():
    global srcDir
    global srcContent
    global srcInclude
    global srcHtml
    global srcStructure
    global srcDevel
    global configFile

    srcDir = "E:\\virtual_tours\\.archives\\bin\\newvt\\src"
    srcContent = os.path.join(srcDir + '\\content')
    srcInclude = os.path.join(srcDir + '\\include')
    srcHtml = os.path.join(srcDir + '\\html')
    srcStructure = os.path.join(srcDir + '\\structure')
    srcDevel = os.path.join(srcStructure +'\\files\\devel.xml')

    configFile = 'vt_conf.py'

print(configFile)
