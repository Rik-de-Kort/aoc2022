from dataclasses import dataclass
from typing import Callable


@dataclass(slots=True)
class Monkey:
    id: int
    items: list[int]
    operation: Callable[[int], int]
    test_num: int
    next_if_true: int
    next_if_false: int
    inspections: int = 0


monkeys = [Monkey(id=0, items=[54, 98, 50, 94, 69, 62, 53, 85], operation=lambda old: old * 13,
                  test_num=3, next_if_true=2, next_if_false=1, ),
           Monkey(id=1, items=[71, 55, 82], operation=lambda old: old + 2, test_num=13,
                  next_if_true=7, next_if_false=2),
           Monkey(id=2, items=[77, 73, 86, 72, 87], operation=lambda old: old + 8, test_num=19,
                  next_if_true=4, next_if_false=7),
           Monkey(id=3, items=[97, 91], operation=lambda old: old + 1, test_num=17,
                  next_if_true=6, next_if_false=5),
           Monkey(id=4, items=[78, 97, 51, 85, 66, 63, 62], operation=lambda old: old * 17,
                  test_num=5, next_if_true=6, next_if_false=3),
           Monkey(id=5, items=[88], operation=lambda old: old + 3, test_num=7, next_if_true=1,
                  next_if_false=0),
           Monkey(id=6, items=[87, 57, 63, 86, 87, 53], operation=lambda old: old * old,
                  test_num=11, next_if_true=5, next_if_false=0),
           Monkey(id=7, items=[73, 59, 82, 65], operation=lambda old: old + 6, test_num=2,
                  next_if_true=4, next_if_false=3), ]

assert not any(m.next_if_true == m.id or m.next_if_false == m.id for m in monkeys)

from functools import reduce
from operator import mul

FACTOR = reduce(mul, (m.test_num for m in monkeys), 1)

# for i in range(20):
for i in range(10000):
    for monkey in monkeys:
        monkey.inspections += len(monkey.items)
        for item in monkey.items:
            worry_level = monkey.operation(item)
            # worry_level = worry_level // 3
            worry_level = worry_level % FACTOR
            next_id = monkey.next_if_true if worry_level % monkey.test_num == 0 else monkey.next_if_false
            monkeys[next_id].items.append(worry_level)
        monkey.items = []

prod = lambda it: it[0] * it[1]
print(prod(sorted((m.inspections for m in monkeys), reverse=True)[:2]))
