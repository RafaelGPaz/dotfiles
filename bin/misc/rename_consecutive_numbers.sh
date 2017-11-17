#! /bin/bash

echo "This script will rename all the files as CUSTOMNAME#"
echo "For example scene1, scene2, scene3, etc..."

echo "Enter the custom name:"
read custom_name

new=1
ext=

for i in *
do
        ext="${i#*.}"
        mv "$i" "$custom_name$new.$ext"
        ((new++))
done