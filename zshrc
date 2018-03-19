#!/usr/bin/env zsh

export PATH="$PATH:/usr/local/sbin:$HOME/dotfiles/bin/misc:$HOME/dotfiles/bin/newvt:$HOME/dotfiles/bin/tours"

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
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
# Fix 'pyenv install' bug by telling the compiler where the openssl package is located
# https://github.com/pyenv/pyenv/wiki/Common-build-problems
export CFLAGS="-I$(brew --prefix openssl)/include"
export LDFLAGS="-L$(brew --prefix openssl)/lib"
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=`which python`
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
source /usr/local/bin/virtualenvwrapper_lazy.sh

######################################################
# Aliases                                            #
######################################################
alias off="sudo poweroff"
alias reboot_and_sfck="sudo shutdown -rF now"
alias lsb="ls -1 | sed -e 's/\..*$//'"
alias rmgf="rm -fv '/media/c/Users/Rafael/Downloads/Assets-GForces 360 Makes and Models (Responses).xlsx'"
alias sz="source ~/.zshrc && echo '.zshrc sourced'"

alias findallbutjpg='find . -type f ! -iname *jpg'
alias backup_img='rsync -zvra --delete /home/rafael/ /media/rafael/Life/life_img/'
alias backup_plus='rsync -zvra /home/rafael/ /media/rafael/Life/life_plus/'
alias backup_virtualbox='rsync -zvra --delete --exclude .cache --exclude .emacs.d /home/rafael/ /media/rafael/Elements/home_debian/'
alias backup_all='backup_img && backup_plus'
alias clustergit='dotfiles/bin/clustergit/clustergit'
alias gitrecursive='clustergit --recursive --skip-symlinks -e "./\..*" -e virtual-tours -e Local -e Library && clustergit --recursive -d ~/virtual-tours/ -e gforces  && clustergit --recursive -d ~/virtual-tours/gforces -e cars && clustergit -d ~/virtual-tours/gforces/cars/'
alias code='code-insiders'
alias powershell='pwsh'
alias brew='~/dotfiles/bin/misc/brew'
