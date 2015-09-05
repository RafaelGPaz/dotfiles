#!/bin/bash
# For each file in the *_star folders, create their corresponding panorama folder and move it there.
# Then delete the *_star falders

for f in `ls *_star/*.jpg`; do
    name=`echo "$f"|sed 's/ -.*//'`
    dir=`echo "$name"|cut -c8,9,10,11,12`
    mkdir -p "$dir"
    mv "$f" "$dir"
done
echo 'end'
# rmdir *_star
