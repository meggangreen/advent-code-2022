from inputs import T09, I09

# toggle data for Test or Input
data = I09.split('\n')

class Rope(object):
    """ docstring for Rope """

    compass = {'U': 1j, 'D': -1j, 'R': 1, 'L': -1}
    corrections = {(-2-1j): (-1-1j), (-2+0j): (-1+0j), (-2+1j): (-1+1j),
                   (+2-1j): (+1-1j), (+2+0j): (+1+0j), (+2+1j): (+1+1j),
                   (-1-2j): (-1-1j), (0-2j): (0-1j), (-1+2j): (-1+1j),
                   (+1-2j): (+1-1j), (0+2j): (0+1j), (+1+2j): (+1+1j)}

    def __init__(self, H, T):
        super(Rope, self).__init__()
        self.H = H or 0+0j
        self.T = T or 0+0j
        self.T_visited = set()
        self.T_visited.add(self.T)

    def __repr__(self):
        return f"<Rope H={self.H} T={self.T} >"

    def move_H(self, direction, steps):
        """ Move the head as instructed. Moving the head necessarily moves the tail. """
        for i in range(steps):
            self.H += self.compass[direction]
            self._move_T()

    def _move_T(self):
        distance = self.H - self.T
        self.T += self.corrections.get(distance, 0)
        self.T_visited.add(self.T)

r = Rope(0,0)
for line in data:
    direction, steps = line.split()
    r.move_H(direction, int(steps))

print(f"Part One: {len(r.T_visited)}")  # 6339


# https://www.reddit.com/r/adventofcode/comments/zgnice/comment/izhzxb6/?utm_source=share&utm_medium=web2x&context=3
# https://topaz.github.io/paste/#XQAAAQDYAQAAAAAAAAA5G8pm5rq2zGEq3FAnMmnq8EER0UoD/ZrEuZHeyNjL79bpZLXfg/Dbz424aybsPDyjUN1dpuHMGZn4ncEbddEKyH1V5oJxNIugTQYA3a0cg3tPo+1+xICju6pge5dxTN1gMMRkxmRSnVmqaS4/mppv4aO0g0/4qq8pDfs+1MMhAxsKcMsZLfoW/sMz8uQSt8wUrld9CbEbjBoMIwyvn2iz+zHG+akaQtqO2OKeZImV4dvBK/c74Xb2Y0LE8oQbz+gXadim+4L9LIw7aJHgJ/PbYZ0XkaiqhSa8GHdRwosEbaQ9Q8YjWhAlGlThJfLj9Tf7CqDCASr/xFWvTuAlOrdqb5EhjNdtJ+joNXcFJ2wTAqQ4X/RFVi7/7cYS+A==
rope = [0] * 10
seen = [set([x]) for x in rope]
dirs = {'L':+1, 'R':-1, 'D':1j, 'U':-1j}

# False = 0 and True = 1, gd genius move
sign = lambda x: complex((x.real>0) - (x.real<0), (x.imag>0) - (x.imag<0))

for line in data:
    for _ in range(int(line[2:])):
        rope[0] += dirs[line[0]]

        for i in range(1, 10):
            dist = rope[i-1] - rope[i]
            # abs works on complex numbers, absolutely infuriating
            if abs(dist) >= 2:
                rope[i] += sign(dist)
                seen[i].add(rope[i])

print(len(seen[1]), len(seen[9]))   # 6339 2541
