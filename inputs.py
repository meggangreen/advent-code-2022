T11 = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

I11 = """Monkey 0:
  Starting items: 73, 77
  Operation: new = old * 5
  Test: divisible by 11
    If true: throw to monkey 6
    If false: throw to monkey 5

Monkey 1:
  Starting items: 57, 88, 80
  Operation: new = old + 5
  Test: divisible by 19
    If true: throw to monkey 6
    If false: throw to monkey 0

Monkey 2:
  Starting items: 61, 81, 84, 69, 77, 88
  Operation: new = old * 19
  Test: divisible by 5
    If true: throw to monkey 3
    If false: throw to monkey 1

Monkey 3:
  Starting items: 78, 89, 71, 60, 81, 84, 87, 75
  Operation: new = old + 7
  Test: divisible by 3
    If true: throw to monkey 1
    If false: throw to monkey 0

Monkey 4:
  Starting items: 60, 76, 90, 63, 86, 87, 89
  Operation: new = old + 2
  Test: divisible by 13
    If true: throw to monkey 2
    If false: throw to monkey 7

Monkey 5:
  Starting items: 88
  Operation: new = old + 1
  Test: divisible by 17
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 6:
  Starting items: 84, 98, 78, 85
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 5
    If false: throw to monkey 4

Monkey 7:
  Starting items: 98, 89, 78, 73, 71
  Operation: new = old + 4
  Test: divisible by 2
    If true: throw to monkey 3
    If false: throw to monkey 2"""


T10 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

I10 = """addx 1
noop
noop
addx 4
addx 5
addx -2
addx 19
addx -12
addx 3
addx -2
addx 4
noop
noop
noop
addx 3
addx -8
addx 15
addx 1
noop
noop
addx 6
addx -1
noop
addx -38
noop
addx 10
addx -5
noop
addx 3
addx 2
addx 7
noop
noop
addx 3
noop
addx 2
addx 3
addx -2
addx 2
addx 7
noop
noop
addx 9
noop
addx -12
noop
addx 11
addx -38
noop
noop
noop
addx 5
addx 5
noop
noop
noop
addx 3
addx -12
addx 14
noop
addx 1
addx 3
addx 1
addx 5
addx 4
addx 1
noop
noop
noop
noop
noop
addx -9
addx 17
addx -39
addx 38
addx -8
addx -26
addx 3
addx 4
addx 16
noop
addx -11
addx 3
noop
addx 2
addx 3
addx -2
addx 2
noop
addx 13
addx -8
noop
addx 7
addx -5
addx 8
addx -40
addx 16
addx -9
noop
addx -7
addx 8
addx 2
addx 7
noop
noop
addx -15
addx 16
addx 2
addx 5
addx 2
addx -20
addx 12
addx 11
addx 8
addx -1
addx 3
noop
addx -39
addx 2
noop
addx 5
noop
noop
noop
addx 4
addx 1
noop
noop
addx 2
addx 5
addx 2
addx 1
addx 4
addx -1
addx 2
noop
addx 2
noop
addx 8
noop
noop
noop
addx -10
noop
noop"""


T09 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

I09 = """U 2
L 1
U 1
D 2
L 2
D 1
L 2
R 2
D 2
U 2
L 2
D 1
L 2
U 1
R 2
D 2
R 1
U 1
R 1
L 1
D 2
R 1
D 2
R 2
D 2
L 2
U 1
R 1
L 1
D 2
L 1
R 1
U 1
D 1
R 1
D 2
R 2
L 1
R 2
L 2
U 1
L 1
D 2
U 2
D 1
R 2
L 2
D 1
R 1
D 2
U 1
D 2
R 2
U 2
L 2
D 2
R 2
L 1
D 2
L 1
U 2
R 1
L 2
U 1
R 2
U 1
D 2
R 2
U 1
D 2
L 2
D 2
L 1
R 1
D 1
L 2
D 2
U 2
R 1
U 1
R 2
U 2
L 2
R 2
L 2
R 1
U 2
L 2
R 1
D 1
L 1
D 1
U 2
R 1
U 2
R 2
U 2
L 2
U 2
L 2
U 1
R 1
U 2
R 2
L 2
R 2
U 1
R 1
D 1
U 1
L 2
R 3
L 2
U 3
L 1
R 1
U 1
D 1
U 1
D 1
R 3
U 3
L 3
U 1
R 2
D 1
U 2
D 2
U 3
L 2
U 3
R 1
L 2
U 1
L 2
D 2
U 3
D 1
R 3
U 3
R 3
L 1
D 2
U 2
D 3
U 1
R 2
L 1
D 1
L 1
D 3
R 1
U 2
L 2
D 2
U 3
D 2
U 1
D 3
U 2
L 3
R 2
D 2
R 3
L 3
R 1
D 1
L 2
R 1
D 2
L 3
R 2
U 1
L 3
D 2
R 3
D 3
U 1
L 1
D 3
U 3
D 3
R 3
U 1
D 1
L 1
R 3
L 3
U 1
D 3
R 1
L 3
R 3
D 2
L 3
D 3
U 3
L 1
U 1
L 2
D 3
L 2
U 3
L 3
U 1
R 2
D 3
U 2
R 2
U 1
L 2
D 2
L 2
D 1
U 3
D 1
L 1
U 2
D 1
R 2
L 2
R 3
L 2
R 1
D 1
R 1
D 2
L 4
D 3
R 3
D 4
L 3
D 1
U 2
D 1
L 4
R 4
L 3
R 2
L 1
R 2
D 1
R 1
D 4
U 1
D 2
R 3
D 3
R 2
U 1
D 2
U 2
L 1
D 3
U 4
L 3
U 2
L 4
D 4
L 1
U 3
D 2
R 3
D 2
L 2
U 3
L 3
R 2
D 2
R 2
U 3
L 2
R 4
L 4
U 1
D 3
L 2
R 3
L 2
R 3
D 4
R 1
L 1
U 1
L 2
D 3
L 4
R 2
D 2
U 3
D 4
L 3
R 1
U 4
L 3
D 4
L 1
D 3
L 4
R 2
L 1
R 4
L 4
U 3
D 4
U 1
R 2
D 3
U 3
R 2
L 2
R 2
U 4
L 4
D 4
L 3
D 3
U 1
D 1
U 4
R 1
L 2
U 2
L 3
U 3
L 3
D 1
L 2
U 3
L 3
U 2
L 2
U 2
L 4
R 1
L 2
D 2
R 3
L 5
U 1
R 5
D 3
L 5
U 3
D 1
L 3
R 2
D 2
U 3
R 5
D 5
R 1
D 4
U 1
R 1
L 4
D 1
U 3
D 4
L 1
D 1
L 2
U 1
L 3
R 1
D 1
U 1
D 2
L 5
U 2
R 3
D 4
L 4
R 1
L 4
R 5
D 4
R 4
L 4
U 3
L 3
R 1
D 1
R 4
U 1
R 3
U 5
R 5
D 2
R 4
D 5
L 2
D 4
U 4
R 3
D 2
L 5
R 4
D 4
L 1
D 4
L 4
D 4
R 2
D 5
L 4
U 3
D 5
U 5
L 1
U 3
L 2
U 2
R 2
U 3
D 3
R 1
L 3
R 1
U 4
D 1
R 1
L 1
R 4
L 1
R 3
D 4
U 5
L 4
U 5
L 5
U 4
L 3
D 2
L 1
U 1
R 4
L 5
D 3
U 3
L 2
D 1
L 1
U 4
R 6
U 5
L 4
R 3
U 4
L 5
U 3
D 1
U 3
R 4
L 3
D 6
R 1
L 2
U 6
D 6
R 2
L 4
D 1
R 5
L 3
D 1
R 2
D 3
L 6
U 5
D 1
U 2
R 2
L 5
U 1
D 3
R 5
D 2
L 1
D 6
R 4
D 5
L 1
R 2
L 3
R 4
L 6
U 5
L 3
D 4
R 4
U 1
D 3
R 4
L 4
R 1
U 2
R 6
D 1
L 4
R 2
D 5
R 6
D 3
R 5
L 1
R 2
U 2
D 2
L 4
D 6
L 1
R 2
U 3
D 6
L 1
R 3
L 1
D 1
R 6
D 6
L 1
U 4
L 4
U 6
R 6
L 6
D 1
U 2
R 6
L 6
U 6
D 1
R 5
U 4
R 2
L 2
R 5
U 5
R 6
U 2
D 3
R 6
D 2
R 3
L 6
U 5
R 2
D 5
L 3
D 5
U 2
D 4
L 1
D 3
U 1
L 4
D 2
L 3
U 5
R 5
L 3
D 7
R 5
L 5
U 5
L 7
U 3
L 2
R 5
D 1
R 4
U 1
R 5
U 6
R 1
L 3
U 7
L 6
R 2
L 3
U 6
L 4
D 1
L 6
U 2
L 6
U 2
L 4
U 2
L 4
U 4
D 3
U 1
R 1
U 5
L 2
R 3
D 7
R 4
U 4
R 1
D 1
L 7
R 2
U 3
D 1
U 1
D 1
L 2
R 5
U 2
R 5
U 7
L 2
R 6
U 2
R 1
L 7
U 2
R 3
U 2
R 7
D 7
R 6
U 4
L 1
R 1
U 6
R 6
U 1
L 7
R 6
L 2
U 5
L 3
R 4
D 4
R 6
L 5
D 1
U 4
D 6
L 4
R 4
D 1
L 3
U 2
L 7
R 2
U 7
R 3
L 6
D 6
U 3
D 7
U 7
D 7
R 7
U 5
L 2
U 5
D 4
L 4
U 2
L 6
U 4
D 3
L 6
U 7
R 3
D 2
U 2
L 7
D 5
L 2
U 6
R 8
D 7
R 5
U 5
R 3
L 1
U 6
R 3
D 7
U 3
R 4
U 5
D 4
R 1
D 6
L 7
D 2
R 5
U 4
L 1
R 1
L 7
U 6
D 1
L 1
D 8
U 1
L 7
R 1
U 6
D 6
L 4
U 1
L 3
D 6
R 6
D 3
R 7
U 3
L 7
R 6
L 3
D 2
L 4
U 1
R 1
D 7
L 8
R 1
L 7
D 1
L 1
R 3
U 1
R 8
L 6
D 3
U 3
R 2
D 7
R 6
L 2
R 1
U 4
R 6
L 6
D 4
L 4
U 6
L 2
U 7
D 3
R 3
L 5
R 7
D 7
U 8
L 6
U 6
D 7
L 8
U 8
L 6
U 1
D 1
U 8
D 5
R 5
U 7
D 3
U 3
D 2
U 4
L 6
D 6
L 2
D 4
R 2
L 7
R 4
U 4
D 6
R 7
D 6
U 1
D 2
U 1
D 4
L 2
R 4
L 7
U 5
L 3
D 6
U 5
L 6
U 3
L 3
U 1
D 1
L 6
U 3
L 8
D 3
R 7
L 2
U 8
R 5
U 8
R 9
U 9
L 8
U 5
D 3
U 4
R 8
U 4
L 6
R 6
L 8
R 8
U 2
L 2
R 5
D 7
L 3
D 4
L 5
D 1
R 7
D 6
R 6
D 2
R 8
U 8
R 2
D 4
U 3
R 4
U 2
L 3
U 4
D 5
R 4
U 9
D 4
R 7
L 1
D 7
U 6
L 1
U 3
D 8
R 3
U 4
D 2
L 6
R 8
D 5
R 5
D 1
U 2
L 7
D 7
U 6
D 3
U 6
R 9
U 2
L 7
U 4
L 7
U 4
D 3
U 9
R 5
D 2
U 1
L 6
D 2
L 8
U 5
R 3
U 9
R 2
U 9
L 7
D 6
L 4
R 1
L 4
D 5
R 5
L 1
R 8
L 7
U 2
R 9
L 1
R 2
D 4
U 5
R 5
L 10
D 7
U 7
R 9
L 1
R 9
D 7
U 4
L 8
U 9
R 10
D 3
U 2
D 2
L 10
R 7
L 2
R 4
U 10
R 7
D 5
L 7
R 8
D 6
R 6
U 1
R 1
L 4
D 7
R 10
L 3
U 4
D 10
L 5
R 10
D 7
U 2
D 8
L 5
R 2
D 5
U 9
R 6
L 6
U 5
L 3
R 3
D 6
L 3
U 4
D 10
L 6
U 7
L 4
D 5
L 4
D 8
R 5
U 8
R 8
L 1
D 4
R 7
U 5
D 3
L 5
D 3
L 7
U 7
R 4
U 1
R 7
L 3
R 3
D 2
U 6
D 6
U 1
R 6
D 1
U 4
R 5
D 3
R 8
L 2
D 10
L 7
D 10
U 9
D 6
U 3
L 8
U 9
R 10
D 10
R 5
L 10
D 6
L 6
R 11
D 6
L 1
R 8
U 10
R 8
L 8
R 10
U 8
R 4
L 8
D 7
U 4
L 1
R 10
U 10
L 6
R 10
L 6
U 8
R 11
D 9
L 1
R 2
D 10
L 4
U 8
D 9
L 11
R 7
U 7
L 2
D 1
R 8
U 11
D 5
R 4
U 7
L 8
D 7
R 10
D 1
R 5
U 4
D 3
U 4
D 11
L 8
R 10
D 7
U 1
D 11
U 1
D 10
R 5
L 2
R 10
U 9
D 8
L 3
U 6
R 11
L 4
U 4
R 3
L 3
U 2
R 8
U 6
R 7
D 6
U 1
R 3
L 6
D 4
L 2
D 8
U 2
D 3
R 10
D 10
R 1
L 2
R 4
D 10
L 1
U 3
D 1
R 7
D 9
R 1
L 10
R 9
U 11
R 1
L 5
U 7
R 8
L 3
D 5
R 11
D 4
R 2
U 6
D 11
L 5
D 5
L 3
U 7
R 5
L 11
U 11
L 10
R 9
D 2
U 2
R 2
D 11
L 3
U 4
R 3
U 5
D 5
L 5
U 5
D 3
U 5
D 7
R 9
L 1
D 11
U 11
L 5
R 10
L 3
U 12
L 8
U 4
R 12
U 12
D 6
U 1
L 11
R 8
U 8
R 12
U 2
D 12
R 4
L 1
U 12
R 1
L 8
R 5
U 11
L 8
R 2
L 10
R 3
D 11
L 2
U 11
D 7
L 5
R 8
L 5
U 7
R 10
U 3
L 6
U 1
R 9
D 12
R 10
D 3
R 2
D 8
R 2
D 3
U 2
L 12
D 8
L 4
U 8
D 10
U 11
R 11
U 6
L 10
U 3
L 5
U 12
L 9
R 8
L 12
R 3
D 11
U 11
L 9
R 8
L 1
U 2
L 6
R 6
D 5
R 1
D 7
L 3
U 8
R 1
U 12
R 6
L 9
U 6
R 2
D 8
L 11
U 1
R 2
L 3
U 4
L 12
U 1
D 7
U 3
D 10
L 6
D 1
R 2
U 7
L 3
U 2
D 6
R 5
L 11
R 9
D 5
R 8
L 6
D 3
U 7
L 6
D 10
U 4
L 9
R 2
D 8
U 2
L 7
D 13
R 6
L 6
U 3
D 9
L 5
R 11
D 13
U 6
D 8
L 7
U 13
L 3
D 2
U 7
D 12
L 3
R 10
L 8
D 8
U 5
R 4
U 12
R 2
D 11
L 12
D 12
L 11
D 1
R 10
D 10
U 10
D 2
L 2
R 7
L 13
U 5
L 10
U 5
R 5
L 13
D 7
R 9
U 2
D 11
U 4
R 1
L 5
D 7
L 5
D 6
U 7
R 8
U 10
D 12
R 2
U 6
L 12
D 12
L 8
U 1
D 8
U 9
D 11
U 8
D 1
L 9
R 10
U 4
D 4
U 12
L 9
D 13
L 12
R 12
L 11
D 12
U 9
D 1
R 4
U 5
R 8
U 6
R 10
U 1
L 7
D 12
R 13
D 10
L 1
U 9
L 9
R 2
L 14
R 8
U 6
D 7
R 4
L 9
D 3
L 11
R 13
U 6
D 6
L 2
R 6
U 1
L 13
R 9
D 9
L 5
R 9
D 4
U 13
L 9
D 7
U 8
D 1
U 11
L 12
U 4
D 7
R 6
D 13
L 12
R 8
L 6
U 1
R 13
U 9
D 2
U 2
D 1
U 6
R 8
U 2
R 6
D 8
L 10
D 14
U 6
D 8
L 3
R 2
U 4
D 10
U 13
R 1
L 11
D 2
L 6
D 14
U 8
D 11
R 1
L 8
R 12
U 1
D 4
U 10
L 9
D 11
L 10
U 13
D 7
U 4
L 11
U 8
R 12
D 4
L 1
U 7
D 5
U 6
R 7
L 8
U 13
L 1
D 8
U 14
D 5
U 10
D 14
L 6
U 4
L 9
D 6
U 7
L 14
R 13
D 11
R 6
D 10
U 6
R 8
D 14
U 14
L 4
U 2
L 4
R 8
U 14
D 2
L 15
U 4
D 6
R 3
U 3
L 12
U 4
D 8
R 14
U 15
R 3
D 10
R 14
L 15
R 9
D 9
L 10
U 7
L 13
R 4
U 4
D 13
L 14
U 7
L 4
R 5
D 7
R 4
D 15
R 15
U 1
L 2
R 14
L 7
U 13
R 12
L 5
U 8
L 15
U 6
R 11
L 12
U 13
R 4
U 15
D 5
R 14
L 6
U 1
D 5
L 7
U 13
D 8
U 2
D 11
L 6
R 2
L 10
R 6
L 14
D 7
R 6
L 10
R 4
U 1
L 3
R 6
L 8
D 14
R 3
D 15
L 9
D 10
U 11
R 5
D 11
U 4
R 2
D 2
U 6
L 7
D 5
L 12
U 3
R 8
D 13
R 9
D 1
L 3
R 14
L 3
D 13
L 15
U 2
L 2
U 12
D 1
L 9
U 2
D 8
R 12
L 5
R 9
U 15
D 4
R 7
U 9
R 13
U 14
L 1
U 1
R 15
D 1
R 2
U 11
R 8
D 9
R 1
U 13
D 3
L 4
U 6
L 12
U 5
L 2
R 11
L 5
R 4
D 11
L 9
U 15
L 12
U 16
L 12
D 6
L 3
D 12
U 2
L 4
R 15
U 16
D 13
L 14
U 13
D 11
R 14
L 13
U 9
L 9
D 15
R 1
D 4
L 8
R 1
D 12
U 1
L 13
D 8
U 7
D 7
L 12
D 11
L 7
U 5
R 14
L 6
R 8
L 15
U 12
R 13
U 7
L 1
D 12
U 16
L 8
U 1
L 1
U 6
D 14
U 2
R 9
L 15
R 4
D 5
U 10
R 7
L 15
R 5
D 1
L 1
D 4
L 1
R 4
D 10
U 13
L 1
R 13
U 16
R 15
D 5
U 6
D 1
R 5
D 4
U 6
R 8
L 1
D 3
U 13
D 14
U 11
D 7
U 12
L 1
D 3
U 1
R 2
U 9
R 2
D 5
L 8
U 4
D 1
L 9
R 5
D 12
R 12
L 12
R 16
L 10
R 15
U 7
D 13
R 14
D 12
R 2
L 7
U 5
L 15
D 5
R 12
U 14
D 2
U 11
R 8
U 2
L 5
D 10
U 7
L 3
U 15
R 2
U 11
L 10
D 4
U 6
D 15
L 9
D 8
U 11
L 10
R 17
D 2
U 1
R 7
U 9
L 4
R 5
L 11
U 11
R 13
L 7
D 17
U 10
D 5
U 17
L 1
U 3
D 4
U 16
D 17
U 10
D 12
U 1
R 4
D 2
U 1
D 1
L 9
D 6
L 1
U 8
L 2
D 1
U 10
L 14
U 17
D 12
U 1
R 1
D 8
L 7
D 10
L 15
R 15
D 14
R 12
D 5
L 1
R 14
L 2
D 8
R 15
U 6
L 4
R 5
D 11
L 16
R 11
D 14
L 14
R 16
U 12
R 2
U 16
L 3
R 4
U 15
R 15
D 3
U 17
R 5
L 2
R 15
D 13
L 2
U 4
L 6
R 5
L 5
R 4
L 9
U 3
L 9
R 15
L 4
R 1
U 3
L 1
D 3
R 9
D 9
L 10
R 14
L 18
U 7
R 11
L 6
R 16
U 9
R 5
U 5
R 9
D 9
L 12
D 18
L 11
D 18
L 2
D 8
R 6
L 1
U 11
L 6
U 18
L 8
D 12
L 8
R 15
L 15
R 13
L 10
D 15
R 10
L 11
R 14
D 6
L 9
U 3
R 10
U 18
R 9
L 9
D 4
L 17
D 16
U 10
R 14
L 15
R 5
U 2
L 4
R 15
U 2
D 2
R 9
U 14
D 17
U 5
R 1
U 15
R 17
D 4
R 7
L 4
R 16
L 11
U 10
R 3
D 2
L 5
R 14
L 4
D 11
L 11
U 6
R 9
U 3
R 17
D 16
R 18
L 10
R 15
L 14
R 16
L 12
U 3
R 9
D 17
R 6
L 1
R 16
L 8
U 16
R 6
L 1
U 4
L 17
R 4
U 15
R 19
D 7
R 18
L 16
R 18
U 2
D 11
L 17
R 2
L 10
U 17
D 11
R 17
U 1
D 15
U 6
D 19
R 16
D 12
L 7
R 13
D 14
L 12
U 14
L 5
R 5
D 3
L 10
U 16
R 14
D 16
L 9
D 16
L 10
R 11
D 11
U 19
L 4
D 16
R 8
D 1
U 4
L 15
R 5
D 1
L 19
D 19
R 12
L 18
D 13
L 4
U 6
R 5
D 12
R 15
D 9
L 9
U 16
D 1
R 16
L 7
R 6
D 12
L 7
R 8
U 17
L 12
D 9
L 8
D 16
R 8
D 9
L 17
R 3
U 6
D 1
R 7
L 4
D 10
U 7
R 13
L 10
D 19
U 7
D 10
L 17
R 18
D 15
R 6
L 7
R 8
U 16
R 6
D 3
L 19
D 10
R 12
U 13
L 11"""


