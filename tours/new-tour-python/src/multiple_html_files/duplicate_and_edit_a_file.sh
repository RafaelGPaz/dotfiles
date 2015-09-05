#!/bin/bash
#start with the number 2
i=2

# generate 21 files
while [ $i -le 5 ];do 
file1=scene$i.html
cp scene1.html $file1

#look for 'pano1' and replace for 'panoi'
sed -i "s/pano1/pano$i/g" $file1

i=$(( $i + 1 ))
done

echo " Script finished!"

