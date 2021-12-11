#!/bin/bash
ABSOLUTE_PATH=$(dirname $(realpath -s $0))
pokemon=$(python $ABSOLUTE_PATH/random_pokemon.py)

echo $pokemon
echo " "

kitty icat --align left --silent $ABSOLUTE_PATH/images/$pokemon.png