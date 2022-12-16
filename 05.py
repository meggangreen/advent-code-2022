import re
from inputs import T05_stacks, T05_moves, I05_stacks, I05_moves

# toggle data for Test or Input
stacks = I05_stacks
for stack in stacks:
    stacks[stack] = stacks[stack].split(',')
# print(stacks)
moves = [tuple(map(int, re.findall('\d+', move))) for move in I05_moves.split('\n')]
# print(moves)

for move in moves:
    i, pre, post = move
    while i > 0:
        stacks[post].append(stacks[pre].pop())
        i += -1

answer = ''.join([stacks[s][-1] for s in stacks])
print(f"Part 1: {answer}")    # QMBMJDFTD


