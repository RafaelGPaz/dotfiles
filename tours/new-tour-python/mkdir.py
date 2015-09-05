#! /usr/bin/env python
import os

# Create a new directory if it doesn't exist
def mkdirif(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)

# Create a new directory even if it already exists
def mkdirforce(dirName):
    os.makedirs(dirName)