T08 = """30373
25512
65332
33549
35390"""

I08 = """101232232424431123432342554040352101405502025646520640026102435415402415524241404341001022013221221
322003200404313034023203145443134010555246652210042156042654635314322525041550121322403330300102030
300223331202022110511510154103110142442012332003514242206354525511353252421542430110200442102312123
323133401312301310040251134225352136126616004434252462045055305202261355433025233042244241414400023
101104403040123044220034201231621525016350121330311611014454116414515052210415423202213344444213032
023343200312321341111312312116004553510400124564003503525336352206534312634553034341344231103320121
232432314323445335412313341660535056605316245521312422204421411026063010063200110052210224330113302
312104103023300150511003256056530232416620641476331566726505005253550226461151520445555123411440334
212320403040021521143113451320122514052261721742217616232666314261562006620634125252332350322233244
121203010304521210411013440333264052674653423316314375512175574325262425522003540134541121330431412
242204210504314451204236552066106466756545677241223651236433541213145114512054256134345025222414332
142041442305525524414554456630445566671622363554565311414164346521375126616036343225552430320142242
444343225200452531125463161044526512711315644346716774456167633775552325212323502414500125304101442
310331200433511524004324523024376145644272331714275745132552527332621757111641110604243400150102301
324000410032344243443213031215347666416142612722352331527416524446272144632054626460610411343015214
320123043045014453006030311336322753322266368648765847556774576424774346643352662320364111534525122
442020510341512162315013222156456642565478638555682735664832583554422245165431250246236222000222413
414115045035446663521337425454354252666867442648382483378248585426324451353146435112651062444320153
404031553354665600421273415333424442557623485578324525478673862565714171753646445146504611043544310
420221121313524320031226342733736342778854854745272737436344833444332262273475742543435414301514022
102433434104221136261652367123828833742266365587682657232782236687733375147446456435013164623033453
254052000640223505333752451714435245653688563475537427586864344637533256524566641541066561013340115
402424554664414061612366662262546262344862767983768964383722283664424826344415366464635564003035522
453430306616221255375164464844337767643264664566433699446375333477788728421713267327336401105425333
424340460333633611416743647223584543446663447884569869575943675246265858843135752722203060601314510
100104404661641521713564623486853464898563575445444677875368568656336855687665453132126163413415413
215302243412504531566112426534574499379653449589737746345943794657936355232887343422456306315453552
510025400262416244231532674726546437535536634838644683689356756484986473434524723553734023111254223
200204056365027317421364428852638397454355393937474567465453855598477485557424664756156234516125002
315311346005136326466555385687277868747539849498675894853944993694973352587363421743725352145116525
003432325612552157642734768322776884596464869575664456575756766387847762385773543511142455502615010
323005315540227472658648485349375446787359896487975999967994878588768333826274268465567534243515604
440456221306764751672857476368954437466478794954588479785445855488353476362467345856473677540155641
145626220661445722124873768476448493998999449996678498948886598577843394688625385873326644342243461
445562611272117173322737877366885654845578785685455598488999678884466965543672555556173431656206420
025130063437366574263434683849438959768954744996857595658945978854575385745862424366457372746221315
330056343042353748468655383756666954488668996955869957549949945974898849943638748754612625120241011
432440053115343158276372498785736949588874688959799775598548957878884775394762348284137737673641642
102056040435747284853655648443579469664944568788855866779976889755858957959735324265746533251062403
225266001744262443233334974839654865799445785659659675575666575758865948754463425885535443736632404
110654201772435145572468544985578676579996656795879868576797847675977856844578738333816426565246622
433122252566473253723864943786447484655995769756667897965855958658757798373853334626865115523210441
556541053615336747283763545495655688878588665885858779779899597977449644485399674475255622322020110
011246513266431242864686953687878987686577868895997988788689566679898456889984483487464125476243224
146430654214211787457337933537555866765688875799887976988578679556659655564463526386463716114354031
301355426474121386642848739759597465855588776978689979798756956985699554573779455545642175346410200
665401551644225425227738385396554475758768868798997798968696775989794666575779876332737347375414225
512264373337161748463436934959669586879679979679896989676576695988989664437878448276827532543745623
414644336467578472474486349936485857567669856689768668976766988984549484863488738455255412422624432
036441527146156483775836379836679964765795668878769977878799767597698768864788657252857655434752204
444666167464342238764266465439498755555659877886888899999856978994556568955445528325646125672164600
554433027362778886523875976836986988896695897689678886787996679658974797569374338344624672757631301
310042272613272624885896949859765467876555996976999696789988967965466684754895746762223775172234330
216343113411562425626633578339674859855875577977769879987785777674498658748899947272432652777416624
644655617213144523726243646388856494887979798868676998696768878865895676484383655444254627274131426
563636621655445248723867836434648597896597866798698876698598597697577776937367826877324161661354535
341056514244726338453499673897657855866875759776669996869785685895756748635866544776371413425025432
044435013274135828365337573975868886748866596788969877955955756895957574564469583387354142524005261
410342122777647883362439734978585444678669878589755875966798767797995783366779884352756543534151243
441043541147123324228379874699597946948555885687569696976589658895855548467778233287211424145465240
013520313145473358567557484588597487658658866969675558679557775795544577887779883542724441435601554
413424243572773133387782457533847759697988966666777979879595749686579798343746884752342364430012243
326240460425117754473464599468874499568546888968889968769655795459984446735672755758632161131203442
300131303151234667345248566663377796947878745698979798686969577865488637644574724367556777536526223
201413522556166618225635288589984557686665556767657595967679955648876746974783378576524471465423550
132203011242354537628633669369699337985447975976769776866447886769358896665782776877447544703406253
133532343456535111383888625455386597867455655599757897755558666966586346883426636652263242705454404
515656631143165354267432455336475494569987585578555494867798784856975634394283638544164731533012364
140416432445724172247278853455798367884868796498777454967657748875548789832362674732676672056032431
330330152414564665274243438433876363573585996985888846846845663567545668252624564762246173301325502
302226105363143741352735557782868788733464859494486947884994938599357344542482523627145432560642353
145422126105171466242567724557544489934658889494656859885599738537534845443644581256761746362221023
441212145032074213275667582428345868377677696997785565377585765567746584667226657214272426340532331
101452412564254231314347763234647978536934546886949376683847693599962882662556735366332605253254243
242134245465654443763242368746262775635568895968649374696544643593776484646237623121155311612120205
224324556334241543152423764688727563658665947774377475559746775387478253676754241443542553641515133
112040215053533166723764146688552662254436968389648683363668663468622524888354726754315425216123100
021125312165155354236637163434868472666833569875463833389786585853644277477624254454065142204421252
524302450104653624156271174347323843256576684986975339949343684428633575452572646373611442213410412
013000504615163043526333634318868574767387865682722275245644673556658444321441613432604542203511551
242524501014131565575336754147245826628343573377352338767422674636538742125631345462033033403235255
304401342145144243415545241676576556264543764465565724532645542743372525221461725562353265045051132
234302031320344616366225577677124763333456446683735866667852458578422752674576640145530645050512154
132421020111321255530526663734272513535262623562488642564636574385245112665623132642441334102314011
102255335052511135645343464117315257162723258847453624673355647345665737125672220566436213014134441
312245204230352351210405226233122343511172545755556267356584643164226213732752212035632152433154320
433104142453501532612362446717232767156326652752737733565427127523161253271344216136060252512442041
212230512443134051666444123274474475364671426411226276576372452514665156262633036430153240020401401
300411330411451231141436052664142373444325735263226333375416444576253146002526306114152241250403310
101032115301513352525160453141002773563414647477456721366627231126771542123126102455031250033223313
324233212142235532140166110023400026333355425117234444773232146225326253461050325545343105500423104
033431121034120033510616215166546146337352752676632624643526424216650102540533503153134132000420142
240121103430140123513513462300432156652122676414274512336151334241532064154406340323144200421003324
233142431112012541421523134462664026316416350553765272706623513350020256351263445534113304131112033
323203003131024144404243206121423310355043066662201116504344265455134633403341445324024304010343200
133044014403300041520020101412541120000145660632333004501603416535515112534533414430000213113231220
020200134443230224532201430335140300110631641143466045463552301460233403451514045510012313003444012
003320111443312431412215134024143654125511235514301244523512535041410415313130552501342112344000332
223322121002242440120225413345342544646200604640400343653451404544533034511344250023302010222012033"""


T07 = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

