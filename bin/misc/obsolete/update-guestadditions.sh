#!/bin/bash

if [ ! -f /media/cdrom/VBoxLinuxAdditions.run ]; then
    printf "Please mount Install Guest Additions CD\n"
    exit0
fi

printf "Do you want to upgrade the system? [y/n]\n"
read upgradeSystem
if [ $upgradeSystem = "y" ]; then
    sudo aptitude update && sudo aptitude safe-upgrade
fi

sudo m-a prepare && sudo bash /media/cdrom/VBoxLinuxAdditions.run


printf "[DONE]\n"
