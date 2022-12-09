from inputs import T04

# toggle data for Test or Input
data = T04

pairs = [[[int(n) for n in assign.split('-')] for assign in line.split(',')] for line in data.split('\n')]

count = 0
for pair in pairs:
    L1 = pair[0][0]
    U1 = pair[0][1]
    L2 = pair[1][0]
    U2 = pair[1][1]

    if (((L1 <= L2 ) & (U1>=U2)) | ((L2 <= L1 ) & (U2>=U1))):
        count += 1

print(count)