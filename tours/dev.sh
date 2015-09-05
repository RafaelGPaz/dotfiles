#!/bin/bash

# Usage: Run the script form inside files/ directories.
# To apply recursively, run it from the directory containing all the vt folders
# For examle, run it inside clarendon_apartments/ to apply it to the subfolders

# Edit: edit content/index.xml to apply changes to index.html
#       edit devel.xml to apply changes to devel.html

function add_variables {

    # Some paths variables
    if [ $HOSTNAME = "RafaLaptop" ]; then
        mydrive=/cygdrive/c/Users/rafaelgp/work
    else
        mydrive=/cygdrive/g
    fi
    orig_dir=$mydrive/virtual_tours/.archives/vt_template_8_0_15/src
    orig_content=$orig_dir/content
    orig_include=$orig_dir/include
    orig_structure=$orig_dir/structure
    orig_devel=$orig_structure/files/devel.xml

    scenes_dir=$(basename $scenes_dir)
    dest_dir=$scenes_dir
    dest_files=$dest_dir/files
    dest_content=$dest_files/content
    dest_include=$dest_files/include
    dest_scenes=$dest_files/scenes
    dest_devel=$dest_files/devel.xml

    panos_dir=panos/$scenes_dir

    krpano=$dest_files/krpano.xml
    temp_folder=$orig_dir/temp/$scenes_dir

}

function add_temp {
    if [ ! -d $temp_folder ]
    then
        mkdir $temp_folder
        > $temp_folder/plugins.temp
    fi
}

function add_krpano {

    # Copy devel.xml replacing any existing one
    cp $dest_devel $temp_folder"/devel1.temp"
    > $krpano
    # Make a temp file with all the files url's
    grep -o 'url=['"'"'"][^"'"'"']*['"'"'"]' $temp_folder"/devel1.temp" > $temp_folder"/devel2.temp"
    # Delete lines containing 'editor_and_options'
    sed -e '/editor_and_options/d' $temp_folder/devel2.temp > $temp_folder/devel3.temp
     # Delete lines containing 'scene'
    sed -e '/scenes/d' $temp_folder/devel3.temp > $temp_folder/devel4.temp
    # Strip off everything to leave just the url's'
    sed -e 's/^url=["'"'"']//' -e 's/["'"'"']$//' $temp_folder"/devel4.temp" > $temp_folder"/devel5.temp"
    # Remove %SWFPATH%
    sed -i 's/%SWFPATH%//g' $temp_folder/devel5.temp

    # Merge all the files into krpano.xml
    while read line
    do
        cat $dest_files"/"$line >> $krpano
    done < $temp_folder"/devel5.temp"

    # Add tiles code
    > $temp_folder/tiles.temp
    for f in $(find $dest_scenes/*.xml -maxdepth 0 )
    do
        cat $f >> $temp_folder/tiles.temp
    done
    cat $temp_folder/tiles.temp >> $krpano

    # Delete all the lines beginning with <?xml, <krpano </krpano
    sed -i '/^<?xml/d' $krpano
    sed -i '/^<krpano/d' $krpano
    sed -i '/^<\/krpano/d' $krpano

    # Add krpano tags at the beginning and at the end of krpano.xml
    sed -i '1i<?xml version="1.0" encoding="UTF-8"?>\n<krpano version="1.0.8.15" showerrors="false">' $krpano
    echo '</krpano>' >> $krpano

    # Delete empty lines
    sed -i '/^$/d' $krpano

    # Delete commented lines
    sed -i '/-->/d' $krpano
}

function start {
    for scenes_dir in $(find ./* -maxdepth 0 -type d )
    do
        add_variables $scenes_dir
        add_temp
        add_krpano
    done
}

start

echo "----> Done"
