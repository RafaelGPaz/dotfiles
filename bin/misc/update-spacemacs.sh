#!/usr/bin/env bash

if [ ! -d /lib/lsb/init-functions ]; then
    source /lib/lsb/init-functions
fi

log_action_begin_msg $"git pull --rebase..."
git -C ~/.emacs.d/ pull --quiet --rebase origin master
log_action_end_msg $?
log_action_begin_msg "git submodule sync"
git -C ~/.emacs.d/ submodule sync
log_action_end_msg $?
log_action_begin_msg "git submodule update"
git -C ~/.emacs.d/ submodule update
log_action_end_msg $?
