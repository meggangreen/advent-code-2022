from inputs import T10, I10

# toggle data for Test or Input
data = I10.split('\n')[::-1]

cycles, register = 0, 1
strength, crt = [], []
instructions = {'addx': 2, 'noop': 1}
while data:
    inst = data.pop().split()
    for _ in range(instructions[inst[0]]):
        cycles += 1
        if cycles in [20, 60, 100, 140, 180, 220]:
            strength.append(cycles * register)
    if inst[0] == 'addx':
        register += int(inst[1])

print(f"Part 1: {sum(strength)}")   # 13920
