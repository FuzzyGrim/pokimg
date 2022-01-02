# pokimg

This is a small script inspired by this [project](https://gitlab.com/phoneybadger/pokemon-colorscripts), but since the output depends heavily on the font of your terminal, I decided to make a script that displays a PNG image of the Pokémon. I also made the script work without downloading anything in any other directories.

![Screenshot](screenshot.png)

## Requirements
**Important**:This script requires a terminal that supports images, however, it is currently coded to work only on [Kitty](https://sw.kovidgoyal.net/kitty/) and [iTerm2](https://iterm2.com/downloads.html).

In addition to one of these terminals, you will also need:
  - [Python](https://www.python.org/downloads/)
  - If you are using iTerm2, you will need to install [imgcat](https://iterm2.com/documentation-images.html) by clicking [iTerm2 > Install Shell Integration](https://i.stack.imgur.com/0DseS.png)

## Usage
You will need to run [`pokimg.sh`](https://github.com/FuzzyGrim/pokimg/blob/master/pokimg.sh):

Printing out a random pokemon:
```sh
pokimg.sh
pokimg.sh "-g"
```

Printing out a random pokemon from generation 1:
```sh
pokimg.sh "-g 1"
```

Printing out a random pokemon from generations 1,3 and 5:
```sh
pokimg.sh "-g 1 3 5"
```

Printing out a random pokemon from generations 1-3
```sh
pokimg.sh "-g 1-3"
```

## Running on terminal startup
You can display a random pokemon whenever a terminal gets launched by adding the `$HOME/pokimg/pokimg.sh` to your `.bashrc` or `config.fish` or `.zshrc`.


## TODO

These are some of the features I am thinking of adding:

  - ~~Specify generation to print~~
  - Choose upscale factor
  - Print a specific pokemon
  - Print list of all pokemon
  - Add help page for the program
