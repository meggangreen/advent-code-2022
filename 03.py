from inputs import T03, I03

# toggle data for Test or Input
data = I03

rucksacks = data.split('\n')

vals = 0
for rs in rucksacks:
    v = ord(list(set(rs[:len(rs)//2]) & set(rs[len(rs)//2:]))[0])
    if v >= 97:
        vals += v - 96
    else:
        vals += v - 38

print(f"Part 1: {vals}")    # 7766


vals = 0
i = 0
while i < len(rucksacks):
    v = ord(list(set(rucksacks[i+0]) & set(rucksacks[i+1]) & set(rucksacks[i+2]))[0])
    if v >= 97:
        vals += v - 96
    else:
        vals += v - 38
    i += 3

print(f"Part 2: {vals}")    # 2415
