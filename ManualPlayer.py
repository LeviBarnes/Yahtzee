from Scoresheet import row_names

class player:
    def choose_keep(self, values, scores, rerolls):
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
        return keep
    def choose_row(self, values, scores):
        print('Your dice: ' + ' '.join([str(q) for q in values]))
        print("Your scoresheet:")
        for q in range(13):
            print(str(q) + "  " + row_names[q] + "  " + str(scores[q]))
        row = None
        while(type(row) != int):
            try:
                row = int(input("Apply to which row?  "))
                if (row <  0 or row > 12):
                    raise()
            except:
                print("Please enter an integer between 1 and 13.")
                row = None
        return row

        
