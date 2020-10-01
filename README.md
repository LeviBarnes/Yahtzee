## Yahtzee
Yahtzee game

# Dependencies
Pillow (Python image library) - for YahtzeeGUI.py
Tcl/Tk -for YahtzeeGUI.py

# Play via command line
python3 Yahtzee.py

Specify dice as a comma-separated list. Dice are numbered starting at 0

# Play in the GUI (requires Pillow, Tcl/Tk)
python3 YahtzeeGUI.py

# Create your own CPU player
Model your player after ManualPlayer.py. Create a "player" class with two public member
functions, choose_keep, and choose_row.

__choose_keep(self, values, scores, rerolls):__
>    *values* - current dice values, list of 5 integers (1-6)
>    
>    *scores* - list of 13 scores on your scoresheet. -1 indicates that row is unfilled. The
>    names of the rows can be found in Scoresheet.row_names
>
>    *rerolls* - the number of times you've rolled the dice. You can only keep and re-roll
>    twice before you must score the dice

The function should return a list of 5 boolean values. True indicates you do not want
to re-roll that die.

__choose_row(self, values, scores):__
>    *values* - current dice values, list of 5 integers (1-6)
>
>    *scores* - list of 13 scores on your scoresheet. -1 indicates that row is unfilled. The
>    names of the rows can be found in Scoresheet.row_names

The function should return the row number to which you want to apply these dice. The
row names can be found in Scoresheet.row_names. If you select a row that is already
full, you'll lose your opportunity to score.

