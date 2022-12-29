from inputs import T10, I10

# toggle data for Test or Input
data = I10.split('\n')[::-1]

cycles, register, strength = 0, 1, []
crt = [['.'] * 40, ['.'] * 40, ['.'] * 40, ['.'] * 40, ['.'] * 40, ['.'] * 40]
instructions = {'addx': 2, 'noop': 1}
while data:
    inst = data.pop().split()
    for _ in range(instructions[inst[0]]):
        cycles += 1
        if cycles in [20, 60, 100, 140, 180, 220]:
            strength.append(cycles * register)
        row = cycles // 41
        pixel = (cycles - 1) % 40
        if (register -1) <= pixel <= (register+1):
            crt[row][pixel] = '#'
    if inst[0] == 'addx':
        register += int(inst[1])

for i, row in enumerate(crt):
    crt[i] = ''.join(row)

print(f"Part 1: {sum(strength)}")   # 13920
print("Part 2:", '\n'.join(crt), sep='\n')  # EGLHBLFJ