I07 = """$ cd /
$ ls
dir plws
dir pwlbgbz
dir pwtpltr
dir szn
$ cd plws
$ ls
dir ffpzc
dir frcmjzts
92461 nbvnzg
dir phqcg
21621 vqgsglwq
$ cd ffpzc
$ ls
48459 dzdfc.vqq
143107 jql.jzl
208330 mmnvqn.hqb
290122 svjvhflz
218008 wjlmgq
$ cd ..
$ cd frcmjzts
$ ls
dir bsltmjz
dir jfzgrbm
$ cd bsltmjz
$ ls
34237 dzdfc.vqq
58741 mdgdhqgw
$ cd ..
$ cd jfzgrbm
$ ls
132811 fcmpng
103661 lgt.swt
173031 vqgsglwq
29134 wprjfg.zbr
$ cd ..
$ cd ..
$ cd phqcg
$ ls
955 jgfs.zjw
$ cd ..
$ cd ..
$ cd pwlbgbz
$ ls
dir gbg
dir mjzhcwrd
dir njcscpj
dir sphbzn
dir tbgjpphc
55938 tvrfpczc.djm
4840 twd
$ cd gbg
$ ls
287003 fcsjl.bzm
dir wgq
$ cd wgq
$ ls
22963 fcsjl.fcm
$ cd ..
$ cd ..
$ cd mjzhcwrd
$ ls
228632 clfnpmbq.zmb
28276 dzdfc.vqq
2982 tdbg.wgn
$ cd ..
$ cd njcscpj
$ ls
dir dqzgqgv
275186 ffpzc
192491 gjnflc.plq
$ cd dqzgqgv
$ ls
70309 dzdfc.vqq
56139 fcsjl
142095 sgwz.cdz
dir snjntth
dir sphbzn
284618 wjlmgq
$ cd snjntth
$ ls
51918 ffpzc
dir vrfgfds
$ cd vrfgfds
$ ls
155233 jlscz
$ cd ..
$ cd ..
$ cd sphbzn
$ ls
dir qbzwrrw
dir qwpzn
$ cd qbzwrrw
$ ls
278531 fcsjl.tqj
211591 snjntth.gpd
$ cd ..
$ cd qwpzn
$ ls
174183 vqgsglwq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd sphbzn
$ ls
185471 bsltmjz.fqz
dir bsvh
dir fvzcs
dir ndw
dir nlml
dir pcbt
286260 zhcmrpvt
$ cd bsvh
$ ls
130814 wjlmgq
$ cd ..
$ cd fvzcs
$ ls
dir cgmv
dir ggzwljr
298241 qvzghdpw.lms
dir snjntth
dir sphbzn
$ cd cgmv
$ ls
46843 dzdfc.vqq
dir lmqcbbm
dir rstcqsmd
215261 snjntth
$ cd lmqcbbm
$ ls
229898 bdmbvgp
25529 ffpzc.stm
16871 lnpjzvg.qlj
$ cd ..
$ cd rstcqsmd
$ ls
289038 zrbbbwng.smf
$ cd ..
$ cd ..
$ cd ggzwljr
$ ls
198200 bcthn
$ cd ..
$ cd snjntth
$ ls
191672 fwp.phf
68229 hzs.zpg
dir pggcwb
222426 qbv.bwj
dir snjntth
155354 vmqcm
$ cd pggcwb
$ ls
154272 fqztwvnv.lvv
dir pdjg
62393 vqgsglwq
dir wjhrtg
$ cd pdjg
$ ls
260644 gvhlrcf
209906 wpls.pbd
$ cd ..
$ cd wjhrtg
$ ls
148640 dljf.zrq
172168 dzdfc.vqq
196203 hjdphcfm
247620 sgwz.cdz
$ cd ..
$ cd ..
$ cd snjntth
$ ls
37467 ndlshlmj.cjq
257404 snjntth.nsf
$ cd ..
$ cd ..
$ cd sphbzn
$ ls
64082 bfdv.lwv
dir bsltmjz
58942 dzdfc.vqq
dir snjntth
$ cd bsltmjz
$ ls
dir bsqqdr
266007 fcsjl.gfm
dir ffpzc
dir frsmrd
72122 nthnhzwf
286705 wjlmgq
$ cd bsqqdr
$ ls
117496 wcqt
$ cd ..
$ cd ffpzc
$ ls
280224 mmnvqn.hqb
105346 vrr
$ cd ..
$ cd frsmrd
$ ls
111509 sphbzn.shz
$ cd ..
$ cd ..
$ cd snjntth
$ ls
177491 mplj
9029 pvbz.jwn
92891 snjntth.zrv
203356 vnnnw.gql
134728 vqgsglwq
$ cd ..
$ cd ..
$ cd ..
$ cd ndw
$ ls
241303 bht.rpj
173068 vqgsglwq
$ cd ..
$ cd nlml
$ ls
228982 hzglfpvq.ftt
114981 sgwz.cdz
$ cd ..
$ cd pcbt
$ ls
dir bsltmjz
dir ffpzc
dir fjsjwfg
dir fwm
dir jvwt
227943 tmr.jdc
dir vwpqzdwh
31258 wjlmgq
$ cd bsltmjz
$ ls
177750 bsltmjz.spj
dir ffpzc
dir flrpwfs
138824 mtmdtcpv.cfj
165770 wzqwczj.qwn
$ cd ffpzc
$ ls
179645 snjntth.dss
$ cd ..
$ cd flrpwfs
$ ls
60566 wvjq.gmm
$ cd ..
$ cd ..
$ cd ffpzc
$ ls
97847 qzhhtmd.bhw
1197 vqgsglwq
$ cd ..
$ cd fjsjwfg
$ ls
152232 dnsdd.jgz
181301 gsb.wsh
dir jqpb
dir jscbg
dir snjntth
227677 snjntth.vvg
dir sphbzn
75358 vqgsglwq
2589 wjlmgq
$ cd jqpb
$ ls
253403 mmnvqn.hqb
108325 rvq.mrc
$ cd ..
$ cd jscbg
$ ls
dir dtm
dir gsdnz
208269 prh
25977 qdzljgh
169262 vmnq.mth
$ cd dtm
$ ls
80072 gzqnb
$ cd ..
$ cd gsdnz
$ ls
dir dsqzjs
297895 sgwz.cdz
129983 vqgsglwq
$ cd dsqzjs
$ ls
2621 jqrlsf.gzs
164844 snjntth
$ cd ..
$ cd ..
$ cd ..
$ cd snjntth
$ ls
118553 cbhql
dir ffpzc
dir snjntth
$ cd ffpzc
$ ls
dir lmn
12104 tvlwn.vhh
$ cd lmn
$ ls
46401 bsltmjz
96888 shrnqhvq
$ cd ..
$ cd ..
$ cd snjntth
$ ls
dir snjntth
dir vlnfhbq
dir wpwl
$ cd snjntth
$ ls
dir ctj
$ cd ctj
$ ls
82485 fcsjl.lfl
$ cd ..
$ cd ..
$ cd vlnfhbq
$ ls
250106 qvf
$ cd ..
$ cd wpwl
$ ls
153950 cmsd.rlg
$ cd ..
$ cd ..
$ cd ..
$ cd sphbzn
$ ls
dir glgq
$ cd glgq
$ ls
285182 wjlmgq
$ cd ..
$ cd ..
$ cd ..
$ cd fwm
$ ls
251865 ffpzc.qgb
279522 zvvpfqtp
$ cd ..
$ cd jvwt
$ ls
48990 bsltmjz.nzp
219604 ffpzc
69573 mvmdfzr.lwb
$ cd ..
$ cd vwpqzdwh
$ ls
267581 pvcch
$ cd ..
$ cd ..
$ cd ..
$ cd tbgjpphc
$ ls
255571 dstpcgr.tfq
dir fdbwbrpp
dir gjzwh
dir hjvrtjt
dir rhzczj
292888 sgwz.cdz
dir wlzhr
149395 wnfzrqgz.dtn
$ cd fdbwbrpp
$ ls
dir ffpzc
dir qbrth
51164 qprp
dir slpt
117026 sphbzn
295685 vqgsglwq
dir znmj
$ cd ffpzc
$ ls
dir jhnzrdvb
$ cd jhnzrdvb
$ ls
217775 ffpzc.sgw
$ cd ..
$ cd ..
$ cd qbrth
$ ls
183969 lpbwgfjv.vcg
47333 wjlmgq
$ cd ..
$ cd slpt
$ ls
32343 tqhtj.jwz
$ cd ..
$ cd znmj
$ ls
55058 mmnvqn.hqb
$ cd ..
$ cd ..
$ cd gjzwh
$ ls
dir dvcbcd
202530 dzdfc.vqq
dir fsgz
dir hfrrqq
54897 jlzn.qsn
16097 ldzqsbb.jzl
225078 pswccrd
dir rqqmldw
292464 rzrdhbp.vld
dir ssqbqqp
dir zsztqrc
$ cd dvcbcd
$ ls
187837 dzdfc.vqq
dir jlwtvf
dir jnjvshs
164053 nrf.fqd
5665 tlp.jmt
13801 wjlmgq
$ cd jlwtvf
$ ls
219985 sphbzn.dvj
$ cd ..
$ cd jnjvshs
$ ls
dir bsltmjz
dir nrpm
$ cd bsltmjz
$ ls
152972 qgdqj
$ cd ..
$ cd nrpm
$ ls
18509 wjlmgq
$ cd ..
$ cd ..
$ cd ..
$ cd fsgz
$ ls
224576 mmnvqn.hqb
$ cd ..
$ cd hfrrqq
$ ls
dir bwgsnfvb
dir fcsjl
294608 ffpzc.gvm
136880 qjcgtw
dir sphbzn
$ cd bwgsnfvb
$ ls
29735 dzdfc.vqq
dir wstmzfml
$ cd wstmzfml
$ ls
158447 bnvhbvvc.nrt
59889 jclclgd
$ cd ..
$ cd ..
$ cd fcsjl
$ ls
138297 ffpzc.szw
$ cd ..
$ cd sphbzn
$ ls
dir wqdths
$ cd wqdths
$ ls
8326 cgvtw.jpz
$ cd ..
$ cd ..
$ cd ..
$ cd rqqmldw
$ ls
226757 dzdfc.vqq
115055 mwb.btc
dir qpts
298524 sgwz.cdz
$ cd qpts
$ ls
60860 bsltmjz.frp
dir fcsjl
94904 sgwz.cdz
dir wnmqqspz
$ cd fcsjl
$ ls
25082 mmnvqn.hqb
$ cd ..
$ cd wnmqqspz
$ ls
165529 sgwz.cdz
$ cd ..
$ cd ..
$ cd ..
$ cd ssqbqqp
$ ls
192477 pvrgm
$ cd ..
$ cd zsztqrc
$ ls
254053 lht.htn
$ cd ..
$ cd ..
$ cd hjvrtjt
$ ls
189942 fwps
$ cd ..
$ cd rhzczj
$ ls
36502 bmtfr
dir ffjz
35148 nctfhmzm.vsz
dir qdgjzcz
208196 rwql
79863 sgwz.cdz
dir snjntth
$ cd ffjz
$ ls
dir grsvhwm
$ cd grsvhwm
$ ls
50231 fwj.rdv
dir snjntth
$ cd snjntth
$ ls
dir dtbgb
$ cd dtbgb
$ ls
150245 vdflm.lmq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd qdgjzcz
$ ls
222389 dzdfc.vqq
$ cd ..
$ cd snjntth
$ ls
56794 mmnvqn.hqb
$ cd ..
$ cd ..
$ cd wlzhr
$ ls
116628 bsltmjz
60122 jqpbsgnr.fgb
252605 lfss
300065 qwjdl.vhr
$ cd ..
$ cd ..
$ cd ..
$ cd pwtpltr
$ ls
dir dplsvrhl
140951 gwtfzqvd.znb
dir jbvdb
dir jst
dir qhjv
dir snjntth
$ cd dplsvrhl
$ ls
272101 fcsjl
dir ffpzc
58852 mmnvqn.hqb
dir mnhntjz
91899 sgwz.cdz
228077 snjntth.btv
$ cd ffpzc
$ ls
5499 bsltmjz
dir qmfwpjhl
dir rsrb
dir wgt
$ cd qmfwpjhl
$ ls
300362 dzdfc.vqq
$ cd ..
$ cd rsrb
$ ls
252983 dzdfc.vqq
107744 ltssrgqb.zvj
214895 rhglgcwr.wpw
249727 sgwz.cdz
$ cd ..
$ cd wgt
$ ls
141984 dzdfc.vqq
194686 mmnvqn.hqb
258023 pgr
$ cd ..
$ cd ..
$ cd mnhntjz
$ ls
dir bdvght
dir jprwchh
dir snjntth
$ cd bdvght
$ ls
243166 vpsvjdq.wsn
$ cd ..
$ cd jprwchh
$ ls
178943 bmpc.bjb
$ cd ..
$ cd snjntth
$ ls
dir nlbm
dir zjmjntff
$ cd nlbm
$ ls
33050 fcsjl.rcc
dir sphbzn
17446 wjlmgq
$ cd sphbzn
$ ls
214563 prrfhff.pbp
$ cd ..
$ cd ..
$ cd zjmjntff
$ ls
82134 sgwz.cdz
52203 vrtlgdq.crp
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd jbvdb
$ ls
dir wmtjh
$ cd wmtjh
$ ls
dir ggvwn
$ cd ggvwn
$ ls
192285 spqvmf.sdh
$ cd ..
$ cd ..
$ cd ..
$ cd jst
$ ls
dir bsltmjz
212740 dzdfc.vqq
dir gncztvtb
dir jsqjcqnt
286257 jvs
36654 sdcsm.mbg
192040 sgwz.cdz
dir tbqphzb
dir vdcqgts
285843 wjlmgq
$ cd bsltmjz
$ ls
215705 snjntth.gpv
213665 wjlmgq
$ cd ..
$ cd gncztvtb
$ ls
229298 vqgsglwq
$ cd ..
$ cd jsqjcqnt
$ ls
dir bsltmjz
dir fcsjl
dir ffpzc
dir sphbzn
70864 vqgsglwq
$ cd bsltmjz
$ ls
14981 pqzffzjc
$ cd ..
$ cd fcsjl
$ ls
140328 jwhczwbc
$ cd ..
$ cd ffpzc
$ ls
213650 mmnvqn.hqb
$ cd ..
$ cd sphbzn
$ ls
dir psmtphhq
dir sphbzn
$ cd psmtphhq
$ ls
dir ffpzc
123131 tzgwd
$ cd ffpzc
$ ls
49737 cfngvmd
dir gcnrp
172799 gmd.cwl
dir llnztjf
dir nbqs
79661 rrqz
$ cd gcnrp
$ ls
283 vqnrgl.vwp
$ cd ..
$ cd llnztjf
$ ls
63263 tjhm.bwh
$ cd ..
$ cd nbqs
$ ls
dir vssmq
$ cd vssmq
$ ls
88980 dzdfc.vqq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd sphbzn
$ ls
20140 fcsjl.zrs
260579 snjntth
$ cd ..
$ cd ..
$ cd ..
$ cd tbqphzb
$ ls
93470 sgwz.cdz
$ cd ..
$ cd vdcqgts
$ ls
223564 dzdfc.vqq
dir ffpzc
dir gwhfgwf
dir nbjtqnng
dir snjntth
$ cd ffpzc
$ ls
42813 qwwmw.nmt
$ cd ..
$ cd gwhfgwf
$ ls
59918 jvfv.mpm
dir mjl
211039 pcwl
$ cd mjl
$ ls
13004 pgjb.tpq
195995 tms.fjz
$ cd ..
$ cd ..
$ cd nbjtqnng
$ ls
107058 dzdfc.vqq
dir ldrsd
111631 vqgsglwq
104599 wbzmdljw.tjq
155747 wjlmgq
$ cd ldrsd
$ ls
107439 jvjm
$ cd ..
$ cd ..
$ cd snjntth
$ ls
242680 fgrt.gng
$ cd ..
$ cd ..
$ cd ..
$ cd qhjv
$ ls
dir bmnm
68453 hjjpdgn.hwl
dir sjlbj
dir vqnrj
$ cd bmnm
$ ls
1238 vqgsglwq
$ cd ..
$ cd sjlbj
$ ls
44239 wzzbtmrz.gml
$ cd ..
$ cd vqnrj
$ ls
3286 bsltmjz.qlc
$ cd ..
$ cd ..
$ cd snjntth
$ ls
130833 blm.wmt
dir snjntth
dir tcnmbcgg
218869 wjlmgq
$ cd snjntth
$ ls
dir snmrdfbt
$ cd snmrdfbt
$ ls
281025 bzrsds.lfg
$ cd ..
$ cd ..
$ cd tcnmbcgg
$ ls
194998 fcsjl
dir qdrmpqgn
dir rzqd
dir tcsds
$ cd qdrmpqgn
$ ls
165713 qmzgt.tnc
$ cd ..
$ cd rzqd
$ ls
dir cwhnmlv
57819 fcsjl
246864 pjnzdvd.gjm
$ cd cwhnmlv
$ ls
287539 mmnvqn.hqb
215636 pbnjt.zbn
124638 sqd
$ cd ..
$ cd ..
$ cd tcsds
$ ls
78812 gfmgb.wqj
218987 hnhfvz.dln
209640 mzzhqlq.zqp
102492 nml.ppg
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd szn
$ ls
dir fcsjl
dir snjntth
dir zjbp
$ cd fcsjl
$ ls
158019 jsv.pmz
$ cd ..
$ cd snjntth
$ ls
229510 dfvpvp
191061 fgplbptq.jlt
dir lfb
234911 lfsrwr.wcb
dir lrfcgzl
48031 stbbw
219691 vqgsglwq
dir zshh
$ cd lfb
$ ls
dir btj
99591 dhrjbvvg.gwm
137224 dzdfc.vqq
201972 jtzmqsvj.wnd
9704 mmnvqn.hqb
dir pwg
200308 snjntth.css
dir wcmhcfm
dir zwhvmln
$ cd btj
$ ls
dir rnbzdfgn
51799 wdhsm
dir wvf
$ cd rnbzdfgn
$ ls
117095 bsltmjz.tlv
$ cd ..
$ cd wvf
$ ls
dir ffpzc
dir ncbmgpsc
dir wtwrmjnt
$ cd ffpzc
$ ls
249919 lsth.fmf
$ cd ..
$ cd ncbmgpsc
$ ls
147899 dzdfc.vqq
$ cd ..
$ cd wtwrmjnt
$ ls
252366 pvpdv.jwz
$ cd ..
$ cd ..
$ cd ..
$ cd pwg
$ ls
280845 fcsjl.fjz
44300 sgwz.cdz
dir snjntth
229605 vqgsglwq
$ cd snjntth
$ ls
2053 pflvsnzs
143522 sgwz.cdz
$ cd ..
$ cd ..
$ cd wcmhcfm
$ ls
229329 qsznhwlw.vjg
$ cd ..
$ cd zwhvmln
$ ls
dir ffpzc
dir tjjzbf
dir wzcq
$ cd ffpzc
$ ls
dir ncnj
37497 vqgsglwq
$ cd ncnj
$ ls
40920 htbjhjq
$ cd ..
$ cd ..
$ cd tjjzbf
$ ls
47522 mczn.spd
$ cd ..
$ cd wzcq
$ ls
56662 ffpzc.vwp
dir snjntth
$ cd snjntth
$ ls
117276 wjlmgq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd lrfcgzl
$ ls
267485 rsjmpph.qqz
$ cd ..
$ cd zshh
$ ls
dir ffpzc
dir gmn
dir snjntth
150048 tgtlh
32020 thfr
72152 vqgsglwq
$ cd ffpzc
$ ls
dir snjntth
$ cd snjntth
$ ls
224945 dpfpz
$ cd ..
$ cd ..
$ cd gmn
$ ls
238996 sgwz.cdz
$ cd ..
$ cd snjntth
$ ls
86775 dzdfc.vqq
19560 vshcmjj
$ cd ..
$ cd ..
$ cd ..
$ cd zjbp
$ ls
dir fcsjl
41522 nlvpb.fpf
dir nmtjtd
$ cd fcsjl
$ ls
276802 fcsjl.psm
197934 sgwz.cdz
$ cd ..
$ cd nmtjtd
$ ls
47477 dvqmqlgw.ths
51081 vqgsglwq"""


T06 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

I06 = """zcncrcnrrlccmhchssgqsqrsstfffnqfnfsswgwjjcmcnnvjvwjvwvfvnvwwhvvwmwhmwwwhbhhldhdmhhdfdbdfbdblllnfllgslllqhlhfhlhqllncnfnsffwmwzzlglzlwlhwwmvmddpvvbrvrdvrdvdhhzdhdpdzzbgbsssrpsrshrshhbqbgbmmtwwcbcrbbvnvhnncscwcwlcwlwnwswbbnwntthzzdlzdzffvqvdqvvtptdptphpddzzvhzvzwwqgqjjjvsspvspsbsffvpvcvjcvjvrvjjgmjjhrrdhhdvhvttjttzptpssnlnjjlnnhmnndjnjwwtjjtbbfflwfwgwvvpjpwpcwcgglmgmdmnmbbqtqctcwcmwwvmvlmvmdvdvhvlhlzhzttghttnvnjntnqqtmtwwhvhrhfhchqchhdrdllnwnfwfjjmsmmnhhshnhpptstjjpnpzzhmmpssgrsrzsrrffzjjhvjhjcjcpcvpccfnfjnfjfllssrdsdnnmffldldppcctcmtctffprpsrrrfhfmflldccnpppvsswppdgpgjpgpqgpqpjppclcjczcnzzzqvzzwlzzqfzffsqqphqhvqqbcccstsdttwcwcvvmjjhqqmllpglgtgwgnnbnrbnnjdndhhbrbvrvwwwblwwwppmdmttztqzqrqjjpggpmgpmpqqmssvnsvnndnvddtztddrrsnsbbshhqmhqmmdnnrsrllqvvfjfpfqpqfqflqlmqmrrqgrqrrhvvfddfhhfnhnlncnzzwwjwswpsscpchcssrzssjqsqrsswbbzggnqnwqqsrqqzbqbddtffcjjdggwlwnwtnnpddcqddsppcwpcwpphvphhhrprqrqttwgwqwppvdpvvrgggmpmddzvvwwthwtttbqtbbftfrffbdfbbspshphpwhppnhnmhhbbshbsbmbdmmtrmrbrprbprphhnmhmvhmhhqqbvqvqcvcwcbwcchbbgwwqffrcffsvvcczrztrzzdhdmhdmmzbbvlvqqtptpvvfsfppdzppmddfvdfdwdfdmdwwlvvqdvqdqmdqqmnmdndsswsfwfvwfwzzhrzhhwfhhpvhppmssnhsnsnwswvwlwdwzwnwswwmqmjmbbdjdbbtllcpllltqlttnvvppznpnttlrrwlwvllphpbblccgjcggbtbwtwdwrrbnndpddbqqnpnrnnqqshspsggtptztpzzclcggtqtgqttcmmbgbfbdfdfsddlrlvrlvvmqqgbqgbqbcbbnpplqqblqbqmbbbdqbbhjjcgcdgdwdjwjqqlsqqnnwffglfglgnlggjgjtgjtgjtgjjclcwcqqvpvwwvgvhgvhvjjzpzbznnvrrrpbpdbdhhmshsnnnwppcbcvvlldccdggqnqgnqqzbzzcfflnnmppcgcmgmrgmrgmgngwwptpzzpfzpfzpzdppgcgtcgtgccvtctzzdmzmlmzlzwllbplblltgtctrrghgvhgvvfvssngsschshrhvrvddghgwwwwzgwgvgccjdjzjwwvdvvqsqshsvvddmddbllvppmlpmlmwlwppjmppwrrdzrrpmrmrdmrmbmzzwttvwwsfswwlflnlrlvvdllzbztbtpbtppnjpnpdnnjrjsshtssvvsjvjfjwffsszvsvjssqzsslpslppjpspqptbncvzrlwtjvsrwtnzzhwdfsmlthvgqgjrpshpbsrrvnsdbqslbcplnpcjqwmwqsnwdcjsdmccbdglwbrcdcqsfhjqhstvhqqdwltqwhhqcrnpvnzjhhbjvqbqhclwggjqfvnfsvcnjjhbmrvbpjqrbljbtltvnsgdfhddlmsdhcrfwvlvbsdrjwjvtnqzhrlqgjmzsmjlpdjsrjmdhmvgwjmfwtqffnzfrtswrlgvvhhqgpzcjwscfqgjmdhtvbgzdlvzfhgqlqbfwsjrmmhrlcwhrcnwwvngcmsrfgczsfqvvmdtmtprfvjrwrwcqwvgmzcjncrzvcswlzsdszvdtwmptnrhgzqwrhjjtbchhpwsdjnqmnsgzwqzvlzlsznpqgvtqnldjqpvndtsjlzhpzsgthbwvwnlbwjlmndqpcdvjdgdzhctpghlfwrtqtvfwdpgrjbmwzqgthjpmlrsqmzsznddhrbjnggqrdntpbngvldnnltfnmdwfhftjvpqbrzqvdzbzzctshzldtcdgfnczglrrjtwswzdvjrfgwztwznbpplmbgwpcmstcsjtqhmzmzsjwsfbjlbnbdtdsmlpdmrrbhdhpzrjdpzhcwsrgfrhmqzqtjfhpvltnthwjrrrpnsbmmwrhsfqbmnvwhpntltsgwgnqhcvlndfrtrfrnlmbhltmtgzhlzqgtsbbnggdjvbslfbczhpghqqcqlrbtpnbqbflfjrmpmwwvjqgvcqtmfggmptqlqstcmdtqlslnnzwbgnstftfsvsjdrmgbzfnzltwbjmqhsvshnmwhftjdndltdpngzwbrjpgpwmqgfsflnhmtzcmdjmzwrsrrrmpvwgggwrhrwtfwdbgbpmwpcdspdtbqvdwwsnwdtrtdtgnfzzsmlbcqdzbsqnrgtvvnlfcdlcgcnfpqbddqcjfqtmpndmnwvfqgjzrltqvlprmbbhmtwbzjjgfhhhfjswpffmjnsdmrcjrwlwpmfrmhljpphlwwwwmgsjcsrcvmfrdjdhshddshpplzsnsphcmdhvllgmdgrvbvjmtpltdthffsvwwhvgqrhmfjfpdswcqldrhpmznffjsntwrnmnpmsshljszbchctptsdlnbcvpfvtlfnzcrljpdwrsjnlpqcpnwvnqhzhqmjbvlbtgslzthlbbjzsgdglbrltzjdshpfbndjtssvsjqlstnrjdzzjvlpqhmwvrsvndcqrqjjcsqvmvrbhngtcfdprlbnqmhqllddgjpdzbjlphntrtgjrdgtbslrtzczbnnlddzzsvqvqvvzjpjqfhztgtsfggdppfdhzsbjzqjmpnmgqzlsdhjjbfpbsbnzpmhwrzjqhczrgcsflfwtrgwbnbrshjpwltntsnsdhmhqlmzdprcrcpcpjnphsmjwhzdqtncdbwgspmnfzsgmpbdhmslqchhhbbwfrghhnfjplsvrtbvplgrwdnbnfsgpwrqczvzlnfsngnsnbwvpmfdcmjztdnrllslnwcfwwnwsvztqmgqtfvmdqrrrmwfmphbcvwwttpmwjjbvqrmlwtwfsjdpcbmdlnlzcqntfzzmslshwprjfhwwpbbdfcdjwllfwcznwpjpwrlsfnnbgzjllrgtzcdcvhdhbtlrcvfdvsdjlzsmwwqvpzfhzjlqpfbqstvfrpcchmtwgbrhqqbglrvzmctdlpnvmglgdtzpbdngtfdnmsmwbgjstzbqwqcdlhfrtqqnhqvpfhdrjqvsvstftdgwwnwpfbfbdcfqnqlwpdnfhhfctwrgdqpbpbmgnfsnbpjfctvdtjnsfqlrtctrnjgltndngcmrdphhsqpjhprbngjzqqhnhhrdwlwwpmhzwshvrtzfgzlrhwghvpvfprbbvflltplpptvrmwcrdqndfqbfqtlqqwvphsmcvnbzghvsptrphhfcgdsslhfbcwhtjcmnpbvqrfgpsjgqpnnwwhjjwqrhhqgznwdzjqbtmmjljjwctqtfgwqbdrjwqwbbcftvjwfdfrgvsrlcrccpvfzdrcjvqfbhddpvrrhjrmhdgchrghbzsqpmgnmslfctblwlvphdfpvtdtwpdfsjwssmgnsvsqpdbqngccsplhmjbwjwtzwsbjhwpwcslqjdchmbvzrbgnwvjrrrdtvhtlzlrbwthzlhhqzzpvpwbzrrbrbtpwnhldhqqltqrqdddfwdmjzgctnlrjrjwvddfmjpnptdmrvnqjvsjfrmlvlqsthhsbvnjlsdzrjngfnqdjfssmvgrchbwmwbbvfqfhvrtwghmrpddnwbrbvbmqvfzbjdsnbzgrtmsfhmsmjtrqsgmpnwwbfwtp"""


