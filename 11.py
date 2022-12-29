from inputs import T11, I11
from collections import deque, defaultdict
import re
from math import prod

# toggle data for Test or Input
text = I11.split('\n\n')

class Monkey(object):
    """ docstring for Monkey """

    def __init__(self, digits):
        super(Monkey, self).__init__()
        self.name = int(digits[0])
        self.items = deque(map(int, digits[1:-6]))
        self.operation = ' '.join(digits[-6:-3])
        self.test = {'div': int(digits[-3]), True: int(digits[-2]), False: int(digits[-1])}
        self.num_inspections = 0
        self.current = None

    def __repr__(self):
        return f"<Monkey {self.name} {self.items} {self.num_inspections}>"

    def do_inspection(self):
        thrown_items = defaultdict(list)
        while self.items:
            self.current = self.items.popleft()
            self._operate()
            self._relieve()
            thrown_items[self._which_monkey()].append(self.current)
            self.current = None
            self.num_inspections += 1
        return thrown_items
    
    def _operate(self):
        old = self.current
        self.current = eval(self.operation)

    def _relieve(self):
        self.current = self.current // 3
    
    def _which_monkey(self):
        return self.test[self.current % self.test['div'] == 0]


class Jungle(object):
    def __init__(self, text):
        super(Jungle, self).__init__()
        self.monkeys = None
        self.rounds = 0

        monkeys = []
        for blob in text:
            digits = list(re.findall('[\d+*]+|old', blob))
            monkeys.append(Monkey(digits))
        self.monkeys = monkeys

    def __repr__(self):
        return f"<Jungle rounds={self.rounds}\n{self.monkeys}\n >"

    def monkey_go_round(self, i=1):
        for _ in range(i):
            for monkey in self.monkeys:
                thrown_items = monkey.do_inspection().items()
                for monkey, items in thrown_items:
                    self.monkeys[monkey].items.extend(items)
            self.rounds += 1    

    def calc_monkey_business(self, i=None):
        if i:
            self.monkey_go_round(i)
        #try using key in sort
        return prod(sorted([m.num_inspections for m in self.monkeys],reverse=True)[:2])
