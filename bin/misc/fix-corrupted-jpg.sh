#!/usr/bin/env bash

echo "Start"
mkdir converted
find . -iname '*.jpg' |
while read file
do convert "$file" converted/"$file"
   touch -r "$file" converted/"$file"
   echo "$file"
done