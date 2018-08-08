#!/usr/bin/env zsh

export PATH="/usr/local/bin:/usr/local/sbin:$PATH:$HOME/dotfiles/bin/misc:$HOME/dotfiles/bin/newvt:$HOME/dotfiles/bin/tours"

######################################################
# Antigen                                            #
######################################################
source /usr/local/share/antigen/antigen.zsh
# Load the oh-my-zsh's library
antigen use oh-my-zsh
# Bundles from the default repo (robbyrussell's oh-my-zsh).
antigen bundles <<EOBUNDLES
brew
command-not-found
common-aliases
git
rsync
virtualenvwrapper
z
EOBUNDLES
# Syntax highlighting bundle
antigen bundle zsh-users/zsh-autosuggestions # Fish-like auto suggestions
antigen bundle zsh-users/zsh-completions # Extra zsh completions
antigen bundle zsh-users/zsh-syntax-highlighting
# Theme. Don't use 'antigen theme'
antigen bundle mafredri/zsh-async
antigen bundle sindresorhus/pure
# Tell antigen that you're done
antigen apply


######################################################
# Python                                             #
######################################################
# pyenv: to install python interpreters
# Usage:
# pyenv install 3.6.0
# pyenv shell 3.6.0
# pyenv global 3.6.0
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
# Fix 'pyenv install' bug by telling the compiler where the openssl package is located
# https://github.com/pyenv/pyenv/wiki/Common-build-problems
export CFLAGS="-I$(brew --prefix openssl)/include"
export LDFLAGS="-L$(brew --prefix openssl)/lib"
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
if which pyenv-virtualenv-init > /dev/null; then  eval "$(pyenv virtualenv-init -)"; fi
# ---
# pyenv-virtualenv: to configure a global environment
# Usage:
# pyenv virtualenv 3.6.0 pelican
# pyenv virtualenvs
# pyenv activate pelican
# pyenv deactivate pelican
# pyenv uninstall pelican
# ---
# virtualenv-wrapper: to keep all virtualenvs in the same directory and manage them
# Usage:
# mktmpenv
# lsvirtualenv
# showvirtualenv pelican
# rmvirtualenv pelicon
# cpvirtualenv pelicon pelican2
# allvirtualenv pip install -U pip
# workon pelican
# deactivote
# cdvirtualenv
# lssitepackages
export PYENV_VIRTUALENVWRAPPER_PREFER_PYVENV="false" # Use virtualenv instead of pyenv
export WORKON_HOME=$HOME/.virtualenvs
pyenv virtualenvwrapper_lazy

######################################################
# Aliases                                            #
######################################################
alias off="sudo poweroff"
alias reboot_and_sfck="sudo shutdown -rF now"
alias lsb="ls -1 | sed -e 's/\..*$//'"
alias rmgf="rm -fv '/media/c/Users/Rafael/Downloads/Assets-GForces 360 Makes and Models (Responses).xlsx'"
alias sz="source ~/.zshrc && echo '.zshrc sourced'"

alias update_pip="python -m pip install -U pip"
alias findallbutjpg='find . -type f ! -iname *jpg'
alias backup_img='rsync -zvra --delete /home/rafael/ /media/rafael/Life/life_img/'
alias backup_plus='rsync -zvra /home/rafael/ /media/rafael/Life/life_plus/'
alias backup_virtualbox='rsync -zvra --delete --exclude .cache --exclude .emacs.d /home/rafael/ /media/rafael/Elements/home_debian/'
alias backup_all='backup_img && backup_plus'
alias clusterg='dotfiles/bin/clustergit/clustergit'
alias gitrecursive='clusterg --recursive --skip-symlinks -e "./\..*" -e virtual-tours -e Local -e Library && clusterg --recursive -d ~/virtual-tours/ -e gforces  && clusterg --recursive -d ~/virtual-tours/gforces -e cars && clusterg -d ~/virtual-tours/gforces/cars/'
alias code='code-insiders'
alias powershell='pwsh'
alias brew='~/dotfiles/bin/misc/brew'
alias remove_-min_string='for file in *; do mv "${file}" "${file//\-min/}"; done'
alias import_v10='open -a Adobe\ Photoshop\ CC\ 2017 "/Users/rafael/dotfiles/bin/adobe-extendscript/import_v10.jsx"'
alias export_v10='open -a Adobe\ Photoshop\ CC\ 2017 "/Users/rafael/dotfiles/bin/adobe-extendscript/export_v10.jsx"'
