with open('6/input') as handle:
    data = handle.read().strip()


def window(it: list, n: int = 4):
    for i in range(0, len(it) - n):
        yield it[i:i + n]


for i, group in enumerate(window(data, 4)):
    if len(set(group)) == len(group):
        print(i + 4)
        break

for i, group in enumerate(window(data, 14)):
    if len(set(group)) == len(group):
        print(i + 14)
        break
