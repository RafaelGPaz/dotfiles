#!/bin/bash

#  DESCRIPTION:
# Script made for Clarendon apartments
# It will search for scene*.xml files and:
# 1- Delete the first line
# 2- Add a new <scene /> line with the scene name and the corresponding apartment 

# USAGE:
# Run from directory g:/virtual_tours/clarendon_apartments/

for eachdirectory in $(find ./* -maxdepth 0 -type d ); do
    # echo $eachdirectory
    eachdirectory=$(basename $eachdirectory)

    echo "Apartment: $eachdirectory"

    for each_xml_file_path in $(find ./$eachdirectory/files/scenes/ -maxdepth 3 -name scene*.xml ); do

        each_xml_file=$(basename $each_xml_file_path)
        extension="${each_xml_file##*.}"
        each_xml_file="${each_xml_file%.*}"

        first_line='<scene name="'$each_xml_file'" apartment="'$eachdirectory'">'

        sed -i -e "1c $first_line" $each_xml_file_path

        echo "Edited $each_xml_file"

    done

done