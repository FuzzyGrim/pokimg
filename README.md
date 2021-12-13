# pokimg

This is a small script inspired by this [project](https://gitlab.com/phoneybadger/pokemon-colorscripts), but since the output depends heavily on the font of your terminal, I decided to make a script that displays a PNG image of the Pokémon. I also made the script work without downloading anything in any other directories.

![Screenshot](screenshot.png)

## Requirements
**Important**:This script requires a terminal that supports images, however, it is currently coded to work only on [Kitty](https://sw.kovidgoyal.net/kitty/) and [iTerm2](https://iterm2.com/downloads.html).

In addition to one of these terminals, you will also need:
  - [Python](https://www.python.org/downloads/)
  - If you are using iTerm2, you will need to install imgcat by clicking [iTerm2 > Install Shell Integration](https://i.stack.imgur.com/0DseS.png)

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
