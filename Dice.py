import random

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
