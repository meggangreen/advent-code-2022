from inputs import I01

def part_1_and_2():
    data = I01.split('\n\n')
    elves = []
        for elf in data:
            cals = sum([int(n) for n in elf.split('\n')])
            elves.append(cals)

    print(f"Part 1: {max(elves)}")    # 70374

    total_cals = 0
    for i in range(0,3):
        curr_max = max(elves)
        total_cals += curr_max
        for e, cal in enumerate(elves):
            if cal == curr_max:
                elves[e] = 0
                break

    print(f"Part 2: {total_cals}")    # 204610
