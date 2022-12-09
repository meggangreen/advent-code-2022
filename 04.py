from inputs import T04, I04

# toggle data for Test or Input
data = I04

pairs = [[[int(n) for n in assign.split('-')] for assign in line.split(',')] for line in data.split('\n')]

count = 0
for pair in pairs:
    L1 = pair[0][0]
    U1 = pair[0][1]
    L2 = pair[1][0]
    U2 = pair[1][1]

    if (((L1 <= L2 ) & (U1>=U2)) | ((L2 <= L1 ) & (U2>=U1))):
        count += 1

print(f"Part 1: {count}")    # 413


count = 0
for pair in pairs:
    L1 = pair[0][0]
    U1 = pair[0][1]
    L2 = pair[1][0]
    U2 = pair[1][1]

    if (((L1 <= L2) & (U1>=U2)) | ((L2 <= L1) & (U2>=U1)) | ((U1 >= L2)  & (L1<=U2))):
        count += 1

print(f"Part 2: {count}")