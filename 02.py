from inputs import I02, T02

data = I02
plays = [play.split(' ') for play in data.split('\n')]

exchange = {'A': 1, 'B': 2, 'C': 3,
            'X': 1, 'Y': 2, 'Z': 3,
            -2: 0, -1: 6, 0: 3, 1: 0, 2: 6}

score = 0
for p1, p2 in plays:
    score += exchange[p2]
    score += exchange[exchange[p1] - exchange[p2]]

print(f"Part 1: {score}")    # 13526 (15 for test)

exchange = {'A': 1, 'B': 2, 'C': 3,
            'X': 0, 'Y': 3, 'Z': 6,
            (0,1): 3, (0,2): 1, (0,3): 2,
            (6,1): 2, (6,2): 3, (6,3): 1}

score = 0
for p1, p2 in plays:
    score += exchange[p2]
    if exchange[p2] == 3:
        score += exchange[p1]
    else: # really just need to get the value to the right (lose) or left (win) but i didn't want to code the "if index is less than/greater than bounds"
        score += exchange[(exchange[p2], exchange[p1])]
        # could have used a deque with rotate to find the answer and then rotate to original

print(f"Part 2: {score}")    # 14204 (12 for test)
