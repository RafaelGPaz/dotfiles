#!/bin/bash

#  DESCRIPTION:
# Script made for Clarendon apartments
# It will search for scene*.xml files and:
# 1- Delete the first line
# 2- Add a new <scene /> line with the scene name and the corresponding apartment
# Then it will change the path from:
# %SWFPATH%/scenes
# to:
# %SWFPATH%/../../ApartmentFolderName/files/scenes
# This change ensures that the "more_apartments" button loads the corresponding tour inside the same frame
# USAGE:
# Run from directory e:/virtual_tours/clarendon_apartments/

for eachdirectory in $(find ./* -maxdepth 0 -type d ); do
    # echo $eachdirectory
    eachdirectory=$(basename $eachdirectory)

    echo "Apartment: $eachdirectory"

    for each_xml_file_path in $(find ./$eachdirectory/files/scenes/ -maxdepth 3 -name scene*.xml ); do

        each_xml_file=$(basename $each_xml_file_path)
        extension="${each_xml_file##*.}"
        each_xml_file="${each_xml_file%.*}"
        each_xml_file_path_bck=$each_xml_file_path"_bck"

        first_line='<scene name="'$each_xml_file'" apartment="'$eachdirectory'">'

        sed -i -e "1c $first_line" $each_xml_file_path
        sed -e 's/\%SWFPATH\%\/scenes/\%SWFPATH\%\/..\/..\/'$eachdirectory'\/files\/scenes/g' $each_xml_file_path > $each_xml_file_path_bck
        mv $each_xml_file_path_bck $each_xml_file_path

        echo "Edited $each_xml_file"

    done

done
