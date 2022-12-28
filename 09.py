from inputs import T09, I09

# toggle data for Test or Input
data = T09.split('\n')

start = 0+0j

class Rope(object):
    """ docstring for Rope """
    def __init__(self, H, T):
        super(Rope, self).__init__()
        self.H = H or 0+0j
        self.T = T or 0+0j

    def __repr__(self):
        return f"<Rope H={self.H} T={self.T} >"

    def move_H(self, move):
        """ Move the head as instructed by move, a complex number. Moving the head necessarily moves the tail. """
        self.H += move
        self._move_T()
        print(self)

    def _move_T(self):
        corrections = {(-2-1j): (1+1j), (-2+0j): (1+0j), (-2+1j): (1-1j),
                       (2-1j): (-1+1j), (2+0j): (-1+0j), (2+1j): (-1-1j)}
        distance = self.H - self.T
        self.T += corrections[distance]
        if distance.real == 0 and distance.imag > 1:
            self.T += distance - (0+1j)
        elif distance.imag == 0 and distance.real > 1:
            self.T += distance - (1+0j)

