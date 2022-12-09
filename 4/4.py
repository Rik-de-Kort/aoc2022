with open('4/input') as handle:
    data = handle.read().splitlines(keepends=False)

elves = [tuple(tuple(int(x) for x in elf.split('-')) for elf in line.split(',')) for line in data]


def full_overlap(first, second):
    x, y = first
    u, w = second
    return u <= x <= y <= w or x <= u <= w <= y


print(sum(full_overlap(*pair) for pair in elves))


def partial_overlap(first, second):
    x, y = first
    u, w = second
    return x <= u <= y or x <= w <= y or u <= x <= w or u <= y <= w


print(sum(partial_overlap(*pair) for pair in elves))
