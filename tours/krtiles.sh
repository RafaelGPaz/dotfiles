#!/bin/bash

# This script creates the tiles for all the panoramas in the current directory that it's executed

echo "---- Start ----"

krpath="/cygdrive/g/documents/software/virtual_tours/krpano/krpanotools-1.0.8.15/kmakemultires"
config="-config=templates/tv_tiles_2_levels_all_devices.config"

for f in *.jpg;
do
    $krpath $config $f;
    # echo $f
done

echo -e "Panoramas created:\n$f\n";
