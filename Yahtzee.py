import Dice
import Scoresheet
from ManualPlayer import player

def one_turn(sheet, decider):
    values = [0] * 5
    keep = [False] * 5
    Dice.roll_dice(values,keep)
    print("Your scoresheet:")
    for q in range(13):
        print(Scoresheet.row_names[q] + "  " + str(sheet.scores[q]))
    for q in range(2):
        keep=decider.choose_keep(values.copy(), sheet.scores.copy(), q)
        print (keep)
        Dice.roll_dice(values,keep)
        print(values)
    row = decider.choose_row(values.copy(), sheet.scores.copy())
    # If the decider chooses a row that's full, start from the bottom, find
    # an unfilled row and apply there. Otherwise deciders could cheat by
    # specifying filled rows and getting extra turns
    if sheet.scores[row] != -1:
        print("Row " + str(row) + " is already full!!!")
        sheet.score(values,row)
        row = 12
        while(sheet.scores[row] != -1 and row >0):
            row = row-1
        print("Applying to " + sheet.row_names[row])
    sheet.scores[row] = sheet.row_funcs[row](values)

n_players = 0
while(n_players == 0):
    try:
        n_players = int(input("How many players?  "))
    except:
        print("Please enter a number between 1 and 8")
        n_players = 0

sheets = [Scoresheet.scoreSheet() for i in range(n_players)]
players = [player() for i in range(n_players)]

done = False
while( not done):
    done = True
    for q in range(n_players):
        if not sheets[q].full():
            print("Player " + str(q) + ", take your turn.")
            one_turn(sheets[q], players[q])
            done = False

print("Player    Score")
for q in range(n_players):
    print(" " + str(q) + "          " + str(sheets[q].compute_score()))
