#!/usr/bin/env zsh

export PATH="/usr/local/bin:/usr/local/sbin:$PATH:$HOME/dotfiles/bin/misc:$HOME/dotfiles/bin/newvt:$HOME/dotfiles/bin/tours"

######################################################
# Antigen                                            #
######################################################
source /usr/local/share/antigen/antigen.zsh
# Load the oh-my-zsh's library
antigen use oh-my-zsh
# robbyrussell
antigen bundles <<EOBUNDLES
common-aliases
git
rsync
z
EOBUNDLES
# zsh-users
antigen bundle zsh-users/zsh-autosuggestions # Fish-like auto suggestions
antigen bundle zsh-users/zsh-completions # Extra zsh completions
antigen bundle zsh-users/zsh-syntax-highlighting
# other
antigen theme romkatv/powerlevel10k # Minimal terminal theme
antigen apply

# Command prompt
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

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
alias gitrecursive='clusterg --recursive --skip-symlinks -e "./\..*" -e virtual-tours -e Local -e Library -e nvim && clusterg --recursive -d ~/virtual-tours/ -e gforces && clusterg -d ~/virtual-tours/gforces/cars/'
alias code='code-insiders'
alias brew='~/dotfiles/bin/misc/brew'
alias remove_-min_string='for file in *; do mv "${file}" "${file//\-min/}"; done'
alias echopath='echo "${PATH//:/"\n"}"'
alias p_helper="tr ':' '\n' <<< $(/usr/libexec/path_helper)"
alias krjsyalm='npx js-yaml ~/Documents/projects/vscode-krpano/syntaxes/krpano.tmLanguage.yaml > ~/Documents/projects/vscode-krpano/syntaxes/krpano.tmLanguage.json'
alias ou="open-url.sh $1"
alias delchat="gsed -i '/chat/d; /myfree/d' ~/.zsh_history"
