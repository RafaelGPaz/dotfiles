#! /bin/bash

# Some path variables
if [ $HOSTNAME = "debian" ]; then
    c_drive=/media/sf_C_DRIVE
    f_drive=/media/sf_F_DRIVE
    my_home=$c_drive/Users/rafaelgp/AppData/Roaming
elif [ $HOSTNAME = "RafaLaptop" ]; then
    c_drive=/c
    f_drive=/f
    my_home=$HOME
else
    echo "This script does only works in the laptop"
    exit 1
fi

local_drive=$c_drive/Users/rafaelgp/
backup_drive=$f_drive/rafaelgp/
backup_plus_drive=$f_drive/rafaelgp_plus/
exclude_list=$my_home/bin/exclude_list
rsync_log_file=$my_home/log/rsync_image.cron.log

# echo
echo "Backup Home directory"
echo "Choose backup type:"
echo "[1] Image"
echo "[2] Incremental"
echo "[3] Show stats"

read backup_type

> $rsync_log_file

# Image
if [ $backup_type == "1" ]; then
    rsync -zvra --delete-before --log-file=$rsync_log_file --log-format=' %t %B %i %o %f (%c)' --progress --exclude-from="$exclude_list" $local_drive $backup_drive
fi

# Incremental
if [ $backup_type == "2" ]; then
    rsync -zvra --log-file=$rsync_log_file --log-format=' %t %B %i %o %f (%c)' --progress --exclude-from="$exclude_list" $local_drive $backup_plus_drive
fi

# Stats
if [ $backup_type == "3" ]; then
    rsync --dry-run --stats -a -i --delete-delay --exclude-from="$exclude_list" $local_drive $backup_drive
fi

echo "Done"

exit 0