T05_stacks = {1: 'Z,N',
              2: 'M,C,D',
              3: 'P'}
T05_moves = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

I05_stacks = {1: 'D,L,J,R,V,G,F',
              2: 'T,P,M,B,V,H,J,S',
              3: 'V,H,M,F,D,G,P,C',
              4: 'M,D,P,N,G,Q',
              5: 'J,L,H,N,F',
              6: 'N,F,V,Q,D,G,T,Z',
              7: 'F,D,B,L',
              8: 'M,J,B,S,V,D,N',
              9: 'G,L,D'}
I05_moves = """move 3 from 4 to 6
move 1 from 5 to 8
move 3 from 7 to 3
move 4 from 5 to 7
move 1 from 7 to 8
move 3 from 9 to 4
move 2 from 8 to 2
move 4 from 4 to 5
move 2 from 5 to 1
move 2 from 5 to 6
move 7 from 8 to 1
move 9 from 3 to 9
move 11 from 6 to 5
move 2 from 6 to 7
move 12 from 1 to 4
move 10 from 2 to 9
move 2 from 3 to 9
move 1 from 7 to 5
move 4 from 7 to 6
move 2 from 6 to 1
move 5 from 1 to 6
move 10 from 9 to 1
move 9 from 9 to 8
move 13 from 4 to 3
move 7 from 6 to 2
move 2 from 8 to 5
move 9 from 3 to 9
move 8 from 9 to 8
move 4 from 8 to 4
move 1 from 7 to 5
move 3 from 9 to 1
move 7 from 2 to 1
move 1 from 3 to 1
move 1 from 3 to 6
move 1 from 6 to 1
move 2 from 3 to 6
move 5 from 4 to 1
move 1 from 6 to 1
move 3 from 8 to 7
move 8 from 8 to 4
move 3 from 5 to 4
move 1 from 6 to 7
move 1 from 5 to 8
move 4 from 5 to 2
move 7 from 5 to 8
move 3 from 2 to 7
move 7 from 4 to 8
move 11 from 8 to 4
move 15 from 4 to 1
move 25 from 1 to 6
move 4 from 8 to 7
move 1 from 2 to 4
move 11 from 6 to 4
move 12 from 6 to 3
move 1 from 1 to 9
move 1 from 9 to 8
move 16 from 1 to 3
move 1 from 8 to 7
move 12 from 4 to 6
move 9 from 6 to 5
move 3 from 6 to 5
move 6 from 7 to 5
move 3 from 3 to 5
move 2 from 6 to 3
move 11 from 5 to 8
move 2 from 8 to 3
move 2 from 1 to 4
move 7 from 3 to 1
move 2 from 4 to 6
move 2 from 6 to 2
move 5 from 7 to 3
move 1 from 1 to 6
move 1 from 1 to 8
move 2 from 2 to 5
move 1 from 7 to 4
move 1 from 1 to 2
move 10 from 3 to 5
move 11 from 3 to 6
move 1 from 4 to 9
move 1 from 9 to 4
move 1 from 4 to 2
move 2 from 5 to 9
move 2 from 2 to 8
move 2 from 1 to 6
move 2 from 1 to 2
move 2 from 3 to 6
move 3 from 8 to 1
move 3 from 1 to 4
move 7 from 8 to 3
move 2 from 9 to 5
move 2 from 4 to 9
move 7 from 5 to 6
move 2 from 8 to 6
move 1 from 4 to 8
move 2 from 2 to 4
move 21 from 6 to 3
move 10 from 5 to 7
move 7 from 7 to 6
move 1 from 9 to 3
move 1 from 4 to 9
move 1 from 9 to 4
move 1 from 8 to 4
move 8 from 6 to 4
move 1 from 4 to 5
move 1 from 5 to 8
move 4 from 3 to 6
move 1 from 8 to 2
move 1 from 4 to 2
move 2 from 7 to 3
move 2 from 2 to 7
move 22 from 3 to 5
move 4 from 6 to 2
move 2 from 6 to 9
move 7 from 3 to 9
move 6 from 9 to 1
move 18 from 5 to 3
move 2 from 5 to 4
move 20 from 3 to 5
move 3 from 7 to 3
move 5 from 1 to 2
move 11 from 5 to 7
move 1 from 1 to 7
move 3 from 9 to 3
move 16 from 5 to 8
move 7 from 8 to 7
move 1 from 9 to 2
move 8 from 2 to 3
move 2 from 2 to 4
move 3 from 3 to 1
move 9 from 3 to 8
move 1 from 6 to 3
move 9 from 7 to 3
move 3 from 1 to 8
move 1 from 7 to 9
move 1 from 9 to 4
move 1 from 7 to 5
move 10 from 4 to 5
move 2 from 4 to 2
move 19 from 8 to 5
move 1 from 8 to 3
move 4 from 3 to 5
move 2 from 4 to 8
move 4 from 7 to 8
move 4 from 3 to 9
move 4 from 7 to 6
move 2 from 2 to 5
move 2 from 3 to 2
move 6 from 8 to 7
move 1 from 8 to 4
move 2 from 6 to 4
move 3 from 4 to 8
move 3 from 9 to 2
move 4 from 7 to 8
move 28 from 5 to 8
move 16 from 8 to 4
move 11 from 8 to 4
move 3 from 3 to 4
move 7 from 5 to 8
move 13 from 8 to 7
move 1 from 5 to 6
move 1 from 6 to 7
move 1 from 9 to 2
move 2 from 6 to 2
move 12 from 4 to 9
move 4 from 4 to 1
move 2 from 9 to 8
move 4 from 8 to 3
move 3 from 4 to 5
move 4 from 4 to 1
move 4 from 4 to 7
move 3 from 7 to 9
move 5 from 9 to 7
move 7 from 2 to 3
move 1 from 5 to 7
move 8 from 1 to 5
move 1 from 2 to 4
move 11 from 3 to 1
move 10 from 5 to 3
move 3 from 9 to 1
move 3 from 9 to 6
move 5 from 1 to 6
move 7 from 6 to 9
move 8 from 9 to 7
move 9 from 3 to 4
move 1 from 6 to 9
move 8 from 7 to 1
move 9 from 4 to 2
move 2 from 1 to 6
move 3 from 2 to 6
move 4 from 4 to 6
move 2 from 9 to 8
move 2 from 1 to 2
move 1 from 3 to 8
move 2 from 8 to 4
move 1 from 6 to 8
move 11 from 1 to 6
move 1 from 1 to 5
move 3 from 2 to 9
move 2 from 9 to 3
move 1 from 1 to 7
move 2 from 4 to 9
move 4 from 2 to 9
move 2 from 8 to 5
move 10 from 6 to 1
move 2 from 5 to 6
move 5 from 9 to 8
move 5 from 8 to 7
move 1 from 2 to 1
move 7 from 1 to 2
move 2 from 9 to 4
move 1 from 3 to 5
move 15 from 7 to 2
move 8 from 6 to 3
move 2 from 4 to 3
move 2 from 6 to 4
move 4 from 7 to 1
move 4 from 7 to 5
move 1 from 6 to 4
move 3 from 1 to 7
move 5 from 7 to 6
move 4 from 7 to 5
move 18 from 2 to 4
move 5 from 6 to 4
move 4 from 1 to 2
move 8 from 3 to 8
move 2 from 8 to 4
move 2 from 3 to 7
move 1 from 5 to 7
move 3 from 8 to 4
move 2 from 7 to 2
move 1 from 3 to 8
move 9 from 2 to 6
move 2 from 8 to 6
move 1 from 7 to 3
move 1 from 3 to 5
move 3 from 6 to 8
move 1 from 8 to 5
move 1 from 5 to 9
move 1 from 1 to 2
move 5 from 4 to 6
move 10 from 6 to 2
move 5 from 2 to 6
move 5 from 6 to 4
move 1 from 6 to 3
move 6 from 4 to 6
move 3 from 2 to 6
move 2 from 2 to 3
move 11 from 4 to 6
move 1 from 9 to 5
move 4 from 6 to 7
move 1 from 4 to 3
move 12 from 4 to 3
move 1 from 8 to 6
move 9 from 5 to 7
move 1 from 5 to 2
move 1 from 8 to 5
move 1 from 4 to 9
move 9 from 7 to 9
move 1 from 3 to 4
move 2 from 3 to 6
move 2 from 5 to 6
move 2 from 8 to 5
move 11 from 3 to 4
move 2 from 3 to 1
move 1 from 2 to 3
move 1 from 3 to 8
move 3 from 7 to 9
move 5 from 4 to 2
move 2 from 5 to 8
move 6 from 4 to 2
move 1 from 1 to 3
move 12 from 9 to 1
move 6 from 1 to 6
move 1 from 8 to 4
move 1 from 8 to 3
move 5 from 2 to 7
move 2 from 3 to 9
move 5 from 7 to 1
move 1 from 7 to 5
move 2 from 9 to 1
move 14 from 1 to 7
move 2 from 4 to 7
move 7 from 2 to 4
move 1 from 2 to 1
move 1 from 1 to 3
move 1 from 5 to 4
move 1 from 9 to 6
move 16 from 6 to 5
move 2 from 5 to 4
move 12 from 6 to 8
move 10 from 4 to 8
move 9 from 7 to 3
move 4 from 7 to 6
move 11 from 5 to 8
move 2 from 5 to 2
move 14 from 8 to 9
move 1 from 5 to 1
move 3 from 9 to 4
move 2 from 2 to 1
move 7 from 8 to 3
move 6 from 3 to 5
move 8 from 9 to 8
move 1 from 6 to 1
move 1 from 4 to 2
move 4 from 3 to 8
move 1 from 7 to 2
move 3 from 1 to 5
move 2 from 5 to 7
move 3 from 9 to 2
move 1 from 1 to 8
move 5 from 5 to 4
move 2 from 7 to 8
move 4 from 2 to 5
move 1 from 2 to 4
move 2 from 7 to 8
move 4 from 6 to 2
move 6 from 5 to 3
move 1 from 6 to 5
move 1 from 5 to 3
move 1 from 3 to 8
move 8 from 8 to 3
move 9 from 8 to 5
move 9 from 8 to 2
move 2 from 8 to 9
move 2 from 3 to 8
move 5 from 5 to 8
move 1 from 3 to 7
move 2 from 9 to 5
move 7 from 2 to 4
move 14 from 4 to 6
move 2 from 2 to 7
move 1 from 7 to 3
move 1 from 7 to 9
move 3 from 5 to 2
move 1 from 7 to 1
move 3 from 2 to 4
move 7 from 8 to 2
move 3 from 6 to 1
move 17 from 3 to 1
move 2 from 8 to 3
move 6 from 2 to 7
move 2 from 7 to 9
move 3 from 6 to 8
move 2 from 8 to 6
move 4 from 2 to 1
move 3 from 4 to 7
move 1 from 8 to 7
move 1 from 8 to 9
move 1 from 4 to 2
move 3 from 5 to 7
move 2 from 3 to 1
move 2 from 3 to 5
move 5 from 7 to 4
move 5 from 7 to 3
move 1 from 4 to 8
move 3 from 3 to 1
move 6 from 1 to 3
move 1 from 7 to 5
move 2 from 9 to 2
move 3 from 5 to 8
move 1 from 8 to 1
move 8 from 3 to 5
move 1 from 4 to 9
move 3 from 6 to 5
move 3 from 6 to 3
move 2 from 3 to 7
move 1 from 4 to 7
move 3 from 6 to 4
move 2 from 7 to 2
move 1 from 7 to 8
move 2 from 5 to 4
move 1 from 6 to 1
move 7 from 4 to 7
move 7 from 5 to 2
move 10 from 2 to 3
move 3 from 2 to 6
move 3 from 8 to 1
move 1 from 8 to 7
move 2 from 6 to 3
move 1 from 6 to 9
move 4 from 7 to 5
move 16 from 1 to 5
move 1 from 9 to 7
move 3 from 7 to 6
move 11 from 5 to 6
move 2 from 7 to 9
move 12 from 6 to 4
move 2 from 6 to 9
move 6 from 3 to 2
move 1 from 5 to 7
move 5 from 9 to 5
move 1 from 9 to 6
move 4 from 3 to 7
move 1 from 4 to 2
move 7 from 2 to 5
move 3 from 5 to 2
move 6 from 5 to 6
move 3 from 2 to 6
move 9 from 6 to 8
move 5 from 5 to 9
move 5 from 7 to 1
move 4 from 1 to 9
move 2 from 9 to 4
move 1 from 6 to 7
move 9 from 4 to 1
move 7 from 5 to 9
move 18 from 1 to 3
move 9 from 9 to 5
move 8 from 8 to 2
move 1 from 2 to 5
move 4 from 2 to 3
move 4 from 9 to 6
move 1 from 4 to 8
move 2 from 5 to 7
move 2 from 9 to 2
move 10 from 3 to 9
move 5 from 5 to 9
move 1 from 7 to 2
move 2 from 8 to 7
move 2 from 3 to 5
move 2 from 9 to 1
move 2 from 7 to 3
move 1 from 2 to 1
move 5 from 5 to 8
move 1 from 2 to 1
move 15 from 3 to 6
move 1 from 7 to 6
move 10 from 6 to 5
move 1 from 7 to 8
move 4 from 1 to 6
move 1 from 8 to 3
move 2 from 1 to 5
move 3 from 8 to 1
move 1 from 4 to 6
move 1 from 4 to 2
move 4 from 9 to 7
move 6 from 5 to 7
move 3 from 1 to 9
move 10 from 6 to 8
move 2 from 1 to 3
move 8 from 7 to 9
move 1 from 9 to 6
move 2 from 7 to 9
move 3 from 3 to 5
move 1 from 2 to 6
move 2 from 6 to 5
move 5 from 9 to 4
move 4 from 8 to 2
move 1 from 1 to 3
move 4 from 5 to 9
move 3 from 6 to 1
move 2 from 1 to 5
move 3 from 5 to 2
move 8 from 8 to 3
move 11 from 9 to 4
move 13 from 4 to 8
move 2 from 9 to 2
move 2 from 3 to 1
move 1 from 4 to 1
move 1 from 3 to 8
move 2 from 6 to 9
move 7 from 8 to 1
move 3 from 2 to 5
move 7 from 2 to 5
move 3 from 4 to 6
move 4 from 9 to 2
move 2 from 3 to 5
move 9 from 5 to 6
move 5 from 2 to 7
move 2 from 9 to 2
move 2 from 9 to 7
move 12 from 6 to 8
move 5 from 5 to 7
move 1 from 9 to 8
move 3 from 1 to 6
move 5 from 5 to 8
move 6 from 1 to 9
move 2 from 1 to 5
move 1 from 6 to 9
move 5 from 9 to 7
move 2 from 5 to 8
move 11 from 7 to 6
move 20 from 8 to 1
move 2 from 9 to 8
move 4 from 7 to 6
move 6 from 8 to 3
move 13 from 6 to 9
move 4 from 3 to 2
move 4 from 6 to 3
move 2 from 3 to 6
move 5 from 9 to 8
move 2 from 7 to 1
move 2 from 6 to 9
move 6 from 8 to 3
move 6 from 3 to 6
move 5 from 2 to 9
move 22 from 1 to 3
move 3 from 2 to 1
move 5 from 9 to 3
move 1 from 1 to 6
move 3 from 6 to 2
move 1 from 2 to 4
move 33 from 3 to 5
move 1 from 8 to 7"""


T04 = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

