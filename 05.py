import re
from inputs import T05_stacks, T05_moves, I05_stacks, I05_moves

def prep_data():# toggle data for Test or Input
    stacks = {n: stack.split(',') for n, stack in I05_stacks.items()}
    # print(stacks)
    moves = [tuple(map(int, re.findall('\d+', move))) for move in I05_moves.split('\n')]
    # print(moves)
    return (stacks, moves)


def do_part1():
    stacks, moves = prep_data()
    for move in moves:
        i, pre, post = move
        while i > 0:
            stacks[post].append(stacks[pre].pop())
            i += -1

    answer = ''.join([stacks[s][-1] for s in stacks])
    print(f"Part 1: {answer}")    # QMBMJDFTD


def do_part2():
    stacks, moves = prep_data()
    for move in moves:
        i, pre, post = move
        crates = stacks[pre][-i:]
        stacks[pre][-i:] = []
        stacks[post].extend(crates)

    answer = ''.join([stacks[s][-1] for s in stacks])
    print(f"Part 2 : {answer}")    # NBTVTJNFJ


if __name__ == '__main__':
    do_part1()
    do_part2()