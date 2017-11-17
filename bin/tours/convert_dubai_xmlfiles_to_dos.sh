#!/bin/bash

root="/media/e/virtual_tours/gforces/manufacturers/lexus_manufacturer/ae_lexus_gs350_2016/ae_lexus_gs350_2016/files/scenes/"

find $root/base/*.xml -type f -exec dos2unix {} \;
find $root/luxury/*.xml -type f -exec dos2unix {} \;
find $root/fsport/*.xml -type f -exec dos2unix {} \;

echo "_EOF_"
exit 0
