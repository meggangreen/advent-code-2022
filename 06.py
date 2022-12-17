from inputs import T06, I06

# toggle data for Test or Input
data = I06.split('\n')

for d in data:
    for i in range(3,len(d)):
        if len(set(d[i-3:i+1])) == 4:
            print(f"Part 1: {i+1}")    # 1723
            break
