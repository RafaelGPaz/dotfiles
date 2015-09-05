#!/bin/bash

function check_conf {

    if [ -f "vt_conf.sh" ]
    then
        source vt_conf.sh
        current_dir=$new_dir
    else
        current_dir=.
    fi
}

function find_and_del {
    find $current_dir -name $1 -exec rm -vrf {} \;
}

function find_and_bck {
    find $current_dir -name $1 -exec mv {} "{}-$(date "+%F %H:%M:%S")" \;
}

function ask {
    echo "Delete:"
    echo "[0] PWD"
    echo "[1] sa.xml"
    echo "[2] scroll.xml"
    echo "[3] info_btn.xml"
    echo "[4] info_btn_text.xml"
    echo "[5] thumbs directory"
    echo "[6] *** coord.xml ***"
    echo "[7] *** hs.xml ***"
    echo "[8] *** content directory ***"
    read del

    if [ $del == "0" ]; then echo $current_dir; fi
    if [ $del == "1" ]; then find_and_del "sa.xml"; fi
    if [ $del == "2" ]; then find_and_del "scroll.xml"; fi
    if [ $del == "3" ]; then find_and_del "info_btn.xml"; fi
    if [ $del == "4" ]; then find_and_del "info_btn_text.xml"; fi
    if [ $del == "5" ]; then find_and_del "thumbs/*.jpg"; fi
    if [ $del == "6" ]; then find_and_bck "coord.xml"; fi
    if [ $del == "7" ]; then find_and_bck "hs.xml"; fi
    if [ $del == "8" ]; then find_and_del "content/*"; fi
}

function start {
    check_conf
    ask
}

start

