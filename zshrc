source /usr/local/share/antigen/antigen.zsh

# Load the oh-my-zsh's library
antigen use oh-my-zsh

antigen bundles <<EOBUNDLES
command-not-found
common-aliases
git
rsync
virtualenvwrapper
z
zsh-users/zsh-autosuggestions # Fish-like auto suggestions
zsh-users/zsh-completions # Extra zsh completions
EOBUNDLES

# Syntax highlighting bundle (Load last)
antigen bundle zsh-users/zsh-syntax-highlighting

# Load the theme
antigen theme robbyrussell

# Tell antigen that you're done
antigen apply

# Set Zsh option
setopt correct

# Add to $PATH
export PATH="$PATH:/usr/local/sbin:$HOME/dotfiles/bin/misc:$HOME/dotfiles/bin/newvt:$HOME/dotfiles/bin/tours:$PATH"

# Configuration for Virtualenv and Virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
source /usr/local/bin/virtualenvwrapper.sh

# Aliases
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

alias clustergit='~/bin/clustergit/clustergit --recursive -e .cache/ -e .config/ -e .local/'
alias code='code-insiders'