#!/bin/bash

# Alias: ccd
# Usage: ccd [part of directory's name]
# Limitations: it only search in the current level to avoid to many results
# If it founds 1 result, it will enter to that directory
# If there are more options, it will list them to choose one of them
# If no match is found, then promts again to enter directory name

function question {
    search=$1
    destdir=($(find *$search* -maxdepth 0 -type d))
    # for a in "${destdir[@]}"; do echo $a; done
}

function result {
    if [[ "${#destdir[@]}" = "0" ]]
    then
        echo "Try again"
        start
    fi

    if [[ "${#destdir[@]}" = "1" ]]
    then
        cd $destdir
        # echo "Enter in: "$destdir
    fi

    if [[ "${#destdir[@]}" -gt "1" ]]
    then

        # Loop thought all the possible resusts
        numb=0
        list=1
        for i in "${destdir[@]}"
        do
            echo " $list - ${destdir[$numb]}"
            numb=$((numb+1))
            list=$((list+1))
        done

        echo "Choose a directory:"
        read gotodir
        gotodir=$((gotodir-1))

        enterdir=${destdir[$gotodir]}
        # echo "Enter in: $enterdir"
        cd $enterdir
    fi
}

question $1
result