I04 = """8-17,16-49
17-38,18-36
17-43,43-43
86-94,7-87
23-97,22-85
8-50,7-50
82-84,1-83
43-95,51-94
7-89,8-90
85-90,21-70
46-69,7-46
93-98,18-99
42-85,53-92
25-65,64-65
13-53,12-53
59-90,60-95
1-79,58-78
99-99,16-96
56-86,86-86
49-50,50-51
79-83,80-83
31-86,8-20
8-85,9-86
34-81,35-35
7-87,8-95
14-50,49-51
2-65,1-1
37-37,35-44
17-72,3-39
6-25,24-26
56-94,37-93
49-76,36-75
26-37,25-53
98-98,10-97
48-87,49-97
31-82,30-90
5-98,4-93
77-97,76-94
96-98,1-97
67-67,68-95
26-51,50-50
43-67,66-67
31-68,30-90
36-64,65-92
2-2,3-11
57-60,22-58
43-55,44-56
8-81,80-84
2-52,2-2
28-83,76-77
20-83,13-82
23-87,22-72
11-92,91-91
52-84,5-51
74-78,67-97
48-66,67-67
86-86,39-87
5-6,7-54
14-15,14-98
48-89,59-74
51-75,52-67
6-35,16-74
65-98,44-96
10-85,84-84
26-96,95-95
21-96,22-22
13-69,12-68
67-67,47-66
64-70,71-71
59-96,16-59
69-69,56-70
12-90,20-97
6-45,5-98
89-89,39-88
2-69,1-3
19-33,27-33
69-97,94-94
2-98,97-99
22-88,22-38
2-80,1-1
64-64,63-63
21-22,21-79
18-88,19-89
44-57,43-56
55-56,3-55
40-76,39-84
71-94,70-94
22-23,22-83
2-12,15-26
37-72,12-45
4-79,3-61
2-33,33-34
33-82,18-32
1-99,2-95
7-79,7-79
62-99,2-99
88-94,18-96
35-38,38-38
26-27,26-56
8-64,2-8
11-11,13-88
69-90,17-44
21-22,22-42
38-38,37-37
16-52,10-15
24-82,24-82
9-85,2-26
28-99,1-97
86-86,25-85
9-66,9-27
73-73,74-90
18-99,19-98
85-93,92-92
23-55,23-97
6-79,80-96
31-62,37-42
42-44,43-49
20-85,73-86
56-96,13-94
2-17,8-16
1-59,5-84
46-55,4-77
65-87,16-87
41-87,41-42
1-94,2-92
24-91,24-24
8-67,6-25
89-99,84-96
23-67,2-24
6-38,1-2
67-92,72-98
3-22,7-80
11-53,5-11
62-62,33-62
30-96,31-96
32-99,31-32
15-15,14-70
2-3,14-75
37-56,38-44
46-82,82-82
58-59,32-58
7-43,6-42
25-26,26-84
6-91,92-94
3-69,2-70
11-80,3-9
56-57,57-82
26-68,25-67
43-47,7-46
39-49,2-38
50-51,32-50
85-85,86-98
8-56,5-57
16-83,17-83
43-93,44-92
65-67,18-66
19-76,19-75
33-55,39-68
43-44,38-43
22-26,21-27
1-4,3-68
50-65,26-64
33-94,98-99
52-99,50-50
26-43,20-42
19-37,37-50
2-99,99-99
4-94,3-93
88-95,3-87
71-98,88-98
11-58,10-11
7-93,5-92
98-98,62-82
22-43,43-44
21-28,25-28
56-56,58-63
9-10,9-85
66-87,66-67
8-79,78-78
25-79,78-80
40-40,40-62
5-98,6-99
3-34,28-99
22-93,21-97
26-42,25-97
39-48,38-42
32-50,32-32
14-91,93-93
8-62,7-89
27-93,26-93
64-66,59-65
7-77,76-78
11-72,63-71
54-81,22-80
3-89,89-89
28-80,81-81
9-91,19-43
17-90,90-90
24-75,76-81
31-52,15-24
38-75,39-76
40-55,42-91
95-95,67-94
12-95,11-95
8-54,54-55
18-29,28-53
41-41,42-76
98-98,13-98
23-99,14-27
45-45,10-46
2-70,81-98
14-88,13-90
21-58,28-66
23-24,23-90
12-70,11-85
15-15,16-75
46-48,26-45
78-86,41-98
84-84,83-84
73-81,54-84
19-65,66-88
74-97,74-98
7-86,6-7
18-27,27-29
91-91,10-90
4-8,7-32
21-42,21-42
19-69,20-99
67-68,17-67
30-79,29-89
2-86,1-2
38-54,40-65
28-48,20-29
1-42,43-43
20-41,16-41
8-14,1-13
19-90,18-20
90-91,4-91
1-89,1-89
81-93,83-94
29-66,29-29
28-50,10-50
2-28,2-84
25-67,24-26
35-53,36-37
9-99,6-9
20-78,23-91
36-61,62-62
15-39,14-31
67-73,15-66
33-99,62-90
42-69,70-70
79-80,80-81
88-88,41-89
2-84,84-84
31-74,32-75
9-87,9-94
61-99,61-89
2-99,3-16
42-57,43-58
23-83,23-94
4-97,96-98
2-99,30-36
32-80,32-81
7-31,8-14
4-65,4-65
7-8,7-41
44-64,64-72
86-95,21-87
96-97,63-96
10-94,11-96
14-82,38-85
9-77,10-78
26-87,2-5
96-96,80-95
45-88,44-89
44-44,45-74
37-91,38-89
68-86,85-85
54-67,66-98
24-73,23-72
89-90,88-89
51-71,1-51
10-25,24-26
85-86,36-88
72-72,55-71
2-4,4-50
68-92,67-91
83-86,82-88
71-71,67-70
95-96,6-96
7-99,2-98
77-82,65-78
57-97,19-47
81-91,82-82
11-17,16-55
95-98,50-54
66-98,65-67
1-94,93-96
9-47,10-48
91-95,13-92
4-64,8-63
26-27,26-96
11-60,6-11
28-28,27-82
49-87,50-76
2-96,1-97
29-73,20-29
72-72,73-82
12-68,67-67
98-99,1-97
12-13,13-78
33-65,66-73
34-62,36-67
63-93,64-92
2-45,8-42
11-99,12-97
11-88,6-89
23-61,58-58
16-96,24-95
2-70,6-69
31-90,90-91
9-25,7-8
23-69,23-24
54-64,53-54
15-22,22-56
3-80,2-40
35-39,34-39
20-45,8-64
19-96,18-99
11-72,1-16
24-73,42-73
23-48,47-89
13-82,14-83
42-64,42-63
6-20,5-17
2-6,3-7
35-96,99-99
33-83,34-83
6-6,57-93
67-81,82-82
13-97,12-84
5-64,5-97
31-91,30-97
76-95,75-77
30-92,91-92
19-86,19-20
11-45,3-46
2-37,19-98
11-20,12-32
28-98,97-98
2-94,2-94
1-99,99-99
28-44,40-49
8-46,7-9
36-95,35-94
14-91,15-91
23-74,24-75
24-45,27-46
39-62,26-38
13-15,14-95
22-84,21-21
2-89,88-99
12-69,68-83
24-92,10-60
4-97,9-94
29-74,34-51
9-9,10-91
97-98,33-96
21-66,67-67
2-95,1-89
34-35,36-57
84-84,13-85
5-49,6-50
47-97,48-75
23-96,24-76
4-59,2-3
4-99,5-92
2-95,1-99
14-72,9-71
40-95,41-75
15-96,97-97
9-50,49-51
55-77,76-78
97-97,7-96
92-93,3-92
40-74,39-84
82-87,4-83
2-81,3-77
18-82,17-80
13-80,81-81
20-81,80-80
9-96,1-6
84-89,88-88
6-77,5-76
37-74,69-76
95-98,3-96
26-87,87-88
2-43,44-44
5-89,58-94
34-75,75-75
88-91,19-83
23-78,28-77
64-75,76-76
32-46,31-46
2-13,12-76
51-96,50-99
91-91,32-90
3-76,66-81
10-94,8-96
88-89,14-89
2-40,91-98
29-84,30-85
13-14,13-79
2-97,98-99
1-52,2-51
75-98,40-93
90-98,19-91
47-49,8-48
20-96,20-21
20-87,21-43
50-87,97-99
1-38,77-84
86-92,85-91
15-15,14-14
19-87,71-88
22-66,65-67
9-96,1-97
12-94,13-76
43-68,69-92
18-60,59-97
3-91,1-1
8-26,7-27
7-99,7-98
22-65,65-87
98-99,8-99
78-93,35-79
3-18,17-76
82-86,81-85
2-5,6-95
38-63,64-86
13-54,6-93
37-90,37-89
21-35,36-94
34-95,33-91
4-37,3-8
1-3,3-82
99-99,40-99
7-8,7-94
49-49,3-50
16-72,71-73
3-6,6-13
11-92,10-10
12-12,11-88
42-75,43-91
99-99,88-97
46-48,7-47
20-91,17-20
75-76,27-75
93-95,34-94
26-63,62-62
45-50,46-59
7-70,8-68
41-42,42-60
50-51,51-86
34-59,58-88
53-94,63-99
4-79,5-91
20-23,14-78
98-99,15-99
15-15,14-53
33-40,63-86
8-91,14-91
94-95,3-94
55-83,74-84
17-18,17-91
4-81,3-3
26-26,27-84
85-87,48-86
32-41,42-42
98-99,42-97
80-87,81-84
93-96,1-94
31-87,33-87
26-27,18-26
40-40,41-89
86-88,25-87
6-14,14-15
32-67,31-68
45-45,44-90
96-96,5-95
61-76,62-75
46-78,45-96
4-92,3-93
48-56,61-70
83-85,82-98
89-89,73-90
2-56,20-28
45-55,45-54
12-87,87-87
2-91,1-94
91-92,32-92
2-85,1-84
98-98,51-97
90-91,81-91
15-90,17-37
3-97,1-3
7-74,8-77
46-75,45-45
82-83,24-83
17-25,24-80
11-96,11-12
32-81,31-69
21-96,21-22
76-98,76-77
42-88,48-82
60-61,18-61
7-73,74-79
24-99,25-80
85-85,2-84
92-92,93-93
59-59,60-99
95-96,9-94
23-92,19-91
11-94,93-97
14-91,90-95
46-77,77-77
46-47,47-53
3-47,2-3
12-47,48-65
4-44,4-5
26-33,32-77
31-81,81-81
3-48,48-49
4-7,7-93
34-80,80-80
50-77,51-78
28-43,75-82
36-89,51-60
10-87,86-87
1-99,1-99
2-89,49-99
23-36,37-37
8-13,13-62
22-24,23-68
18-18,18-93
32-49,33-51
73-91,74-92
10-59,44-58
2-59,2-59
3-89,89-90
15-94,5-95
42-88,88-88
7-95,7-7
1-75,1-75
12-12,12-86
93-94,2-93
80-89,80-89
14-91,95-95
38-98,38-97
96-99,11-97
69-70,50-70
13-81,80-82
25-89,26-81
47-48,32-47
4-19,3-27
34-64,33-33
10-90,2-11
5-98,4-99
6-90,89-91
41-52,41-53
48-87,49-77
2-53,5-74
82-99,66-84
59-60,11-59
22-57,21-56
38-81,81-81
51-81,3-51
25-73,26-36
98-98,3-99
96-96,1-95
50-72,49-49
91-91,2-90
61-96,60-61
10-45,11-15
65-66,49-66
82-87,45-83
59-59,3-59
5-72,4-73
56-95,55-56
13-83,14-96
52-59,52-59
44-46,42-45
11-93,11-35
74-92,16-81
98-99,17-99
20-99,1-93
37-86,46-51
15-16,16-98
1-97,96-99
73-75,23-74
94-99,24-95
94-99,26-95
39-39,40-80
58-89,57-59
84-93,19-93
7-43,43-98
23-82,21-23
2-59,1-98
93-93,12-73
9-99,9-39
42-61,53-81
12-79,11-69
33-62,34-80
11-99,8-10
44-89,43-82
7-71,70-71
11-99,98-99
87-91,92-97
2-93,3-94
58-79,64-80
24-62,24-25
3-86,3-3
4-90,2-2
3-90,4-91
9-87,9-87
23-57,22-57
4-13,14-87
11-23,24-24
35-68,7-46
3-3,4-80
6-47,36-71
21-93,92-97
6-65,5-86
21-22,8-21
22-55,56-78
51-85,84-84
17-95,94-98
32-61,32-60
63-63,63-63
48-65,56-66
3-33,4-32
7-76,71-79
34-66,37-82
21-65,25-66
3-79,4-80
17-88,95-99
26-26,27-92
81-95,3-80
56-97,3-55
58-86,23-86
84-84,21-84
82-84,29-82
26-80,79-79
40-41,39-52
27-85,26-86
39-39,6-39
29-89,28-28
11-42,11-12
1-66,67-67
15-83,82-83
50-93,51-92
78-80,83-96
6-96,7-94
10-11,10-45
18-40,12-19
31-55,7-32
18-19,29-83
29-29,30-80
35-37,36-99
94-94,28-94
48-98,49-99
63-66,60-62
4-62,62-62
77-84,85-85
34-34,35-47
68-90,20-69
6-68,39-88
8-99,7-99
49-50,17-49
74-85,73-85
88-94,27-87
4-89,88-88
8-84,7-83
60-64,60-64
94-94,95-99
43-91,41-99
92-92,91-91
67-67,19-66
19-99,18-96
47-79,78-79
8-48,22-38
35-59,32-35
5-45,6-46
20-90,19-89
14-55,12-13
34-34,34-43
3-96,4-99
39-40,40-65
83-83,25-82
15-92,14-91
12-12,13-82
43-57,43-57
3-98,99-99
30-66,65-67
92-95,86-92
48-52,13-42
1-7,10-64
60-98,44-59
64-86,65-85
29-97,96-96
49-85,2-50
35-38,33-37
6-8,7-63
1-90,90-91
7-56,8-74
2-61,2-3
79-93,41-96
6-47,5-6
10-87,11-42
93-99,35-94
13-62,21-62
11-49,10-10
2-55,54-54
59-68,3-27
1-96,1-96
38-75,39-76
29-51,51-92
6-61,7-60
24-25,25-90
27-32,28-31
16-47,1-46
20-88,7-18
24-74,25-25
40-86,41-90
8-97,3-97
95-95,1-94
11-36,12-79
8-98,3-99
28-28,29-30
20-86,21-85
42-58,61-88
43-58,52-69
67-92,32-75
81-97,44-89
19-90,89-90
12-92,11-13
27-89,28-89
16-97,17-98
91-93,27-90
15-95,14-95
84-84,10-83
35-35,34-87
14-65,15-78
25-90,91-95
19-21,20-93
12-92,11-95
48-60,47-61
11-92,10-93
6-68,67-69
19-57,20-20
33-45,23-46
6-6,11-99
2-96,2-3
11-21,7-12
9-48,47-48
19-57,2-19
15-96,14-44
78-82,12-79
21-76,5-7
8-31,24-59
52-99,52-53
9-90,89-89
1-3,3-89
18-92,15-93
15-35,16-99
1-7,6-83
7-86,61-85
19-89,19-89
57-98,56-97
22-22,12-23
1-1,1-20
21-23,22-94
44-46,45-47
10-90,4-11
30-84,29-83
55-73,55-73
62-73,14-63
59-81,47-58
27-64,28-28
33-79,55-84
14-50,13-50
77-98,76-95
23-69,24-70
80-82,1-81
27-92,17-28
4-49,50-71
42-85,41-98
97-99,15-98
21-59,20-58
64-98,99-99
90-90,62-91
58-69,70-94
90-96,10-90
95-96,65-96
4-55,3-62
19-71,70-83
1-2,2-2
13-99,12-14
98-99,43-98
3-35,36-36
26-88,27-54
1-99,2-98
11-11,9-10
94-99,19-93
16-85,66-86
53-65,53-65
42-63,63-71
87-87,57-87
35-60,34-60
31-84,38-55
7-76,8-77
1-78,2-2
78-93,52-79
83-96,83-96
82-84,83-85
1-25,1-19
97-97,19-98
78-78,24-77
7-81,6-6
18-84,81-88
46-89,47-90
20-93,61-93
11-51,2-52
94-94,56-94
8-99,98-99
1-2,3-51
6-96,95-97
9-10,9-66
98-98,69-97
64-64,65-78
38-98,97-97
46-52,40-50
74-78,1-75
2-56,5-55
48-54,47-53
35-67,68-98
8-68,68-83
95-97,35-94
13-69,14-91
42-71,71-72
24-40,23-39
65-98,64-89
4-95,5-86
53-84,84-84
29-98,30-99
4-98,3-5
96-96,1-95
50-84,85-85
41-78,25-78
4-84,84-85
15-47,1-45
86-89,50-93
41-82,15-94
18-32,33-35
27-93,26-27
2-90,89-92
52-55,51-77
34-43,33-42
3-3,3-99
93-97,33-94
74-99,5-75
27-99,24-99
27-28,6-27
1-2,1-57
19-82,19-83
37-73,36-72
29-53,5-53
21-94,94-94
8-57,57-91
58-59,57-58
3-3,2-3
43-80,12-27
81-99,82-91
48-49,14-49
13-98,12-95
14-98,13-79
67-98,97-99
31-84,32-32
1-91,91-94
2-2,3-96
1-99,1-1
22-93,22-90
1-92,1-2
28-88,1-1
16-94,15-16
36-70,69-70
14-85,84-86
21-54,15-98
39-61,39-60
54-56,9-55
9-45,45-46
14-19,14-20
2-53,53-53
58-69,68-68
76-98,77-99
21-73,22-49
9-96,8-95
1-50,1-49
28-67,29-98
41-78,40-79
95-99,46-96
9-88,8-10
19-73,7-74
29-65,29-66
98-99,23-97
44-44,43-47
9-60,61-61
39-64,38-65
56-81,55-56
74-75,74-90
72-95,10-66
3-86,2-2
16-26,25-26
13-61,6-51
4-17,39-46
39-97,40-76
36-52,37-51
41-96,40-40
23-70,69-71
10-90,10-87
29-81,30-76
89-89,89-89
11-96,12-97
11-80,55-80
4-94,93-97
11-94,10-93
78-78,22-77
53-98,53-98
6-53,33-63
13-14,13-30
94-96,22-93
22-96,95-95
40-40,41-78
66-66,4-66
40-91,50-76
61-91,87-88
2-50,3-49
98-98,1-99
10-28,14-31
44-95,51-54
31-59,30-31
10-94,9-92
40-47,39-40
3-88,4-89
64-86,7-86
33-37,32-35
10-11,10-60
95-95,3-94
16-84,16-99
96-97,20-96
25-91,91-92
3-3,4-95
15-91,20-91
59-90,16-60
5-53,52-54
3-99,4-4
23-43,24-44
26-91,53-91
4-73,4-5
64-64,2-64
74-74,51-75
35-51,34-34
72-87,86-88
3-92,2-2
55-87,56-56
69-81,70-82
42-78,17-42
51-58,54-58
76-93,94-96
4-88,3-88
53-60,54-64
2-75,3-15
13-56,55-72
3-26,9-9
17-55,18-54
39-75,40-55
12-31,13-52
91-97,46-91
35-56,35-72
46-46,47-47
10-10,11-47
19-54,18-82
1-97,2-97
13-46,13-46
6-95,94-95
16-33,16-33
26-26,26-99
42-83,78-79
5-17,4-67"""


T03 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

