#! /usr/bin/env python

import os
import sys
import shutil

from mkdir import *

sys.path.append("E:\\virtual_tours\\.archives\\bin\\python\\src\\makeTour")
from globalVar import *
from checkConfig import *

def main():
    global configFile
    # Use the next line only for debugging
    os.chdir('C:\\Users\\rafaelgp\\Downloads\\test-newvt')

    defineGlobal()
    print(configFile)
    #checkConfig()

    print ("[FINISH]")

if __name__ == '__main__': main()


