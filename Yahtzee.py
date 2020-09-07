import random
from enum import Enum

def roll_dice(values=None, keep=None):
    if values == None: values = [0]*5
    if keep == None: keep = [False]*5
    if (type(values) != list): raise TypeError ("values must be a list")
    if (len(values) != 5): raise TypeError ("values must be length 5")
    if (type(values[0]) != int): raise TypeError ("values must be a list of integers")
    if (type(keep) != list): raise TypeError ("keep must be a list")
    if (len(keep) != 5): raise TypeError ("keep must be length 5")
    if (type(keep[0]) != bool): raise TypeError ("values must be a list of integers")
    for i in range(5):
        if not keep[i]:
            values[i] = random.randint(1,6)
    return
class YahtzeeRow(Enum):
    ones = 0
    twos = 1
    threes = 2
    fours = 3
    fives = 4
    sixes = 5
    threekind = 6
    fourkind = 7
    fullhouse = 8
    smstr = 9
    lgstr = 10
    chance = 11
    yahtzee = 12
    
class scoreSheet:
    scores=[-1] * 13
    extra_yahtzee = 0
    row_names=["ones", "twos", "threes", "fours", "fives", "sixes",
               "threekind", "fourkind", "fullhouse", "smstr",
               "lgstr", "chance", "yahtzee"]
    def upper_score(self,values, num):
        sum = 0
        for v in values:
            if v == num:
                sum = sum + num
        return num
    def ones(self,values):
        return upper_score(values,1)
    def twos(self,values):
        return upper_score(values,2)
    def threes(self,values):
        return upper_score(values,3)
    def fours(self,values):
        return upper_score(values,4)
    def fives(self,values):
        return upper_score(values,5)
    def sixes(self,values):
        return upper_score(values,6)
    def total_val(self,values):
        return sum(values)
    def verify_cnt(self, values, cnt):
        sort_vals = values.copy()
        sort_vals.sort()
        this_cnt = 1
        last_val = 0
        for v in sort_vals:
            if v == last_val:
                this_cnt = this_cnt + 1
                if this_cnt >= cnt: return True
            else:
                this_cnt = 1
            last_val = v
    def threekind(self,values):
        if (self.verify_cnt(values,3)):
            return self.total_val(values)
        return 0
    def fourkind(self,values):
        if (self.verify_cnt(values,4)):
            return self.total_val(values)
        return 0
    def fullhouse(self,values):
        sort_vals = values.copy()
        sort_vals.sort()
        if (sort_vals[0] != sort_vals[1]): return 0
        if (sort_vals[3] != sort_vals[4]): return 0
        if (sort_vals[1] == sort_vals[2] or
            sort_vals[2] == sort_vals[3]): return 25
        else: return 0
    def smstr(self,values):
        fail_cnt = 0
        sort_vals = values.copy()
        sort_vals.sort()
        last_val = sort_vals[0]-1
        for v in sort_vals:
            if v != last_val+1:
                fail_cnt = fail_cnt + 1
                if fail_cnt > 1: return 0
        return 30
    def lgstr(self,values):
        fail_cnt = 0
        sort_vals = values.copy()
        sort_vals.sort()
        last_val = sort_vals[0]-1
        for v in sort_vals:
            if v != last_val+1:
                return 0
        return 40
    def chance(self,values):
        return self.total_val(values)
    def yahtzee(self,values):
        if (self.verify_cnt(values,5)): return 50
        return 0
    def __init__(self):
        self.scores = [-1] * len(self.row_names)
        self.row_funcs = [self.ones, self.twos, self.threes, self.fours, self.fives, self.sixes,
                     self.threekind, self.fourkind, self.fullhouse, self.smstr,
                     self.lgstr, self.chance, self.yahtzee]
        self.extra_yahtzee = 0
    def compute_score(self):
        sum=0
        for s in self.scores:
            sum = sum + max(0,s)
        return sum + 100 * self.extra_yahtzee
    def row_name(self,row):
        return self.row_names[row]
    def score(self,values, row):
        if row == 12 and self.scores[row] == 50 and self.yahtzee(values) == 50:
            self.extra_yahtzee = self.extra_yahtzee + 1
        if (self.scores[row] == -1): self.scores[row] = self.row_funcs[row](values)
    
if __name__ == "__main__":
    values = [0] * 5
    keep = [False] * 5
    roll_dice(values,keep)
    print(values)
    keep[3] = True
    keep[4] = True
    new_vals = values.copy()
    roll_dice(new_vals,keep)
    print(new_vals)
    if values[3] != new_vals[3] or values[4] != new_vals[4]:
        print("ERROR! Kept values weren't kept.")
    sheet = scoreSheet()
    values=[4,4,4,4,4]
    sheet.score(values,YahtzeeRow.yahtzee.value)
    if sheet.compute_score() != 50:
        print ("ERROR! Yahtzee miscomputed")
    values=[1,4,1,1,4]
    sheet.score(values,YahtzeeRow.fullhouse.value)
    if sheet.compute_score() != 75:
        print ("ERROR! Full house miscomputed")
    values=[2,5,6,5,3]
    sheet.score(values,YahtzeeRow.threekind.value)
    if sheet.compute_score() != 75:
        print ("ERROR! Bad three kind miscomputed")
    values=[2,2,6,2,5]
    sheet.score(values,YahtzeeRow.threekind.value)
    if sheet.compute_score() != 75:
        print ("ERROR! Late three kind miscomputed")
    values=[1,1,1,1,1]
    sheet.score(values,YahtzeeRow.yahtzee.value)
    if sheet.compute_score() != 175:
        print ("ERROR! Second Yahtzee miscomputed")
    values=[6,4,4,5,2]
    sheet.score(values,YahtzeeRow.chance.value)
    if sheet.compute_score() != 196:
        print ("ERROR! chance miscomputed")
