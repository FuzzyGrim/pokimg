#!/bin/bash

if [ "$TERM_PROGRAM" == "iTerm.app" ];
  then TERMINAL="iTerm2"

else
  TERMINAL=$(ps -o comm= -p "$(($(ps -o ppid= -p "$(($(ps -o sid= -p "$$")))")))")
fi

ABSOLUTE_PATH=$(cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P)

OUTPUT=$(python3 $ABSOLUTE_PATH/random_pokemon.py $1)

echo $OUTPUT
echo " "

set -- $OUTPUT
POKEMON=$1

case $TERMINAL in

  kitty)
    kitty icat --align left --silent $ABSOLUTE_PATH/images/$POKEMON.png
    ;;

  iTerm2)
    $HOME/.iterm2/imgcat $ABSOLUTE_PATH/images/$POKEMON.png
    ;;

  *)
    echo "Terminal Emulator is neither Kitty nor iTerm2"
    ;;

esac