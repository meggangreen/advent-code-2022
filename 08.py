# views slicing and partial from https://github.com/AlexTelon/AdventOfCode/blob/master/2022/8/solve.py

from inputs import T08, I08
from functools import partial
from math import prod

# toggle data for Test or Input
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

def one_view_score(tree, view):
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
        view_score = partial(one_view_score, tree)
        total_score = prod(map(view_score, all_views))
        p2 = total_score if total_score > p2 else p2

print(f"Part One: {p1}")    # 1690
print(f"Part Two: {p2}")    # 535680
