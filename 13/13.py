from ast import literal_eval
from functools import cmp_to_key
from itertools import zip_longest, chain
from typing import Optional

with open('13/input') as handle:
    data = [tuple(literal_eval(x) for x in pair.splitlines(keepends=False)) for pair in handle.read().split('\n\n')]


def is_sorted(left, right) -> Optional[bool]:
    """Are inputs in correct order? True, False, or None (inconclusive)"""
    match (left, right):
        case int(x), int(y) if x < y:
            return True
        case int(x), int(y) if x == y:
            return None
        case int(x), int(y) if x > y:
            return False
        case (int(x), list(y)):
            return is_sorted([x], y)
        case (list(x), int(y)):
            return is_sorted(x, [y])
        case (list(x), list(y)):
            for i, j in zip_longest(x, y, fillvalue=None):
                if i is None:
                    return True
                if j is None:
                    return False
                result = is_sorted(i, j)
                if result is not None:
                    return result
            return None
        case _:
            raise ValueError


assert is_sorted(5, 4) is False
assert is_sorted([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) is True
assert is_sorted([[1], [2, 3, 4]], [[1], 4]) is True
assert is_sorted([9], [[8, 7, 6]]) is False
assert is_sorted([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) is True
assert is_sorted([7, 7, 7, 7], [7, 7, 7]) is False
assert is_sorted([], [3]) is True
assert is_sorted([[[]]], [[]]) is False
assert is_sorted([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]) is False

print(sum(i + 1 for i, (left, right) in enumerate(data) if is_sorted(left, right)))

data.append(([[2]], [[6]]))
sorted_packages = sorted(chain.from_iterable(data), key=cmp_to_key(lambda l, r: -1 if is_sorted(l, r) is True else 1))
print((sorted_packages.index([[2]]) + 1) * (sorted_packages.index([[6]])+1))