I03 = """CjhshBJCSrTTsLwqwqwb
GtmnFHlDfcpHbLZjtTTRLWwb
fDfNHHjVFNvvrvVBJJdS
PPWvWQjPhrPQwlMWJJdMDGbJTdCJ
rsqsStgNNggBNBZHSrJGdJdCFRRZCFbGbTdJ
qgBqqHzzggBpzSnBNqNSSSgcfhrVlVmwPljQVLVwVvQmmzVl
bBBGBfmGvBTnGtGJBtGpcJbZrrddjqrZhDldwdcqrjrjDr
HWPSQMsPHFsMWPVVMVSHCwDCDwwZZvwjwQZZwjdd
vVHPgHHFRLfpfJTLLtJL
LWLZhDBHhWWHjBwHwBjCTrBnnrQTQCJTJpTQBQ
vvdcqbRmvwSFmRqPFSqwdvtQnrpCQJpNNVnrptVCtCCP
wRSffqlFgvvdgdlzhLWWDzLljZhhGL
LNbTbPdTNgnShgSjmHcqtQGCtrctCPcQqc
vzWZDZZBlDwlzvDRZfFBRzVBtMMGHCcpjrqBGMtQQppqHtCq
DfRvFZjZRsRjlVWsjFlWVWvdSdbhsSmnSngTdTSTsJdSLm
nnZRbfZRTZfRsbZTFPRfpbRJdqqQNPwNqvvwvvvSwdQqdS
WjDzjMWMHpQwcSQWcJSS
hrHhHDgpphmjtMrGLDmGgmnbsflbfZCsnsClltsVsfRR
QFngsFnGdLGFGVRgLLqWPQPWvBrMDppCPrDB
NfcHZZzbHthSZtNtNfhHWhClDvCqlrqBvrCpWMWB
fSMSHjbTMVgVVngVgT
llnMffwbvCnffHvJJPJpPBNVVZDJDmmS
QssGGHhRgcqjRRTWGWRGDZcVFZBpNBmPFBDSmZNP
hzsRHWQshzgRjjsgQRTsbwzCtnrrlnrwzMCtvMff
HdddHHmtDMDTqHHSftmqdmfdssGzrsjVGtrllWlGZGsnlnnp
BQNPNPgPhBBhCJQhbCgCnrrnbZnlWznzpGssllVW
LFNZRvCPCFZmHmTLcwdwcq
zQRDChCnVhqRllpzQlzqCVVzPvNHTTFFHlNPsPNvTBPBHBFT
wcfdfDmfPHjdsHPs
cwGMwMMbwbmwJZfDSMmfwcpRVWzQqnnnzGVVnhqRVCph
CScCSPcPszFJWSMjGZHMpGMjvG
TTQfQvBTVBfrDVRDVqGMmjZqnpnGmMpnnpZZ
NDdbrQdVQDNNfvTVNdBfrDBJFcsLWcCJzWFCcFLbFcFJsc
WWdzhpHcHHrtzGBJMwmjJGmBtP
CqsgqNrVnlCBCvPjCBmPJm
LDDDLnVsqsgTQsgFcQzbQdprbWHzdb
nFpNPGLGrntlrFLpflfBTcJwSgwQvGwbgSvbvJvT
DHZWmMDZZDHPMHsDJQbbgSJcvbQgjwJM
CRdzzdDDVRHWWNlPfPzllnFLlL
ZJVqGSVCJCSgdSvtjtvcjcjbNl
pmDWFnDFMnDdFLDHffjcbjjtBNctBjBMbMcl
dLnfmdLLmrWsgZqCThgssgsq
CLsvLLQvrlrrpLpw
tmTHnNtgmzgWmpjlpjnwrrlRjw
WHgTdmNJmJTDDrtFWsVGQqBQqcCCbhdvCB
jwCHwmWRTWRWJwfcgVgflvPqPBPH
MpphdbZZpZMNZpsdpZLMgjBlBqDvLPjfLVPBgPfv
ZdrZsjQbnMCGwrRwzmTr
CMDsWppsfhjNNzzzcBrbPgnrrnVBQHBNrV
ZmGdTdvtStFDtTvtBHgPHnPHgnrnHVmH
ZtLZdwdGqtZqLTLtwvfjDWcRscqMCDsCfWjf
QQPPfPjLNLfSShfNRSRrrGHzvHrvlvnHRDJJ
WCMJJVBwbGCbnbCl
gBJmTBBMchsSjgfS
NvCQGNRQQrWRpWhhvQrNLgrJqTVzzLFZsJqJZFcJTqFMJJ
ttdBllbCSdcsJVVVzVMb
CnwfwwdlnPGQgpnPvv
WQmnmBBmWRCgDpndbD
SvjsqGGqTSTdbggS
lZbFJqLjvHZrcZNHcc
gcgQhclQlntnnvBMZlwffTBLwv
JqzNpqbmpJCbbzCfNFFqfWpZvDVTqBMTrTLvrTMTrvrZTT
NbJWCpRWSFWNWJCzmRNRdchcdHcchnfncnhntcdjng
JvDwhPWPzvzPDggWlvCQgPtHgtGnHtNqLqTnHTHHnnVg
jBsfcbpdQsRcsSpRcjZjHNGtnnVncVtqTVVNVNNT
prBbsjQdSbZdSFwMzrhPMWwzwlvC
SStQfWQmJQjjhphQ
sMVTwvLTswLwwqMPnnhglbHgglPh
RDrRVrVCsrssBFWffFCZthfNFN
ZnpgzcqgmhHtfwSDwplwVV
QCrBNLdLrrnSVSrl
LQQLLLjTBjGWnNBBGLFZbGgMcsMsZzbgbZZgsZ
ZnbzbhqPbMrnDGjtQGSRVVMGpf
gFdTlNJFGVGChJCt
HgswWLNdhwTTwWsNNvzPmbvbcZbrsbrmzP
SHpDqcJvBmJgJJHgDphHmvhTddWlLsZTTdFWMMsWtthZ
GPrRCPfRfjjwffjrrnPVPsTLZFwLWMzLdTsTFzzFWT
QPfZVNfbfQnRVjCRrPJBvSJgpDSDBHNgBJpB
mjpcZcHcrqjrNmNpNmptHNHWwvCwgwCgMmQgRQsRMgwMvnCg
DfSfFSVtDSTJVfdGJMwPnMRwnRCPQgMR
DDfzDVdbTbzVDDtrtqlHptqbjbql
lsBgqLqhqqgBBvGLBwQJJHRpJCJDHMwhwz
NCVfntPnVnfrZtfdbTntnnWDDMDwwRRJmJDWRWJmHRzpJD
ZrZbtbSZfdNVfbtCrbPTndsFvFLFSqcGLBFgvgjsgcqj
gwRCCDmlZtPDdtBBPM
VLrjccJVcJTfTtLjscVBHjHPjPQQSPpBHMjBhP
rfcJrzvvctrscvzRqGRCZvmqbmwqZw
nffqBWfRfRnpBfznpWTpTlWNNbcrDcbGbPhrGVwGlllPGN
MsJQsmQLjMMFsmjbPZNcNbrbmGVhZZ
LCJsFSsJFMFpfrTBWSvqpB
vSspfvprpTNTZNTj
LlFQCtnwMqqSmCMPmMSwClCJhBDJZZJZZjBTjQNjJbdjTT
PHtwMLPqCHsfVRGvSR
HjLDQMjtRvTmfTfmtf
BddChcvvhwhqgmqTfnSmdg
NBVVZJhZVhZsJJzhJZNHrRMPbQvHrjPvPDRvRN
GgwtwntLQmNjvRGJGv
wwzWzrzrqWjRlhJrNlrj
wBWSCMPMcdnHsTHPsn
MggMDDJzdbvsjCJvWJnJ
THBGGScfHwHqHGTGTBqfSWCsnWBCbvsbshjRnZWZCn
HwltftNGtmHHGqNlGmfPrVDDgzpVplpzDpVPbP
shMdsCMpQMCZMQsZQVDJnvvPpPLSvLSLLV
RmgzGTGRmClLNCvzVn
rCrRftmftWjbTttjcdFZBcjdsFqZQFjZ
qLwvNLtLvPGqSltLLqvNSpflMfQfMpMnBBggslMpfB
VDcVzzDRRVTDgMPBBgdfQD
VVWrcHbVzrzVjHPNqSmtqJJwjLGN
nBswlBBhntTttbFVnt
JNjTHZvLHDLVVLtCCFFPLz
THvNddgZWQNDNZgjZSfGwfsBrhmfGBhcWs
cCSbPmJqwqJjgJtTzJZT
BpBTFFTQZzQgNgZv
sFRVpsfrfrLfslwTcTccwcnCcTRC
DLjLwDPjVPnWWvVWVjcqzSCJTzSzMTtSrqRqJn
bdNGgmbGHdZdHbSRqrTJzrMtTR
dhGmFffGQsWjshcVpt
TrGzZpzWhCHcPPpF
sqsJqtlqDVDJVJttgNSbsQPfcjQcBQjhFFRSPQHFRc
VgqbtllbdvNtDdLZrHWGmwdrLM
DNrqBvvZZNDDHBFJmMNbLMRctztznRsbds
hlSlPPWfQCChPtWWfjTwLzbdRcbMsbMjnRLsgzsz
PCfWwlQpTTVmmtqmVGrvmt
lLrlLRbgrjRbRjFlRrnRRdgPdWdCwdWqmWPwqScdPc
tDZLNGHsNQZDNBGHTCVSddVCPwVqVtcdWV
BhGLBNvhHDTZDjfRvbfjljbbJf
McRctHfDctZGlZZWgpcW
TTQLQqLSLqTqhdLqPzLqLwrpsGpWVGFZGrlgWZGhFllV
QNdzbQgzSvqPzqNqvnnbtfbRfDntCfMRjn
bHQvFvffjpVvPSTvVm
RDLRRDLBnVbsDsqDSb
MtGGtJJnwnLltblMFCHfQcthjNfjHCQN
FQfFldFCSRRFQSQmLVfRGwGDDGZDhDGwmmhZtthZ
cTpscpCcNzNNvCBgbPPwvZGZggbghb
TNzznnccTjTspHWNzCTpNlRRQnlfdVFVfLLJFrFJQQ
LsMMLCQQQMTJnJMnsJlGlZJNvbNVGNNSDJ
fhcBqmfvmtRftcmfVVNNVbZSSDVGZmgG
BztFRjFjBchWzhvWTHWTMCdwTdTQnH
cpddMRdHTSNRtRztbG
mWvrQnQFhFNtsSNV
vrBnlLvWvlPCCnrrmBrnQQLmTMHwHHccMgggTNjdcDwjNgCw
hlRhqRnQQHcbBHGVVgRLVmrRgrLR
sCFMTMwtzFMzTwCsswWjCsdQJmJLGfrrgLfgPmPVVVmtLP
TMDjCFMTHShBQSDB
fcpssfGWpRDnvDRWvD
LMvQlPLtLQZbQjBqZBFnCRFZRFzR
jlQrvjlbjbLffpdpdrmGwr
hbRTjRRZthvSDvDn
LGrwPfrGfLjqvBsHzBrvstBv
mpCLCqqqLcwcwCLmLmwwdWgWgVVMTbbWbRdQVNjC
QLCqzhzQDqhHsCJjTcVdScccSVgs
NMPBBfwbmwmmGnfpTJJJcTrRjRJJddpr
mflmdfBBlnPBvBNGnwlGzhDqzHZzZtCLZqqltHtL
GGsFmSmFHHGZsqhSTQjlNQNzpptD
JfVJvvJfWMPPnVVJvhlNlltDldzpjpTzQn
LgLcwJffMMLcwPVvPMvsmRqTmbGGssgGssRRqG
ScnbPhwPHPTbwCGJBDtNZZPZDsttNB
FjfQlVVWrQgfQrrWfddnWfQlqJqJMNJBZJqsZtsJjJsvDjJq
lrVngVQpmmmrlnLGLLmTzchcwhHh
QZtDJqWZtWGmhJJjvVBP
crNMSpcdNNFcrdzlrsVGVnvhmnvHbjVjjrhV
NTszNMSpwTNFzcsTlsLRQLtWwZDDfQgZhggQ
mfmdLLLqsvZzjfPgPT
hppLhBNpHGrhHnQQhGMDhPbPbWzvZzbMzZFPbvbvgz
BNGGNLGcQpCcSstSRmct
mnjsJBjBRsmFsSRqqrGfrqqtrfrN
LZDHZZzdcdQzLbcgLwGtNVrlGrMVNfrllHrH
DPcZZzdQpZPzQQDpDdcpbcPgmBBBsnWfTBmnJmCsjjsPSTjJ
jwwHjCPvLVmhmRdJvr
gTBnbFGTTQMgnTbdbhHhrplhJdlV
DTScZTgSSnGTBFzjDwtLtDDHqwwL
RZWhWWRSgBRrdMRdCmtcdtLncHndqF
bssspTjbVDQGTVGTQsJpbvLtVmFLqqHgnLmCcFnmHC
DpfQJJQpDsGzzfDNhPBlPlMBNhghPZlW
VzJrJMBntJpMnBBJMDDGDQLLQwwDpQLGLG
WSFCWNWWWhQRzvNqLTRD
CbSlSlWHghChhWlcclgcWdHgfrmbmznnffMZMztrMbrJBBBJ
gtjBNTvDQNBPlBFlPFZPdP
mCmpfJCVmMzmfsHpCWdGPWCCWZGtSFtF
zJnhJnJzbbMMpnspmmfsJpLNgqtrjQvrTbTgLgtqgqLj
CLJnZZCJLJZJgZZZJMLSTgnRdFWpFdfFWBffpqDBfjFWQdRD
slNzNzzwwPQrfWmDmqBFWlDm
zwHhsVHwQcHJCgnngMZn
wLRLLddJLdZZZjHdRwgJsjqDVsDVSVGSscsVVmDq
tvMWfnhMvnvztzzVSVqqmcSSVsDGmW
TmhhpnnFlfMzMMRZRPTJRHwdPJZB
sLsQSLvcSrbQbFGlWlCD
BhgPBqBhPwmmpPlGhZMVCFFlbZGF
nCBBTPBHdHwmfCvTLStLJSctrJtt
vwNjwvBSSNndtdBJMJsLvZsJhZpPLM
TmCQDHGTVTLhPQhpZprq
CbCmmTzfVGfFGGCNbctwNPtcSnbjww
NWQQdHdTddhGrnJjqCRggvRmhzmm
wLLVHcFFFfwtFfJzqRvmRqzRVgVz
MlwFfflbLFfbwctDplwcwFMMNNWdWNTNSWDQQnsQNWWHsrQH
QlfbQrBjBQvfDBjhlpwpqbMzwWppGWqGwG
VJNcVCJgcntgRcsZWpPDPDqzPTqqnTpL
ZCRNRNmcJZCcNNVRmVdmHfjdrlfhSrvBDSfH
MzzPjGpjpGPPjdtHBfBNBQBrbtlclV
FqCnZcgcnFsWqmVHVHlgfBrbQVVb
STmCLFZWnTsWvdvSSdvPpGcP
lNjczlDNCSRMSmlR
VbhwhgwGQgwpvQpVDpSCbmfnCPfnMnmPmmBn
VhvGTdhwQwVVVsQQshjcDZdHdqzcDdJrjjzH
DhPffCSLCPCwfPPqqwqVjHFjzljppl
TBWBRWTMRBTTBTBdbQqztzQtWqzQFqbV
sgGTBGTGmNvrGfrz
hJgqGzqQmGQMQzgGmJGhJQSvZPfppjjPnZNTTTTpjWJvWp
lbwbRsRdbdmLdrllbbDcrHwwnjvjNfPWWZwWPjPjjZnTZZpf
dDDrdlDBHbDtVFSqmBShMMVF
ddvtMZJdJTtDvgtfZJfvtWZlHpGljLRcBcjplLwGRnnLGlGc
SNbFbrCNhQbrVQCQSCVzbLjBGRGRGwTBVwpnRGcHcw
bbhrTzrbrPrSQFrTTCmFQPCJmJqvJfZZWftZmZJqDvgfJv
vWLsTNNscttvNTLTLHRgcdqBnVSZVZVWVZqdSdJwwd
jDrFMhGPbGGFFPChDGpGBdngZMzVSSwZgJSqgMSV
bjjPQjphCPprhFrCCjFPDCTmcLgLtsTlmsNsQTtscQHt
PdhqLdNccGsrNLpScBnDznjnBnzppQwpHz
ftFtMbtfRMMWTvfRgRWbWMTjjzngzCzjzmDPjjwQDCDQmm
MRWVVfWfbFWWTbFWlvvRWPJGSLSLNJcPVsqJPcLSGr
fdRbPbHmnqvrvHDz
psTdcMgjjNpllVVgjJslMdpMhrttthznDttBWttBvWcnzBvh
gJjgVNFppjgCCVNsTTCsZbFwmmmmQGZSZLfwSZZd
csDFpcpJFbccqpFqpfggJJsljhvlTvQQtjwPTmjPPjRTtNvh
ZBGLddVCSVwNThhCQjPj
ZHLLLrSHGSBzWWzHWpgwcFbJsfcgJbsrgg
QJljRQLGJSNjMjQBLLJllFznzVCFpBnnzgwngpDCnD
mHWrTmWrdZHWvdrdWrdZttsFspFVcpzcwcggzpwzwVwDVp
vfzWvqTWWtPffWHqrWTZvTNSjRjQGGPPRbJbllQbMlJS
DFnFprBLpHcSlJHRBl
dbdMMCdsVWmMPlHSSVPVJfcf
sllvhgsdLThDnhQF
BSFTWCJWFJmBJdbcgDHgfDzHbncC
MjMPNjhlslPPLjPqPqVcDttzLBHcgDggDggDbB
MZhjMsBNNMhPrNjBrMhMPZWRmFmQFRRFFFQmWFQGFQ
NFgqSSrtlNbNffffffmFFZCf
WPvTBPPnBWmdJjCsPmVd
zBwhwwTRWwhvvzTvnhCTnCnSbbqlNStNbLltDRDHRHqtDR
NgggqJTHTJscdjggNVDVRcNHGLQWqpffZQGQGqpQWpWwQZfW
vvBPBhBFrzvnzSSrrSzPMtWZZcWGwmLnWQWpQlwGwpnl
rzbSCtrSttMctvvFMvrvPvgNJDRNHDsHNJsjTjsJJsVb
HbGVfpJbmbpHLBfHbdChRDDwDRhFlMlFVDFr
QzNQqcNgtqcNMjgqtntsgswRDDRQlFDSFQPDFRDwhCFR
ngscZtsqsznnnszqTnnqHfLWLWLWZmJpWMJGLBZb
cTNmqSbTBFhBQZjq
vswHWHWzHMMttvGGwgppttRfZFZjfBnQnfQZBhwQfhRB
lglsvMHHWHsWjHMtsvHvjWvTmJbCmcCcbCTcJlTmSmPSPT
JjSBbBLppbrvZGhhhvGwZNRtNMPCqCPqRgCFRNMgjP
lWlmDsdDnszRRwdCcNcdwd
TsDwwVTWsHTmTWVzQflQJbSGhZrZZQBhvBSrJZSr
JcrncrnrcZcGtJzfrrrzqbTWTlvW
SCRSDRPSLgRDCHdjjgmdDSHqQTzlmTNNVWbqfbvQzQlbfb
gpvpHHPPLdLRCSgjpLPtpZZMtnBMZJZBZBtMZs
lQSvJllvHBPPHPHWSPQQJtDtnhbwDDwwtwfhrrVw
MgLLdsMsgpRpTLLMgFrbFnfhNbbrhtwDwDDr
MqpTpqGRLpMgBzGPSvlhSBhW
NqpNNNPzhwzzshPwRPHWRmRFQWHDQPHD
VcbcnbjbbrrbbcnbZQDHmlRSVlvZWRFm
MttmjTtMrhqwhLhtdN
dMggwDwvMdqgqqtqwHnzVnmGmGtGRrFmsJrN
SlBClclffBPfZlssrGnJnZZzzznF
ljfTPplCpLcpBBPfTBfcCTbvbDMMFhqdvqWpMWHMDMpd
llTNZlhSvqMGlZMGhGgGlttrbVVwNjDbNFJbtjjDtN
fQWCBWQBBpBCsmzPmnmddQccwJtjdVbJDtDcrrjwjbFr
QzpQCRspPPPmzfppmmBBWLhgTZZTMRwSTgLlqvMqGG
HSfnNllsHThcchcJBjJhRL
FQQdzFCrFMbdFbrJBcqprcBrcBDqcB
mtmMFJJmnTfnsHvm
nddbfrBHdvbdBBhhhnWmtLsBGQCCtpmmMGPMQP
cwVVqVNggDgjZDFspptttQrsPgpttp
wDjczVZqSFDZVlSvrfhHlJHThh
CttLqSPLqLHhhCdGGTgdlZfclNlsfglbTg
nzFJpQJWVQjFmnmpjFWzVvBbMBTBNNTfTgZlTgFMNNZb
njDDWpVWQjQnzZzjJjnRRwCqPtLLrSqhSwCPCHqG
BFmNvfFNJRrdpMLLLVldWm
jPjGGwqsndHZqJqM
GtTSbjbtJjGQsQSSbPSGbzNgCRcCTCFhvfFgFFTBhfRc
rwBvGlDrBMSzMvGVSBwMSZgnJmmJqmcTTTmVCFJRcTgF
bbjpzLhHnFTLngLJ
zdHQdQQftWfNfNtsSvrsGBPGlswrlvDw
hdnMhghHZzFnZhDCCVTTTbtVmHmWbT
PQscSNcllJwzwbGmTmWVGm
sjprJpJjJNPpJBlpdFdgMzDDDhhvhd
SMwBWSBMPSfzqzPf
gJDlrFFQlgbFgvjDjTgrQQTGlhNNLdlqLGhNPqwPNPNfGf
jvwHQQjrjrJrppjvJpDFgDgHcsZZnnsVHsmMWCnsBsVVWZ
cblRJczlcBtBRCqNfGgHfpHCVHGp
WZWsLWmSPjMdWFGHTVNgLfvHqGDT
ZdmsFmZPmnZMsWWNsNjdmmmcQlrBQnBtQJtclBrtJwBzJz
wtMNCNwNqwtMMRnVcTlFtlcnFlsl
vrvrjzjZDDDwmwwVFT
jzrHjrrHjjLBPfQPjZBZzvpSMwCNRpRwSdRCNLqSShSR
BDgnhMDCDDpjDhBDJDfMSsLSZzCFTTLzTFLzTFZS
lrqrlmqbvtvWwVRtwlmrrqNvZlZSsLTTFTFZSPzZFzzTBFzz
HRRRbVmmwqhHHHhGJBcD
MvnmMvNjvvvmNnRcvzHgzMGtzhffHwHtwt
ZBBsFPPrTgCpSSBwHrLtwbHbLLtzLf
ZBZZssBdWRJgmgJdNn
TTLChzhDnjQLTDhTQJrzSbbJHsGrGrGFGb
BfvvpflfWVlVsFFvJHcFJFrJrt
ZwMBwwZPWMMpffflqlZMRnRNQLCNhPhDDNssnRQD"""


