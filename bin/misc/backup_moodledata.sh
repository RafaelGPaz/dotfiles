#!/usr/bin/env bash

BACKUPFILE1='/var/www/moodledata.tar.gz'
SOURCEDIR1='/var/www/moodledata/'
BACKUPFILE2='/var/www/360certified.tar.gz'
SOURCEDIR2='/var/www/360certified.co.uk/'

# 1. Delete previous backup file
# 2. Backup directory

if [ -f $BACKUPFILE1 ]; then
    rm -f $BACKUPFILE1
fi
tar cpzfP $BACKUPFILE1 $SOURCEDIR1

if [ -f $BACKUPFILE2 ]; then
    rm -f $BACKUPFILE2
fi
tar cpzfP $BACKUPFILE2 $SOURCEDIR2

exit 0

# Run backup monthly on the first day at midnight
# crontab -e
# 0 0 1 * * /bin/bash ~/bin/misc/backup_moodledata.sh

# 1. Minutes: 0 to 59
# 2. Hours: 0 to 23
# 3. Day of Month: 1 to 31
# 4. Month: 1 to 12
# 5. Day of Week: 0 to 6
# 6. Command
