#!/bin/bash

# Description: merges all the XML files inside each 'scenes' directories into a file named 'scenes/index.xml'
# Usage: Run inside the directory containing all the tour folders. Usually the directory where is the folder '.src'.

for tour in $(find ./* -maxdepth 0 -type d ! -iname "shared" ! -iname ".*" ) ; do
    # tour=toyota_86
    > $tour/files/scenes/index.xml
    printf "<krpano>\n" > $tour/files/scenes/index.xml
    printf "Merging $tour/files/scenes/index.xml ...\n"
    for xmlfile in $(find $tour/files/scenes/* -maxdepth 0 ! -iname "index.xml" -type f ); do
        cat $xmlfile >> $tour/files/scenes/index.xml
    done
    printf "</krpano>\n" >> $tour/files/scenes/index.xml

    # Delete dos new line
    sed -i 's/\r//' $tour/files/scenes/index.xml

done
