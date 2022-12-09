from copy import deepcopy
import re

with open('5/input') as handle:
    data = handle.read()

# data = '''    [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2'''

raw_stacks, raw_instructions = data.split('\n\n')
raw_stacks_ = list(zip(*raw_stacks.splitlines(keepends=False)))
stacks = [[item for item in stack[:-1] if item != ' '] for stack in raw_stacks_ if stack[-1] != ' ']
print(stacks)

instructions = [
    tuple(int(x) for x in re.search(r'move (\d+) from (\d+) to (\d)', line).groups())
    for line in raw_instructions.splitlines(keepends=False)
]
print(instructions)


def move_9000(stacks, n, from_stack, to_stack):
    # Zero-indexed
    from_stack -= 1
    to_stack -= 1
    stacks[from_stack], moved = stacks[from_stack][n:], stacks[from_stack][:n]
    stacks[to_stack] = list(reversed(moved)) + stacks[to_stack]
    return stacks


assert move_9000([['A', 'B', 'C'], ['D', 'E']], 1, 1, 2) == [['B', 'C'], ['A', 'D', 'E']]
assert move_9000([['A', 'B', 'C'], ['D', 'E']], 2, 1, 2) == [['C'], ['B', 'A', 'D', 'E']]

result_stacks = deepcopy(stacks)
for instruction in instructions:
    # print(result_stacks)
    result_stacks = move_9000(result_stacks, *instruction)

# print(result_stacks)
print(''.join(stack[0] for stack in result_stacks))


def move_9001(stacks, n, from_stack, to_stack):
    # Zero-indexed
    from_stack -= 1
    to_stack -= 1
    stacks[from_stack], moved = stacks[from_stack][n:], stacks[from_stack][:n]
    stacks[to_stack] = moved + stacks[to_stack]
    return stacks


assert move_9001([['A', 'B', 'C'], ['D', 'E']], 1, 1, 2) == [['B', 'C'], ['A', 'D', 'E']]
assert move_9001([['A', 'B', 'C'], ['D', 'E']], 2, 1, 2) == [['C'], ['A', 'B', 'D', 'E']]

result_stacks = deepcopy(stacks)
for instruction in instructions:
    # print(result_stacks)
    result_stacks = move_9001(result_stacks, *instruction)

# print(result_stacks)
print(''.join(stack[0] for stack in result_stacks))
