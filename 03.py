from inputs import T03

# toggle data for Test or Input
data = T03

rucksacks = [(chars[:len(chars)//2], chars[len(chars)//2:]) for chars in data.split('\n')]

vals = 0
for rucksack in rucksacks:
    r1, r2 = set(rucksack[0]), set(rucksack[1])
    v = ord(list(r1 & r2)[0])
    if v >= 97:
        vals += v - 96
    else:
        vals += v - 38


print(f"Part 1: {vals}")

