import Dice
import Scoresheet

def one_turn(sheet):
    values = [0] * 5
    keep = [False] * 5
    Dice.roll_dice(values,keep)
    print("Your scoresheet:")
    for q in range(13):
        print(sheet.row_names[q] + "  " + str(sheet.scores[q]))
    for q in range(2):
        keep=None
        while (keep == None):
            try:
                print('Your dice: ' + ' '.join([str(q) for q in values]))
                keep_str = input("Keep which dice?  ")
                keep_list = [int(q) for q in keep_str.split(',')]
                keep = [q in keep_list for q in range(5)]
            except:
                keep = None
                print('Please enter a comma-separated list of integers (e.g. 2,4,5)')
        Dice.roll_dice(values,keep)
    print('Your dice: ' + ' '.join([str(q) for q in values]))
    print("Your scoresheet:")
    for q in range(13):
        print(str(q) + "  " + sheet.row_names[q] + "  " + str(sheet.scores[q]))
    row = None
    while(type(row) != int):
        try:
            row = int(input("Apply to which row?  "))
            if (row <  0 or row > 12):
                raise()
        except:
            print("Please enter an integer between 1 and 13.")
            row = None
    sheet.score(values,row)

A = Scoresheet.scoreSheet()
one_turn(A)
one_turn(A)
n_players = 0
while(n_players == 0):
    try:
        n_players = int(input("How many players?  "))
    except:
        print("Please enter a number between 1 and 8")
        n_players = 0

sheets = [Scoresheet.scoreSheet() for i in range(n_players)]

    
    
        
done = False
while( not done):
    done = True
    for q in range(n_players):
        if not sheets[q].full():
            print("Player " + str(q) + ", take your turn.")
            one_turn(sheets[q])
            done = False

print("Player    Score")
for q in range(n_players):
    print(" " + str(q) + "          " + str(sheets[q].compute_score()))
