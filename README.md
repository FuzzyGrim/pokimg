# pokimg

This is a small script inspired by this [project](https://gitlab.com/phoneybadger/pokemon-colorscripts), but since the output depends heavily on the font of your terminal, I decided to make a script that displays a PNG image of the Pokémon. I also made the script work without downloading anything in any other directories.

![Screenshot](screenshot.png)

## Requirements
**Important**:This script requires a terminal that supports images, however, it is currently hard-coded to work only on [Kitty](https://sw.kovidgoyal.net/kitty/). I will add support for more terminals soon. 

So, to use this script, you will need:
  - [Kitty](https://sw.kovidgoyal.net/kitty/binary/)
  - [Python](https://www.python.org/downloads/)

## Usage
You can run the program from the command line by running [](https://github.com/FuzzyGrim/pokimg/blob/master/pokimg.sh):

Example:
```
$HOME/pokimg/pokimg.sh
```

## Running on terminal startup
You can display a random pokemon whenever a terminal gets launched by adding the `$HOME/pokimg/pokimg.sh` to your `.bashrc` or `config.fish` or `.zshrc`.


## TODO

These are some of the features I am thinking of adding:

  - Choose upscale factor
  - Print a specific pokemon
  - Print a random pokemon from a specific generation
  - Print list of all pokemon
  - Add help page for the program
