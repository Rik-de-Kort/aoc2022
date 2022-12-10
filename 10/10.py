from copy import copy
import re

with open('10/input') as handle:
    data = handle.read().splitlines(keepends=False)

instructions_per_cycle = []
for instr in data:
    if instr == 'noop':
        instructions_per_cycle.append(instr)
    elif m := re.match('addx (.*)', instr):
        instructions_per_cycle.extend(['noop', ('addx', int(m.group(1)))])

assert all(instructions_per_cycle[i] == 'noop' if isinstance(instructions_per_cycle[i + 1], tuple) else True for i in
           range(len(instructions_per_cycle) - 1))
assert len(instructions_per_cycle) == len(data) + sum(line.startswith('addx') for line in data)

cycle_count = []
x = 1
for instr in instructions_per_cycle:
    cycle_count.append(copy(x))
    if instr == 'noop':
        continue
    opcode, arg = instr
    assert opcode == 'addx'
    x += arg

print(sum((20 + 40 * i) * cycle_count[19 + 40 * i] for i in range(6)))


pixels = []
for i in range(6):
    line = []
    for j in range(40):
        x = cycle_count[i*40 + j]
        pixel_in_row = j
        # print(f'{x=} {pixel_in_row=}')
        if abs(pixel_in_row - x) <= 1:
            line.append('#')
        else:
            line.append('·')
    pixels.append(line)

print('\n'.join(''.join(line) for line in pixels))
