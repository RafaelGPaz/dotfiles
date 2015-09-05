#!/bin/bash

# Description: change 'scenes/' to '%SWFPATH%/scenes' in any xml file in the current directory
# Usage: Run inside the directory with all the xml files

for xmlfile in $(find *".xml" -maxdepth 0 ); do
    echo "Editing $xmlfile ..."
    sed -e 's/scenes/\%SWFPATH\%\/scenes/g' $xmlfile > bck_$xmlfile
    mv bck_$xmlfile $xmlfile
done
