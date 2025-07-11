# pokimg

This is a small script inspired by this [project](https://gitlab.com/phoneybadger/pokemon-colorscripts), but since the output depends heavily on the font of your terminal, I decided to make a script that displays a PNG image of the Pokémon. I also made the script work without downloading anything in any other directories.

![Screenshot](screenshot.png)

## Requirements
**Important**: This script requires [Kitty](https://sw.kovidgoyal.net/kitty/), [iTerm2](https://iterm2.com/downloads.html) or [Chafa](https://github.com/hpjansson/chafa/) with a compatible terminal emulator.

In addition, you will also need:
  - [Python](https://www.python.org/downloads/)
  - If you are using iTerm2, you will need to install [imgcat](https://iterm2.com/documentation-images.html) by clicking [iTerm2 > Install Shell Integration](https://i.stack.imgur.com/0DseS.png)

## Usage
You will need to run [`pokimg`](https://github.com/FuzzyGrim/pokimg/blob/master/pokimg):

Printing out a random pokemon:
```sh
pokimg
```

Printing out a specific pokemon:
```sh
pokimg -n pikachu
```

Printing out a random pokemon from generation 1:
```sh
pokimg -g 1
```

Printing out a random pokemon from generations 1,3 and 5:
```sh
pokimg -g 1 3 5
```

Printing out a random pokemon from generations 1-3
```sh
pokimg -g 1-3
```

Printing list of all pokemon names.
```sh
pokimg -l
```

## Running on terminal startup
You can display a random pokemon whenever a terminal gets launched by adding the `$HOME/pokimg/pokimg` to your `.bashrc` or `config.fish` or `.zshrc`.


## TODO

These are some of the features I am thinking of adding:

  - ~~Specify generation to print~~
  - ~~Print a specific pokemon~~
  - ~~Print list of all pokemon names~~
  - ~~Add help flag for the program~~
  - Choose upscale factor
