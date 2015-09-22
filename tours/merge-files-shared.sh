#!/bin/bash

# Description: merges all the XML files inside ./shared/include/*/index.xml
# and each tour's 'content/*.xml' and 'scenes/index.xml'
# Usage: Run inside the directory containing all the tour folders. Usually the directory where is the folder '.src'.

krpano_version="1.18"

# Merge all the files in 'shared/include'
includexml="./shared/include/index.xml"
printf "[ OK ] Merge include\n"
> $includexml
for include_files in $(find ./shared/include/*/*.xml -maxdepth 1 -type f ); do
    cat $include_files >> $includexml
done

for tour in $(find ./* -maxdepth 0 -type d ! -iname "shared" ! -iname ".*" ) ; do
    printf "Merging $tour ...\n"
    tourxml="$tour/files/tour.xml"
    > $tourxml
    printf "[ OK ] Content\n"
    cat $tour/files/content/index.xml >> $tourxml
    printf "[ OK ] Include\n"
    cat ./shared/include/index.xml >> $tourxml
    printf "[ OK ] Scenes\n"
    cat $tour/files/scenes/index.xml >> $tourxml

    # Clean up
    printf "[ OK ] Cleanup\n"
    # Delete empty lines
    sed -i '/^$/d' $tourxml
    # Delete commented lines
    sed -i '/-->/d' $tourxml
    # Delete indentation
    sed -i -r 's/^[[:blank:]]+//g' $tourxml
    # Delete empty spaces around any = signs
    sed -i 's/\ *=\ */=/g' $tourxml

    # Remove all tags
    printf "[ OK ] Remove tags\n"
    sed -i '/^<?xml/d' $tourxml
    sed -i '/^<krpano/d' $tourxml
    sed -i '/^<\/krpano/d' $tourxml

    # Add krpano tags at the beginning of tour.xml
    printf "[ OK ] Add tags\n"
    sed -i "1i<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<krpano version=\"$krpano_version\" onstart=\"startup();\" showerrors=\"false\">" $tourxml
    # Add closing krpano tag at the end of tour.xml and tour_clean.xml
    printf "</krpano>\n" >> $tourxml

    # Concatenate all lines
    printf "[ OK ] Minify\n"
    cat $tourxml | while read line; do
        echo -n "${line} "
    done > $tour/files/tour-temp.xml

    mv $tour/files/tour-temp.xml $tourxml

done

printf "[DONE]\n"
