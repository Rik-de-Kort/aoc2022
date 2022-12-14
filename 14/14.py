from ast import literal_eval
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from itertools import product


@dataclass(slots=True)
class P:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    def __sub__(self, other):
        return P(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        if isinstance(other, int):
            return P(self.x + other, self.y + other)
        return P(self.x + other.x, self.y + other.y)

    def __iter__(self):
        return iter((self.x, self.y))


def print_cave(cave):
    min_i = min(i for i, _ in cave.keys())
    max_i = max(i for i, _ in cave.keys())
    min_j = min(j for _, j in cave.keys())
    max_j = max(j for _, j in cave.keys())
    print('\n'.join(
        ''.join(cave.get(P(i, j), Pixel.AIR).value for i in range(min_i, max_i + 1)) for j in range(min_j, max_j + 1)
    ))


with open('14/input') as handle:
    data = handle.read().splitlines(keepends=False)

# data = '''498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9'''.splitlines(keepends=False)

lines = [[P(*literal_eval(point)) for point in item.split(' -> ')] for item in data]


class Pixel(Enum):
    ROCK = '#'
    AIR = '·'
    SAND = 'o'
    SOURCE = '+'


def load_cave(lines):
    cave = {P(500, 0): Pixel.SOURCE}
    for line in lines:
        (i, j), *rest = line
        while rest:
            (i_, j_), *rest = rest
            if i != i_ and j != j_:
                raise ValueError
            for x, y in product(range(min(i, i_), max(i, i_) + 1), range(min(j, j_), max(j, j_) + 1)):
                cave[P(x, y)] = Pixel.ROCK
            i, j = i_, j_
    return cave


cave = load_cave(lines)
end = max(j for _, j in cave.keys())
counter = 0


# print_cave(cave)

def simulate_sand(sand: P, cave: dict[P, Pixel], end=None) -> P:
    end = max(p.y for p in cave.keys()) if end is None else end
    while sand.y < end:
        attempt = sand + P(0, 1)
        if attempt in cave:
            attempt = attempt + P(-1, 0)
            if attempt in cave:
                attempt = attempt + P(2, 0)  # Correct for step left
                if attempt in cave:
                    break
        sand = attempt
    return sand


cave = load_cave(lines)
end = max(p.y for p in cave.keys())
while True:
    sand = simulate_sand(P(500, 0), cave, end)
    if sand.y == end:
        break
    if cave.get(sand, Pixel.AIR) != Pixel.SOURCE:
        cave[sand] = Pixel.SAND
    counter += 1
print_cave(cave)

print(counter)

cave = load_cave(lines)
end = max(j for _, j in cave.keys()) + 1
counter = 0
done = False
while not done:
    sand = simulate_sand(P(500, 0), cave, end)
    counter += 1
    if sand == P(500, 0):
        break
    if cave.get(sand, Pixel.AIR) != Pixel.SOURCE:
        cave[sand] = Pixel.SAND
    if counter % 100 == 0:
        print_cave(cave)

print(counter)
