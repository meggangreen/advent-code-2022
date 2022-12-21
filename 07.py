from collections import defaultdict
from itertools import accumulate
from inputs import T07, I07

# toggle data for Test or Input
data = I07.split('\n')

paths = []
sizes = defaultdict(int)    # dd to prevent key error on first go

for instruction in data:
    match instruction.split():
        case ['$', 'cd', '..']: paths.pop()
        case ['$', 'cd', folder]: paths.append(f"{folder}/")
        case ['$', _]: pass
        case ['dir', _]: pass
        case [size, _]:
            for path in accumulate(paths):
                sizes[path] += int(size)

print(f"Part 1: {sum(s for s in sizes.values() if s <= 100_000)}")    # 1432936
print(f"Part 2: {min(s for s in sizes.values() if s >= sizes['//'] - 40_000_000)}")    # 272298


# with help from:
# https://www.reddit.com/r/adventofcode/comments/zesk40/comment/iz8fww6/?utm_source=share&utm_medium=web2x&context=3
# https://www.reddit.com/r/adventofcode/comments/zesk40/comment/iz93c8u/?utm_source=share&utm_medium=web2x&context=3
# https://www.reddit.com/r/adventofcode/comments/zesk40/comment/iz8zntk/?utm_source=share&utm_medium=web2x&context=3