T02 = """A Y
B X
C Z"""

I02 = """C Y
C Z
B Z
A Z
A Z
A Y
A Z
C Y
C Z
A Y
A Y
B X
A Y
C Z
C Z
B X
C Z
A Z
B Y
C Z
A Y
C X
B Y
A Z
B Y
C Z
B Z
B Y
C Z
A Z
A Z
B Z
C Z
A X
B X
C Y
C Z
C Z
C Z
A Y
C Z
C Z
C Z
C X
A Z
A Z
C Y
A Z
C Z
C Z
C Z
A Z
B Y
C Z
A Z
B Z
A Z
A Y
B X
B X
C Z
C X
C Z
C Z
A Z
B Z
B X
B X
B Y
C X
C Y
A Y
C Z
A Y
C Z
A X
B X
B X
C X
B X
B X
A Y
B Y
C Y
A Z
C Y
B Y
B X
B X
B Z
B X
B Z
A Z
B Y
C Z
B Z
B Z
B Y
A Y
C Z
A Z
C Y
C Z
B Z
C Z
C Z
B Y
A Z
C Z
C Z
A Z
A Z
B X
C Y
A Y
C Z
B Y
C Z
A Y
C X
C X
B Y
C Z
C X
C Z
B Y
A Y
B Z
C Z
B Y
C Y
C Z
C Z
B Z
C Z
A Z
A Y
C Z
C Z
B Y
A Z
C Z
C Z
C Y
B Y
C Z
C Z
C Z
C Z
A X
B Y
C Z
B Y
C Z
B Y
C X
C Y
A X
C Z
B X
B X
A Z
A Z
A Z
B Y
C Z
B Z
A Z
B Y
C Y
C Z
C Z
C Z
C Y
C Z
B Y
C Z
C Z
B Z
A Y
B Z
C Z
C Y
A Z
C X
B Z
C Y
B Y
C Z
C Z
A Z
C Y
C Y
C Y
B Y
C Z
C X
B Y
C Z
C Y
B Z
A Y
C Z
A Y
B Z
A Y
A Y
B Z
A Z
C Z
C Z
B X
C Z
C Z
B X
B Y
C Z
C X
A X
C Z
C Z
C Z
B X
B X
A Z
C Z
C X
A Z
C Z
C Z
A Z
B Z
C Z
B Y
C Z
A Y
B Z
C Z
C Z
C Z
C X
A X
A Y
B Y
C Z
B Y
C X
A Y
C Z
C Z
B Y
B Z
C Z
B Y
B Y
B Y
A Y
C Z
B Z
A X
B Y
C Z
C Z
C X
A Y
C Z
A X
B Y
A X
A Z
B X
B X
C Z
C Z
A X
C Z
A Y
B Y
B Z
C X
C Y
B X
C Z
C Y
B Y
C Z
C X
B Z
C Z
C Z
C X
C Y
C Z
A Y
C Z
C Z
C Z
C Z
C Z
C Y
B Y
C Z
A X
A Z
C Y
B Z
B X
A Z
C Z
C Y
C Z
C X
A Y
C Z
A Z
B Y
B Z
C Z
B Z
A Y
C Z
B Y
C Z
C Y
C Z
C X
A Y
A Y
C Y
C Z
C Z
B Y
A Z
C Z
C Y
A Y
A Z
A Z
C X
C Z
B X
C Y
C Z
C Z
B Y
C Z
B X
C Z
B Z
B Y
C X
C X
A X
B Y
A Z
C X
B X
A Z
C Z
C Z
A X
A Y
B X
C Z
A X
C Z
B Y
C Z
A Y
B Y
C Z
B Z
B Y
A Z
C Z
A X
B Z
C Y
B Z
B Y
A Z
A Y
A Z
A X
C X
A X
C Y
C Z
A Y
C Y
B X
A X
A Y
C Y
B Y
C Z
C Z
B Z
C Z
C Z
C Z
C Z
C Z
C Z
C Z
B Y
C Z
A Y
B Y
C Y
C X
C Z
B Z
B Y
C Y
C Z
A Z
C Y
B Z
C Z
A Z
C X
B Y
B Y
B Y
C Z
B Y
A Y
C Z
C Z
A Z
A Z
C Z
B Z
B Y
C Z
B Y
B Z
C Z
A X
A X
C X
C Y
A Y
C Z
A Y
A Z
C Z
C Z
C Z
B Y
A Z
B Z
C X
B X
C X
B Y
C Z
A Z
C Z
A X
B Z
B Z
B Y
A Y
C Z
B X
C Z
B Z
C X
A X
C Z
C Z
B Z
B Y
C Z
C Z
A Z
C Y
C Z
B Y
A Y
B Y
A Y
C Z
C Y
B Z
A Y
C Z
B X
B X
B X
C Y
C Z
A Y
C Z
C Z
C Z
A Y
C Z
B X
A Z
C Z
C Z
A Y
C Z
C Z
B X
C Z
B Y
A Z
C X
C Y
C Y
C Z
C Y
A Y
B Z
C Z
C Z
C Z
B Y
C Z
C Z
A Y
A X
A Y
C Y
C Z
C Z
A X
B Z
C Z
C Z
B Z
B Y
C Z
A X
C X
A Z
B Z
C Z
A X
C X
C Z
B Y
A X
A X
C Z
C Z
B X
C Z
B Z
B Y
A X
C Y
C Z
C X
A Y
B Y
C Z
C Z
C Z
C Z
B Z
A Y
C Z
C Z
B Z
C Y
B Z
B X
B Y
A Z
C Z
A Z
B Y
C Y
C Z
C Z
C Z
B Z
C Z
C X
C Z
B X
C Y
B Y
C Z
C Z
C Z
C Z
B Y
B Y
C Z
B Y
C X
B Z
A X
C X
C Z
B X
C Z
C X
C Z
A X
A Z
B X
C Z
C Z
B Y
C Z
A Y
C Z
C Z
C Y
C Z
A Z
A X
C X
B Y
A Y
B Y
A X
C Z
B Y
B Y
C Z
C Z
B Y
B X
A Y
C Z
B Y
C Y
C Z
C Z
C X
B Y
A Z
C Z
A Z
A X
C X
A Z
C Z
C Z
A X
B Z
C Z
B Y
A Z
A Y
A X
A Y
A X
C Z
A X
B Y
A Y
B Z
C Y
C Z
B Z
C X
A Y
A Y
C Z
C Y
C Z
B Y
B Y
B Y
B X
C Z
C X
B Y
C Z
C Z
B Y
C Z
C Z
B Y
C Z
C Y
C Z
C Y
C Z
C Y
A Y
A Y
C Y
C Y
C Y
C Y
C Z
C X
B Z
B Z
C X
C Z
B Y
B Y
A Z
C Y
C Z
C Z
C X
C Z
C Z
A Z
B Y
C Z
A Y
C Z
C Z
C Z
A Z
C X
C Y
B Y
A Z
B Z
C Z
B Y
C Z
B Z
C X
A X
C Y
A Y
B Z
B Y
A X
C Z
B Z
C Z
C Z
C X
B Z
C X
A Z
B Z
C Z
C Z
C Z
B Y
A X
C Z
C Y
C Y
C Z
A Z
C Z
C Z
A X
C Y
B Y
A Y
A Z
A Z
B Z
C Z
A Z
B Y
B Y
A Y
A Z
A Z
C Z
C Z
C Z
A X
C Z
B Z
B X
C Y
A Z
B Y
C Z
B Y
A X
C Z
A Z
C Z
B Z
C Y
C Z
B Y
A Z
B Z
A Y
B X
C Z
B Y
C Z
C Z
C X
C Y
C Z
B X
C X
A Y
A Y
C Z
C Y
B Y
C Y
C Y
C Z
A Y
A Z
B Y
C Z
C Z
A X
C Z
C Y
C Z
B X
C Y
A Z
A Y
A Z
C X
C Z
C Z
C Z
B Z
C Y
B Z
C Z
B Y
C Z
B Y
A Y
B X
C Z
A Y
C Z
A Y
A Z
A Z
B Z
A Y
C Z
A X
B Y
C Z
B Z
C Z
A Y
A Y
B Z
B X
B X
C Y
C Z
C Z
C Y
A X
B Z
C X
B Y
C X
B X
C X
C X
C Z
A Y
C Y
C Z
B Z
A Z
A Z
C Z
A Z
C Z
A Z
A X
B Y
A X
A Y
C X
B Y
C Z
A X
B X
C Z
C Z
C X
B X
A Z
B X
C Z
B Y
C Z
C X
C Z
C X
C Z
B Z
B Y
C Z
B X
C X
C Z
C Y
A Z
B Z
A X
B X
B X
C Z
B Z
C X
A Y
C Z
C Z
B Y
C X
C Z
A X
B Y
C Z
C Z
C Z
C Z
C Z
A X
A Z
C X
A Z
C Z
A Z
C Z
B Y
B Z
A X
C X
C Z
B Z
A Z
C Z
C Y
C Z
C Z
C X
A Y
B Y
C Z
A Y
C Z
B Z
C X
B Z
B Z
B X
B Z
C Y
C Z
C Y
B Y
C Y
C Z
C X
C X
A Z
B Y
C Z
A Y
B X
C Y
A Y
A Z
B Y
B Y
A Y
B Y
B Z
A X
C Z
B Y
A X
C Z
C Z
C X
B Y
A Z
A X
B Y
A Z
C Z
B Z
B Z
B Y
B Y
A Z
A Z
A Y
C Z
C Z
A Z
C Z
C Z
C Z
A X
C Z
A Y
C Y
A Z
C Z
B Y
C X
B Y
C Z
C Z
C Z
A Z
B Z
B X
C Z
C Z
A Y
B Z
B X
C Z
C Y
A Y
C Y
C Y
C Z
C Y
C X
C Y
B Z
B Y
C Z
A Z
A Y
C Z
C Z
B Y
B Y
A Z
A Z
A X
C Z
C Z
A Y
B Y
C X
C Z
C Z
A Z
C Z
B X
B Y
A Y
C Z
A X
A Y
C Z
B X
C X
B Z
C Y
C X
B Y
B Y
C Z
C Z
C X
C Z
A Y
A Z
C Y
C Z
A Z
C Z
C Y
A X
C X
C Z
B X
C Z
B X
C Z
C Z
C Z
B X
B Y
B Y
B Y
C X
B Y
C Z
C Y
C Z
C Z
B X
C Y
B Z
C Z
C Y
C X
C Z
A X
A Z
C Z
C Y
C X
C Z
B Y
C X
C Y
C Z
C X
A Z
B Y
B X
C X
C Y
B Z
C Z
C Y
B Z
C X
A Z
A Y
C Z
C Z
C X
B Y
C Y
C Z
A Z
B Z
B Y
B Y
B Z
C Z
A X
B Y
A Z
A Y
C Z
C Z
B Y
C Y
C Z
B Z
A Z
B Z
C Z
C Z
B Y
B X
C Z
C Y
C Z
A Y
C Z
A X
C X
B Y
B X
C X
C Z
C X
B Z
C Z
A Z
B Z
C Z
A X
C Z
C Z
A Y
B Y
B Z
B X
B Z
C X
B Y
C Z
C Z
C Z
A Z
C Z
C X
C X
B Y
C X
C X
C Z
C Z
A Z
C Y
C Z
C Z
B Z
C Z
A Y
B Y
C Z
C Z
B Y
B Y
C X
C Z
B X
A Y
B Z
A Y
A Y
A Y
C Y
C Y
C Z
B X
B Z
C Z
C X
C X
B Z
A Z
A X
B Y
C Z
B Z
A Z
B X
C Z
A Y
C Z
A Z
A Z
C Z
C X
C Z
C Y
A X
B Y
C Z
C Z
C Z
C Z
C Z
A Y
C X
C Z
A Y
B X
C Z
A Y
C Z
C Z
C Y
B Z
B X
C Z
A X
B Y
C Z
C Z
A X
A Y
C Z
C Y
B Y
C Z
C Z
A Y
A Y
A Y
A Y
C Z
A X
A Z
B Y
B Z
A Z
C Y
C Z
C Z
C Z
A Z
C Z
A Z
C Z
C Z
A Z
C Z
C Z
A Z
B X
C Z
A Y
B Y
C Z
A X
C Z
A Y
C Z
C Z
C Y
C Z
A X
B Y
C Z
A Z
C Z
A Z
A Z
B Y
C X
B Y
C X
C X
C Z
A Y
B Z
A Y
C Z
C Z
B Z
A Y
C Z
B Y
C Z
A X
C Z
C Z
C Z
B Z
A X
B Y
C Z
A X
C Z
C X
B Y
C Z
A Y
C Y
B Y
A Y
C Z
A X
B Y
A Y
A Z
C Z
C Z
C X
A Z
C Z
C Z
B Y
B X
A Z
C Z
B X
C Z
C Y
C Z
C Z
C Z
C Y
A Y
C Z
C Y
C Z
C Z
B Y
B Y
B X
C Y
B Z
C Z
B Y
C Z
C Z
C Z
A Z
A Y
C Y
C Z
C Z
A Z
C Z
C Z
C Z
B Y
B X
B Y
A Y
C Z
B Z
C Z
B Y
B Z
A Y
C Z
C Z
C Y
A Y
C Z
C Z
B Y
A Z
A Y
C Z
C Z
B Y
C Z
B Y
B Z
C X
C Y
C Z
A Y
C Z
A Z
A X
B X
C Z
C Y
C Z
C X
B X
B Y
B Y
C Z
C Z
C Z
A X
B Z
C Z
A Z
A Z
C Z
B Y
B X
B Y
C Z
B Z
C Z
B X
B Z
C Z
B X
A X
C Z
C X
B Z
C Y
C X
C Z
C X
A X
A X
C Z
C Z
C Z
B X
B X
C Z
C Z
C X
C X
C Z
A Y
B Y
B Y
B Y
C Z
C Y
C Z
C Z
C Z
B Y
C Y
C Z
B X
C Z
A X
C Y
A Y
C X
A Y
A Z
C Z
B Y
B Y
A Z
C Y
B Z
B Z
A X
B Y
C Z
B X
A Z
A Z
C Z
B Z
A Z
C X
B Z
C Z
C Z
C Z
C Z
B X
B Y
C Z
C Z
C X
C Y
A Z
B X
B Y
B Z
C Z
B Z
C Z
C Z
C Z
C Z
A Y
C X
C Z
A Y
C Z
C Z
B Z
C Z
A Z
C Z
A Y
C X
C Z
A X
C X
C Z
C Z
B Y
C Z
A Z
C X
C Z
B Y
A Y
B Y
C Z
B X
A X
C Z
B Y
C Z
B Y
A Z
A Z
C Z
A Z
B Y
C Z
C Y
B X
C Z
A Z
B Z
C Z
C Y
C Z
B Z
A X
A X
A Z
C Z
C Z
C Y
C X
C X
A X
C X
B X
C X
A Y
C Y
C Z
C Z
C Z
C Z
C X
A Y
C Y
A Y
B X
C Y
C Z
A X
A Z
C Z
C Z
B Y
C Z
B Z
C Z
C Z
A Y
A Y
C Z
C Z
A Z
C Z
C Z
B X
C Y
C Z
C Z
C Z
C Z
A X
B Y
B X
B Z
C Z
A Z
A Z
B Z
A Z
B X
C Z
B Z
C Z
A Z
C Z
C Z
A Y
B Y
C Y
B X
A Z
C X
C Z
C X
B Y
B Z
C Z
C Z
C Z
C Y
C Z
A X
A X
A Y
C X
C X
A Y
B Y
C X
C Z
C Z
B X
B Z
B X
C X
B X
A Y
C Z
A Z
C Z
C Z
C Z
C Z
C X
A Z
B Y
C Z
C X
A Y
A Y
C Z
C Z
B Z
B X
C Z
A Z
B Y
C Z
C Z
B Y
A Y
C Z
B Z
B Z
A Z
C X
C Z
B Z
C Z
C Z
B Y
C X
B Y
A Z
C Z
A X
C Z
B Y
C Z
A Z
B Z
C Z
A Z
A Y
C Y
B X
C Z
A Y
C Y
A X
A Z
A Y
C X
C Z
C Z
B Z
A Z
C Z
C Z
C Y
C X
C Y
B Y
C Z
B Y
C Y
C Y
C Y
A X
C Z
C Z
B X
B Y
C Z
A Y
C Z
A Y
B Z
C Z
C Z
C Z
A Y
A X
B Z
B Y
A Y
A Y
B Y
B Z
C X
A Y
B Y
C X
C Z
C Z
B Y
C Z
C X
C Z
C X
C Z
A Y
A Y
B Y
C Z
A Z
C Y
C Z
A X
C Y
C Y
C Y
A Z
C X
C Z
C Z
A Z
C Z
B Y
C Y
C Z
C Z
C Z
B Z
C X
C Z
C Z
C X
C Z
C Z
C X
C Z
C X
B Z
B X
A X
C Z
A Y
C Z
B X
C Y
A X
C X
B Z
C Z
A Y
A X
C X
B Z
B Z
C X
A Y
C Y
A Y
C Z
C Y
A X
C Z
A Y
A Z
C Z
B Y
C X
A Y
A Y
C Y
B Y
A Z
B Y
C X
A Y
B Z
B Z
C Z
C Y
C Z
B Y
C X
C Z
C Z
A Y
C Z
C X
A Y
C Z
C Z
B X
C Z
A X
C Z
A Y
C Y
A Y
B X
C Y
C Y
A Y
C Z
A Z
C Z
C Y
C Z
A Z
A Z
C Z
C Z
C Z
C Z
C Z
A Y
A Z
B Y
C Z
A Y
C Y
C Z
A Y
C X
C Z
A Z
C Z
C Y
C X
C Z
C Y
A X
B Y
C Z
A Y
A Z
C X
C X
C Z
A Z
C Z
C Z
C Z
C Z
A X
C Z
C Z
C X
C Z
A Y
C Z
C Z
B X
B Y
C Y
B Z
C Y
C Z
B Y
A Y
A Y
B Y
A Z
B Z
B Y
A X
C Z
B X
A Y
C X
C Z
C X
C Z
C Z
C X
A Z
B Y
A X
C Z
C Z
B Z
C X
C X
B Z
A Y
A Y
A Y
A Z
C Y
C Z
A X
B Y
C Z
B Y
B Y
C Y
C Z
C Y
B Y
C Z
B Z
C X
C X
A X
C Z
C Z
B Z
A Y
A Z
B X
B Z
B Y
C Z
A Z
C X
A Z
B Y
C Z
B Y
A Y
C Z
A Y
B Z
C Z
A Z
B Z
B Y
B Y
A X
B Y
B Y
C Z
B Y
C Z
B Z
A Z
A Y
C Z
B Y
C Z
C Z
C X
C X
C Y
B Y
C Y
A Z
C Z
A Z
C Z
B Z
C Y
C Z
A X
B X
A Z
A Y
A Y
C Z
C Z
C Z
C Y
C Z
C Z
A Z
A X
B X
A Z
C Y
C Z
B Y
A Y
A Y
B X
B X
C Z
C Z
C Z
C X
C Z
C Y
C Z
A Y
C Z
C Z
C Y
A Z
B Y
A Y
B Y
B Y
A Y
A Y
B Z
C Z
C X
B Y
C Z
C Z
C X
A Z
B Y
A Z
C Z
C Z
B Y
C X
C Z
C Y
A Y
C Z
A Y
B Y
A Y
C X
C Y
C Y
B Y
B Z
A Z
C Z
C Y
B Z
B Y
A Y
A Z
A Y
A Y
B X
C Z
A X
B Y
B Y
C Z
B Y
B Y
B Z
C Z
A Y
C X
A X
A Y
C X
A Y
A Z
C Z
B Y
B Y
B Y
C Y
A Y
B Z
C Z
C Z
B Z
C Z
B X
C Y
B Y
A Z
C X
A Z
C Z
B X
C Z
C Z
B Z
C Z
A Z
A Z
B Y
C Z
A Z
C Y
B Y
B Z
C Z
C X
C Z
A Z
C Z
C Y
C X
A Y
B Y
B X
C X
C Z
A Z
C X
B Z
C Z
A Y
C Y
C Z
A Z
C Z
A Z
C Y
C X
C Y
B Z
B Y
A Z
A Y
B X
A Z
C X
C Y
C X
C Z
C X
A X
C Z
B Y
C Z
A Y
B Z
C X
B Y
C Z
A Z
C Z
C Z
C Y
A Y
A Z
A Y
C X
B Z
A Z
C Z
C Z
C Z
A X
C Z
A Z
A Y
C X
B X
C Z
C Z
A X
A Y
C Z
C X
C Z
A Z
C Y
C Z
B Z
C Y
C X
A Y
A X
A Z
C Z
C Z
C Z
C Z
A Y
C Z
A Z
A Y
C Z
B Z
B Y
C X
C Z
C X
C Z
B X
A Y
C Z
B Z
A Z
A Z
B Z
B Z
C Z
C Z
B Y
C Z
A Y
C X
A X
A X
C X
C X
B Y
B X
A Y
C Z
B X
B Y
A Z
B Z
A Z
A Z
C X
C Z
A X
A Y
C X
C Y
C Y
C X
A Z
C Z
C X
C X
A Y
A X
C Z
C Z
B Y
B Z
C X
C X
C Z
B Z
B Z
B Z
B Z
B Y
B X
C Z
C Z
C Z
C X
C Z
C Z
B Y
C Z
C X
B Y
C Z
C Y
B Z
C Y
C Z
C Z
C Z
C Z
C Z
C Z
C Z
A X
A Y
C Y
C Z
A Y
B X
C Z
B Y
C Y
C Z
C Z
C Z
C Y
C Z
A Z
B Y
A Z
C Z
B Z
C X
C X
A Z
C Z
C X
C Z
B Z
C Z
C Y
B X
C Z
A Z
C X
B Y
B Y
C Z
C Z
C Z
B Y
C Z
B Y
A Y
B Z
B Z
B Y
C Z
B Z
A X
C Z
C Z
C Z
B Y
B Y
C Z
C Y
C Z
B Y
C Z
B X
B Z
C X
B Y
C Y
B Y
C Z
A Y
B Z
C X
B Y
A Z
C Z
C X
A Z
B Z
A Y
C Z
C X
B Y
C Z
C Z
B Y
B Z
C X
C X
C Z
C Z
C X
B Z
A Y
C Z
C X
A Z
C Z
C Z
C Z
C Y
B Z
A X
B Z
B Z
C Z
C Z
B Z
C Z
B Z
A X
B Z
B Y
B Z
B Z
B Y
C X
A Y
B Y
B X
B X
A X
C Z
C Y
C Y
C Y
C Y
B Y
A X
C Y
A X
C Z
B Z
C Z
C Y
B Y
A Z
C Y
A Z
B Y
B X
C Z
A X
A Z
C Z
C Z
A X
C Z
C X
A Z
C Y
B Z
C Y
B Z
A Y
A Z
C Z
A Y
C Z
C Z
A X
C Z
C Z
C Z
B Y
C X
C Y
C Z
B X
A Z
C Z
C X
B Y
A Y
B Y
C Z
C Z
C Z
A Y
A X
C Z
C Z
C Z
C Z
B Y
A Z
C Z
A X
A Y
B Z"""


