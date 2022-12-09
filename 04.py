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

print(f"Part 2: {count}")    #806


# I like this one better though
# https://topaz.github.io/paste/#XQAAAQBhAQAAAAAAAAA0m0pnuFI8c/T1e9wHxCKuscg9AMzaBLqTZh8ox9OSPEmMWHqqdqQkUt+MFSCjb9uFPLiWkB0t5amF4A0bHW20JuNZpR1ralYd4P4bahdS7T9wVceoBN+kbAxk3yZG+YnA37bP1meGuc+vvr451/g9UhTF16/+567hxek1NHy56bv1CKo1nB6bnbPALu5x7fK4aT1wFFX4I2xfOc9seO/pUCZcHYmbsCHZQ/Oc4RA/F/PRTZh4NVM+5P5+zoXhvNFQWGotTq/qTXQhoY8WVf17JESydKtdyqJB59Vf+gV58A==
# https://www.reddit.com/r/adventofcode/comments/zc0zta/comment/iyu9kr5/?utm_source=share&utm_medium=web2x&context=3
import re

answer1 = 0
answer2 = 0

for l in data.split('\n'):
    nums = list(map(int, re.findall('\d+', l)))

    s1 = set(range(nums[0], nums[1]+1))
    s2 = set(range(nums[2], nums[3]+1))

    if s1 <= s2 or s2 <= s1:
        answer1 += 1

    if s1 & s2:
        answer2 += 1

print(answer1, answer2)