from pathlib import Path
import re

with open('7/input') as handle:
    data = handle.read().splitlines(keepends=False)

current_dir = Path('/')
directory_map = {}
i = 1
while i < len(data):
    if m := re.match(r'\$ cd (.*)', data[i]):
        new_dir = m.group(1)
        current_dir = current_dir.parent if new_dir == '..' else current_dir / new_dir
        i += 1
    elif m := re.match(r'\$ ls', data[i]):
        i += 1
        listed_files = []
        while i < len(data) and not data[i].startswith('$'):
            if not data[i].startswith('dir'):
                size, filename = data[i].split(' ')
                listed_files.append((filename, int(size)))
            i += 1
        if current_dir not in directory_map:
            directory_map[current_dir] = listed_files


def calculate_directory_size(dir_map, dir_path):
    return sum(size for name, files in dir_map.items() for filename, size in files if name.is_relative_to(dir_path))


directory_sizes = {dir_path: calculate_directory_size(directory_map, dir_path) for dir_path in directory_map.keys()}
print(sum(size for dir_path, size in directory_sizes.items() if size <= 100_000))

total_space = 70_000_000
unused_space = total_space - directory_sizes[Path('/')]
needed_space = 30_000_000
to_free_up = needed_space - unused_space

print(min((size for path, size in directory_sizes.items() if size >= to_free_up)))
