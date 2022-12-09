from dataclasses import dataclass
from itertools import chain


@dataclass(slots=True)
class P:
    x: int
    y: int

    def __repr__(self):
        return f'P({self.x}, {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P(self.x - other.x, self.y - other.y)


deltas = [  # position of T relative to H
    P(0, 0),  # overlapping
    P(1, 0),  # right
    P(-1, 0),  # left
    P(0, 1),  # top
    P(0, -1),  # bottom
    P(1, 1),  # right top
    P(1, -1),  # right bottom
    P(-1, 1),  # left top
    P(-1, -1)  # left bottom
]

moves = {
    'R': P(1, 0),  # step right
    'U': P(0, 1),  # step up
    'L': P(-1, 0),  # step left
    'D': P(0, -1),  # step down
}

new_delta_to_T_move = {  # after a move, how does T adjust
    P(2, -1): P(-1, 1),
    P(1, 2): P(-1, -1),
    P(2, 1): P(-1, -1),
    P(-2, -1): P(1, 1),
    P(-1, -2): P(1, 1),
    P(-2, 1): P(1, -1),
    P(2, 0): P(-1, 0),
    P(1, -2): P(-1, 1),
    P(-2, 0): P(1, 0),
    P(0, 2): P(0, -1),
    P(-1, 2): P(1, -1),
    P(0, -2): P(0, 1),
    P(2, 2): P(-1, -1),
    P(2, -2): P(-1, 1),
    P(-2, 2): P(1, -1),
    P(-2, -2): P(1, 1),
}
assert all(k.x < 0 and v.x > 0 or k.x == v.x == 0 or k.x > 0 and v.x < 0 for k, v in new_delta_to_T_move.items())
assert all(k.y < 0 and v.y > 0 or k.y == v.y == 0 or k.y > 0 and v.y < 0 for k, v in new_delta_to_T_move.items())
#
# data = '''R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2'''.splitlines(keepends=False)

with open('9/input') as handle:
    data = handle.read().splitlines(keepends=False)


def parse_line(s: str) -> list[str]:
    move, repeats = s.split()
    return [move] * int(repeats)


def draw_figure(rope):
    rev = {r: str(i) for i, r in enumerate(rope)}
    print('\n'.join((''.join(rev.get(P(i, j), '·') for i in range(6)) for j in range(6, -1, -1))))


n_links = 10
touched = {P(0, 0)}
rope = [P(0, 0) for _ in range(n_links)]
for command in chain.from_iterable(parse_line(line) for line in data):
    rope[0] += moves[command]
    for i in range(1, n_links):
        rope[i] -= new_delta_to_T_move.get(rope[i - 1] - rope[i], P(0, 0))
    # draw_figure(rope)
    touched.add(rope[-1])

print(len(touched))
