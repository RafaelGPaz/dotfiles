#!/bin/bash

# Description: replace '%SWFPATH%' for '%CURRENTXML%' in any xml file inside any directory named 'scenes'
# Usage: Run inside the directory containing all the tours' folders

for tour in $(find . -maxdepth 3 -type d -name 'scenes' ); do
    for xmlfile in $(find $tour -name "*.xml" ); do
        echo "Editing $xmlfile ..."
        xmlfile_bck=$xmlfile"_bck"
        sed -e 's/\%SWFPATH\%/\%CURRENTXML\%/g' $xmlfile > $xmlfile_bck
        mv $xmlfile_bck $xmlfile
    done
done
