#!/usr/bin/env bash

# Description: merges all the XML files inside ./shared/include/*/index.xml
# and each tour's 'content/*.xml' and 'scenes/index.xml'
# Usage: Run inside the directory containing all the tour folders. Usually the directory where is the folder '.src'.

krpano_version="1.18"

if [ ! -d /lib/lsb/init-functions ]; then
    source /lib/lsb/init-functions
fi

# Merge all the files in 'shared/include'
if [ -d "./shared" ]; then
    log_action_begin_msg $"Merge include"
    includexml="./shared/include/index.xml"
    > $includexml
    for include_files in $(find ./shared/include/*/*.xml -maxdepth 1 -type f ); do
        cat $include_files >> $includexml
    done
    log_action_end_msg $?
fi

for tour in $(find ./* -maxdepth 0 -type d ! -iname "shared" ! -iname ".*" ) ; do
    log_action_msg $"Tour: $(basename $tour)"
    # printf "Merging $tour ...\n"
    tourxml="$tour/files/tour.xml"
    > $tourxml
    if [[ $(find $tour/files/plugins/* -maxdepth 0 -type f -name *.xml) ]]; then
        log_action_begin_msg $"Merge plugins"
        cat $tour/files/plugins/*.xml >> $tourxml
        log_action_end_msg $?
    fi
    log_action_begin_msg $"Merge content"
    cat $tour/files/content/*.xml >> $tourxml
    log_action_end_msg $?
    log_action_begin_msg $"Merge include"
    if [ -d "./shared" ]; then
        cat ./shared/include/index.xml >> $tourxml
    else
        for includefolder in $(find $tour/files/include/* -maxdepth 0 -type d) ; do
            cat $includefolder/*.xml >> $tourxml
        done
    fi
    log_action_end_msg $?
    log_action_begin_msg $"Merge scenes"
    if [ -f "$tour/files/scenes/index.xml" ]; then
        cat $tour/files/scenes/index.xml >> $tourxml
    else
        cat $tour/files/scenes/*.xml >> $tourxml
    fi
    log_action_end_msg $?

    # Clean up
    log_action_begin_msg $"Cleanup"
    tidy -modify --hide-comments yes -wrap 0 -quiet -xml $tour/files/tour.xml
    log_action_end_msg $?

    log_action_begin_msg $"Remove tags"
    # Remove all tags
    sed -i '/^<?xml/d' $tourxml
    sed -i '/^<krpano/d' $tourxml
    sed -i '/^<\/krpano/d' $tourxml
    log_action_end_msg $?

    # Add krpano tags at the beginning of tour.xml
    log_action_begin_msg $"Add tags"
    sed -i "1i<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<krpano version=\"$krpano_version\" onstart=\"startup();\" showerrors=\"false\">" $tourxml
    # Add closing krpano tag at the end of tour.xml and tour_clean.xml
    printf "</krpano>\n" >> $tourxml
    log_action_end_msg $?

done
log_action_end_msg $?
