""" Generates experience/level table

Based on this formula:
http://howtomakeanrpg.com/a/how-to-make-an-rpg-levels.html
"""
import math


def create_xp_table(start=1, end=100, base_xp=10, exponent=1.5):
    """ Creates an experience/level table
    
    Keyword Arguments:
        start {int} -- [description] (default: {1})
        end {int} -- [description] (default: {100})
        base_xp {int} -- [description] (default: {1000})
        exponent {float} -- [description] (default: {1.5})
    
    Returns:
        list -- experience points needed to reach this level
    """

    levels = [0]
    
    for level in range( start, end):
        xp = math.floor(base_xp * math.pow(level, float(exponent)))
        levels.append(xp)

    return levels


def show_xp_table(xp_table):
    """ Print experience points needed for each level
    
    Arguments:
        level_table {list} -- experience points needed to reach each level
    """

    for level, xp in enumerate(xp_table):
        print(f"Level {level} = {xp}")



def main():
    xp_table = create_xp_table(start=1, end=20, base_xp=100, exponent=1.5)
    show_xp_table(xp_table)



if __name__ == '__main__':
    main()
