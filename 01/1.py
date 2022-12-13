with open('1/input') as handle:
    lines = handle.read()

elves = lines.split('\n\n')
elves_parsed = [[int(s.strip()) for s in elf.split('\n') if s.strip()] for elf in elves]

print(max(sum(elf) for elf in elves_parsed))
print(sum(sorted((sum(elf) for elf in elves_parsed), reverse=True)[:3]))
