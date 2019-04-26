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
# pyenv:
# It installs python interpreters
# Usage:
# pyenv install 3.7.0
# pyenv shell 3.7.0
# pyenv global 3.7.0
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then;  eval "$(pyenv init -)"; fi
# ---
# pyenv-virtualenv:
# It's a pyenv plugin.
# It manages virtualenvs by configuring a local, global or shell environments.
# I prefer to use virtualenv-wrapper (see below).
# ---
# virtualenv-wrapper:
# It's a pyenv plugin.
# It keeps all virtualenvs in one directory ($WORKON_HOME) and manage them.
# Type wirtualenvwrapper to list al the commands.
export WORKON_HOME=$HOME/.virtualenvs
pyenv virtualenvwrapper_lazy

######################################################
# Aliases                                            #
######################################################
alias lsb="ls -1 | sed -e 's/\..*$//'"
alias sz="source ~/.zshrc && echo '.zshrc sourced'"

alias update_pip="python -m pip install -U pip"
alias findallbutjpg='find . -type f ! -iname *jpg'
alias clusterg='dotfiles/bin/clustergit/clustergit'
alias gitrecursive='clusterg --recursive --skip-symlinks -e "./\..*" -e virtual-tours -e Local -e Library && clusterg --recursive -d ~/virtual-tours/ -e gforces &&   clusterg -d ~/virtual-tours/gforces/cars/'
alias code='code-insiders'
alias brew='~/dotfiles/bin/misc/brew'
alias remove_-min_string='for file in *; do mv "${file}" "${file//\-min/}"; done'
alias echopath='echo "${PATH//:/"\n"}"'