I01 = """6750
6538
5292
4635
6855
4137
3840
4691
1633
6008
2447
1448
4061

4261
6778
1531
2914
2102
4098
2451
1219
6488
3941
2158

9058
3441
9318
1976
6115
9451
10090
5850

4921
3202
3193
4170
1079
1757
5828
1757
2849
1586
5661
2607
2047
5385

7272
20573
13163

10682
5428
3751
9040
1556
1778
8657
9901

4889
6751
5090

12074
19421
3745
10856

15209
13798
15398
15838
4569

2572
4413
3683
12331
6840

8924
7301
1912
7526
4090
6867
3223
1083
2215

1728
12054
13145
4353
12434
3579

24525
23626

4395
11502
14008
10243
1463

4565
5888
3039
5295
1034
3440
2668
7161
5646

6367
8398
5485
8919
6618
2850
6855
5865

6788
7063
6797
3168
7176
1193
1846
1873
5291
1712
2802

3991
4976
2611
3576
3919
3522
3877
2822
3726
5944
4658
6066
4618

6675
12989
2094
2264
13116
11464

6322
2429
4887

6282
11135
3600
3977
6564
1687
3041

48760

3670
16233
6513
15868
12383

10008
9791
3299
4085
5778
10435
7349

5393
1162
4273
3179
3259
1892
8713
7147
8921

7793
5170
3658
6938
5040
6680
1682
1411
4675
2435

19306
33764

5046
5534
5683
4581
5515
4866
1520
1469
3747
3969
4070
3201
4376
3453
5877

13009
23239
20343

11867
14880

2716
1627
2914
2171
3475
4131
2816
2237
1538
3209
4589
4920
2222
3873
5492

4059
3824
2008
1651
5992
5777
6401
5129
1919
2921
1897
5831
5123

5504
6492
3528
5206
5682
5635
6720
3617
1625
5082
1140

3202
4433
8085
6145
1788
5332
5737
2561
1502
5880

19360
15037
9234
1425

6289
2249
6150
5228
4380
4528
4320
1979
3716
2908
4012
7181

2027
5508
3895
8700

6981
5136
2006
2955
7964
8445
1394
4874
5100
6794

5929
7003
3703
7981
7682
4386
8325
7086

6000
8868
12326
3747
2003
6186

5770
5634
1784
9951
8578
13924

2935
24789
21603

8239
10654
12558
5657
14398

1306
7030
4126
3092
7155
3949
5040
5951
6263
5587
1561
6046

34556

5474
3194
1962
7296
8065
2107
7355
4748
4752
7983
7051

19407

7778
1987
7642
1268
5019
3694
2161
6285
1600
5145

8850
14656
2486
10361
2067

6012
4885
4612
1807
7657
6930
1790
6035
5725

6047
2033
6994
2344
5801
1207
5190
3118
3153
1869
6065
3754

4721
1639
2235
3834
4052
4763
1649
2470
4294
2716
5381
6453

2751
7038
1463
2756
2256
3708
1921
4682

7439
1232
3630
7889
2564
7272
5764
5655
7827
6832

7254
6038
3702
6855
4473
1957
1597
7394
2850
3529
6832
6855

3486
3877
6424
5280
5080
4055
1830
1737
4379
1980
5148
5972

10069
4487
14451
7309
8744

8751
4856
4594
3986
4709
4361
4205
1401
5873
5059

2548
6623
3418
6848
2165
6466
4259
2792
1663
5537
1343

15745
5468
8877
18074

6055
14504
12291
8253
5828

25661

7301
9470
9040
1483
2974
7741
8556
7457

1465
4805
2485
2431
6956
2712
7434
1079
2500
1670

2537
5815
5604
2453
3919
2488
2866
5500
4009
1219
6109
3118
4932
4514
1732

2589
6885
7099
8389
4576
4904
3223
4645
1076
1453

6236
9825
7747
4682

2958
4351
3057
2951
6734
1766
4026
2957
8567
7559

5472
5402
4469
4762
3408
5000
3805
3535
4942
3180
3477
1599
5597
1030

2651
4374
6259
3969
6953
5116
3336
4486
5499
3027
1109
6419
4552

2876
6394
5562
5153
2408
6503
1909
3958
2908
1817
5627

1662
7210
5719
4019
3414
9539
7163
5050
7793

1003
4450
5580
2140
3531
4093
4189
2347
4990
2177
5204
3731
1673
2567
2206

5589
3205
6409
7776
4005
1250
7219
6491

22563
24898
3671

1628
4812
6709
1969
1128
2526
5606
3184
3590
5067
7267

6073
4594
2346
1819
2383
5765
1530
3850
2453
2015
4712
5945
3990

5700
2022
4971
2569
2226
5599
2661
3097
4126
6015
1328
4067
6088
4550
3083

5833
2291
1397
6032
2359
4478
2480
2217
3012
2212
2551
3894
1144
2494
5242

10165
5568
5967
10286
5835
6187
6443

2460
2361
5067
2008
6812
6381
4005
6778
5942
4981
3141
5420
1137

8977
11981
4701
4392
7377

6702
1053
5682
2280
4750
5451
5425
5739
3052
1884
5115
3447
1355

15207

23476
24176

4357
6421
4897
6452
5591
3745
4225
3902
4382
6200
3521
1158
6742

7327
4654
4242
4063
2551
2845
5636
1645
6300
3800
3324
5186

2671
4674
5368
10396
7250
8983
10080

5132
9545
4031
2698
2741
3072
1542
1419
3958

1736
6254
7696
5803
4724
2811
7429
3568
8717
1015

3616
3437
1285
2201
3597
2818
1859
4828
2644
4907
5468
3424
6160
4025

7153
1979
3198
2506
1838
5274
2904
5671
1300
3064
2447
2756

8583
8107
14984
10437
9655

4628
1643
2052
4833
3918
6200
6348
1551
7568
7647
5621

4470
4926
1971
6085
2990
4674
1927
2155
6489
6878
3445
6810
1998

3804
5867
3159
3385
3765
3175
1265
3572
3718
4562
5117
3938
1977
3606
2281

3352
15576
7744
3992
1217

4426
12388
12828
5208
2784
12502

1762
4751
3595
4360
1064
4224
3268
5411
3390
2589
1513
3075
5845
1738
4082

13785
6062
7074
3574
11195
8335

8519
22618
10403

12822
12248
9591
13299
10619

7025
6943
5930
3343
3430
7089
6784
7879
9007

3920
7809
7363
6740
1326
2578
2518
7446
7417

3603
10150
8180
5872
7075

3118
10518
8824
2675
8445
9206
3724
4329

9885
10933
1372
3905
12731
6330

3884
3392
3455
3560
3093
2778
4630
4742
4959
2883
4820

5796
1645
14987
6986
15074

3281
1335
3725
5414
6439
1619
4557
4583
1522
1009
1835
2371
5955
2289

43920

2477
1999
4809
5084
3606
4850
5977
3763
1108
4160
2322
6356
5461

5000
3267
5171
7136
9932
1281
11676

3689
3319
3508
7243
7766
1685
3809
4093
2539
7137
3167

8322
11802
6949
15451

2806
6035
4881
1152
5328
4693
5930
1610
5849
4853
2049
1263
5736
5234
1525

1616
2945
23855

2062
8376
10728
9744
2777
4101
5612
5133

13599
14149
8082
12680

5143
6807
6474
7390
2308
3201
7265
4492
6646
1664
6422
7428

15425
4319
15222
7365

5186
4698
4556
6355
1879
5436
3440
4223
6103
1027

6897
5842
1932
3726
3608
3011
6812
2384
2285
1388
3211
6414

37328
20417

1127
2001
6357
1978
5528
4675
7215
1097

4258
3189
4748
3973
3492
4496
1123
6485
4969
3947
4079
2657
4920
1940

5593
3590
7069
6526
3404
8501
5189
9022
3399

4146
4305
3820
2260
3144
1288
3812
2815
1553
2301
5655
1298
2531
4350

1200
2871
7637
2279
7747
5740
2103
2373
2471
3658

3108
4947
2258
1073
9635
7326
7712
9458
1008

6679
16292
11474
10212
11418

4018
6049
1942
5851
3480
1108
1769
4176
1911
2497
2904
5108
4018
4839

9257
5081
3816
1487
8582
5317
8506
2749
7187

10033
12757
9353
6820
2459
12843

17725
16704
1919
14770

11941
8538
2984
6435
1242
2782
11283

4787
1630
2456
4425
5434
1684
2066
4657
3419
6536
1132
4288
4319

7364
6179
5832
4077
4003
8781
6022
5672
5784

4582
8233
9135
8448
7295
3450
5941
5678
8945

3673
11877
8079
5830
13123
8819

2464
4267
1275
4036
3019
7571
6808
2291
4975
4857
7037

4663
5328
2021
1593
5605
2423
6565
1077
3076
2521

2712
10855
10943
6416
2654
11960
9471

5053
2896
2868
2508
3712
2086
1028
5985
1312
2486
3561
3789
1747
4241

1244
3146
3768
5090
4881
1565
4007
5283
8189
2266

11599
6170
7253

1596
2215
6018
5848
3357
5971
1395
5412
4413
2907
3398
6191
1502

5562
1955
3203
4835
5426
5409
4020
3987
4922
1332
1355
2244
4977
1559
5507

8879
3197
11212
4477
8238
1800
3684

15121
7384
14501
12667
9620

1767
4997
6039
1889
3620
2880
4305
1292
6176
3125
5876
6515

3829
5030
2670
6937
7747
1587
3837
3222
3607
3325
5323

27071
32218

5593
3592
2311

2628
2562
1322
5307
4337
4761
4451
2981
4279
4828
2008
3109
3016
1927
5636

1218
1205
2913
1892
4268
5360
5622
4694
1721
3315
1886
1798
2418
2954
2479

2125
7128
2112
5163
6536
7023
7026
2662
7967
3376
4663

11505
9288

4193
5100
1922
3258
1133
3906
6049
1211
3743
3952
1546
2818
1795
3697

13660
13843

10925
4229
10107
10541
3950
6892
7594

3726
4753
3245
2459
5362
4514
1635
1875
2196
3379
4391
3278
3942
5488

6838
7367
5133
4229
8382
5748
4408
1149
2712

5790
7280
1537
6596
4167
7905
4829
1875
5374
3432

18774
12470
2680

1481
4005
8336
9616
9360
9601
8805
1857
7736

2372
16287
11904
4931

6023
3192
2630
2712
5403
7077
3310
2386
3072
6322
6850

20799
2284
9823

4705
5625
1830
1374
1770
1125
2395
5050
1311
4818
3497
2829
6509
2301

3318
10761
10053
11006
4726

3055
8238
8388
10499
16116

4145
1135
6326
3248
3734
2661
4180
1240
6488
5394
4859
6312
2128
2689

31894
27468

7845
2959
2719
2650
3442
2128
2702
3306
2590
2887
2655

4595
6230
11249
2158
3494
7055
5763

4473
6469
6779
3344
5325
7869
1481
6709
5553
8648

5459
12649
10227
19725

4389
4566
2761
5106
4064
4118
1923
3564
2935
1084
5351
6416
6170
1642

63220

3978
7803
9714
6796
5812
7324

6757
3868
18800
1352

2034
1060
4800
5866
2625
3222
2281
2911
3698
2632
2504
2993
5809
1805
4196

5613
2702
1140
2398
2584
3877
2934
1496
4237
4305
2103
5801
2201
1100
4737

4454
24314
4677

6100
1297
4199
6261
5518
1942
1875
3137
5217
2370
4628
4854
6484

2790
5473
6457
4180
1133
6134
3019
3479
5472
3336
5414
4040
6459
5327

24399
21223
12711

7774
10176
10388
2864
2575
8018
3420
6435

9838
14038
11004
7468
1242

6915
5378
5586
7725
5101
1569
3073
4346
1253

2633
4195
6287
4192
8015
9520
6870
9894

7014
2252
3296
2288
5613
2615
1903
7348
5555
1460
2770
4373

8013
8256
3029
8246
2830
6447
8885
9633
9081

6296
6768
4904
3649
2623
1577
7764
1959
6686
7329
3986

13311
5670
6954
7407
12264

1832
6503
7209
7871
5590
1952
4496
4698
3591
5818
1756

3584
6327
6639
7100
3409
1023
4365
5607
6419
7887
5419

23730
7283
7943

5497
4917
1514
1399
6628
3835
5718
2071
6030
2238
2187
4433
6289

6897
2972
3174
2134
6927
3165
2072
6086
5119
4199
3256
3257
6808

23297
8152
1449

4807
4900
7997
13646
10133

60078

1764
4796
7749
1069
5594
2802
3850
1878
3212

8476
1982
3141
2647
10087
1170
5975
3683

4310
5495
1374
1462
1852
5149
5976
3397
1280
3545
3021
2969
5261
3474
4938

14240
36288

3977
6268
1396
2707
6344
5279
3026
1237
4671
1545
3049
1235
3322
1226

7877
10542
10800
11760
7013
11468
10914

1883
6346
8428
2097
12309
1747

6919
4606
4133
6376
6127
3131
5530
1041
6161
4321
6201
7080

9683
19478
7509
7186

15598
23816
9973

1740
5245
7924
2086
3354
5989
1788
7710
5233
4330
6087

5063
3096
7629
6728
5995
6789
5294
8760
5424
6981

3548
2507
2274
1434
4003
3988
2009
5501
3583
4751
3335
1793
3450
4458
5667

9998
12172
10851
13296
12712
5534

3552
2877
3870
4505
5234
4130
5405
5460
5840
4405
1839
3764
2418
4602

11031
11643
9905
8111
10798
12365

38360

3952
19297
16495
16016

9608
2121
5670
3593
8530
2474
9402
1305

2152
6691
5395
7779
5215
6785
1282
7910
3591
1320

6767
5293
5630
5654
9330
2438
5614
8125
5418

8336
6170
1224
3646
4163
8049
9345
6148

2815
2907
4811
1271
2410
3790
4602
3684
2711
2756
3535
1877
3902

3492
4651
2158
6059
2071
8046
3863
4920
2427
5702

4846
14976
16005
17415

4171
3820
1051
3655
1972
1510
6213
2666
5479
3776
2680
4844
3361

68996

1046
3913
6469
3566
5521
2615
5167
1535
1842
4028
2505
6146
5646

30144
31365

2582
5925
1480
3378
7508
6960
5834
4230
4839
5744
5675

32883

13628
14364
15147

3863
1397
8149
3836
6434
1847
6078
5762
4318
2934

4426
1851
4825
5352
5998
4412
2592
5786
3582
3180
2682
3928
2112

6674
1167
4238
4532
4175
2308
4963
5452
7397
7163
4460"""