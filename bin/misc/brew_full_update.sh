#!/usr/bin/env bash

    brew update

    if [ "$1" != '--quick' ]; then
      printf "Removing brew cache\n"
      brew cleanup -s && rm -rf $(brew --cache)
      printf "Running brew update\n"
      brew update
    fi
    for c in $(brew list --cask); do
        if [ "$c" == "carbon-copy-cloner" ]; then
          continue;
        fi
        current="$(brew info --cask $c | sed -n '1p' | sed -n 's/^.*: //p' | sed -e 's/ (auto_updates)//g')"
        installed=( $(ls /usr/local/Caskroom/$c))

      if (! [[ " ${installed[@]} " == *" $current "* ]]); then
            printf "[ INFO ] $c (${installed[@]}) -----> $current\n"
            select ynx in "Yes" "No" "Exit"; do
              case $ynx in
                "Yes") echo "Uninstalling $c"; brew uninstall --cask --force "$c"; echo "Re-installing $c"; brew install --cask "$c"; break;;
                "No") echo "Skipping $c"; break;;
                "Exit") echo "Exiting brew-cask-upgrade"; return;;
              esac
            done
        else
            printf "[  OK  ] $c ($installed)\n"
        fi
    done

    brew upgrade
