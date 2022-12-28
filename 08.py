# views slicing from https://github.com/AlexTelon/AdventOfCode/blob/master/2022/8/solve.py

from inputs import T08, I08

# toggle data for Test or Input
# data = [line.split() for line in T08.split('\n')]

from functools import partial
from math import prod

rows = []
for y, row in enumerate(I08.split('\n')):
    rows.append(list(map(int,row)))

cols = list(zip(*rows))

def views(x, y):
    """Returns the view in the 4 directions from a given position.
    The order is defined as in aoc. above, left, right, below
    Also they are ordered as seen from the (x,y) coordinate.
    """
    above = cols[x][:y]
    left  = rows[y][:x]
    right = rows[y][x+1:]
    below = cols[x][y+1:]
    # print(x, y, [above[::-1], left[::-1], right, below])
    return [above[::-1], left[::-1], right, below]

def view_score(tree, view):
    """The score for the given view"""
    score = 0
    for num in view:
        score += 1
        if num >= tree:
            break
    return score

p1 = 0
p2 = 0
for y, row in enumerate(rows):
    for x, tree in enumerate(row):
        # print(x,y)
        # for other in views(x,y):
        #     print(other, max(other or [-1]))
        #     if tree > max(other or [-1]):
        #         print(tree)
        all_views = views(x, y)
        if any(tree > max(others or [-1]) for others in all_views):
            p1 += 1

print(f"Part One: {p1}")    # 1690
