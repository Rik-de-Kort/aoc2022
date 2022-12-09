from collections import Counter

with open('3/input') as handle:
    data = handle.read().splitlines(keepends=False)

assert all(len(s) % 2 == 0 for s in data)

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def to_priority(s: str) -> Counter:
    return Counter(alphabet.index(x) + 1 for x in s)

def to_rucksack(s: str) -> (Counter, Counter):
    halfway = len(s) // 2
    return to_priority(s[:halfway]), to_priority(s[halfway:])


total = 0
for s in data:
    left, right = to_rucksack(s)
    total += sum(left.keys() & right.keys())

print(total)


def in_threes(items: list):
    for i in range(0, len(items), 3):
        yield items[i], items[i + 1], items[i + 2]


print(sum(sum(to_priority(a).keys() & to_priority(b).keys() & to_priority(c).keys()) for a, b, c in in_threes(data)))
total = 0
for a, b, c in in_threes(data):
    total += (to_priority(a), to_priority(b)


