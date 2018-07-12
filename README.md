# BATTLE SHIP


### Requirements
This game requires that you have `python3` installed on your machine.
Please run `python3 --version` to check if you have the required version.

In the event that you don't have python3, please follow this guide to install it.
[Installing Python3](http://docs.python-guide.org/en/latest/starting/install3/osx/)

### Getting started

1. Run `git clone https://github.com/GeorgeSmith-Sweeper/Battle-Ship.git` in your terminal

2. Run `python3 play.py` at the root in the __Battle-Ship__ folder to start the game.

### Playing the Game

The game will begin by displaying instructions, a board, and a flashing prompt.
![Game Start](/images/game_start.png?raw=true)

Begin playing by marking the board using standard battleship shot protocol (A1-J10).

Once you have made a move, you will be notified whether you have hit or missed a ship, and the computer will make a move.

![first_shot](/images/first_shot.png?raw=true)

Ships can only take a certain number of hits before sinking. If you happen to sink your opponents ship (or vise versa), the game will display the location of the sunk ship.

![sunk_ship](/images/sunk_ship.png?raw=true)

The game will end when a player has successfully destroyed all five of the opponents ships.

### Tests

The tests for this game can be run with the command `pytest`, at the root in the __Battle-Ship__ folder.

### Code Coverage

1. Run `coverage run -m pytest` at the root to gather test data.

2. Run `coverage report` at the root to view coverage totals.
