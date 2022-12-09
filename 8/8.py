from collections import defaultdict

with open('8/input') as handle:
    data = handle.read().splitlines(keepends=False)

# data = '''30373
# 25512
# 65332
# 33549
# 35390'''.splitlines(keepends=False)

trees = {(i, j): int(x) for i, row in enumerate(data) for j, x in enumerate(row)}
n_rows = len(data)
n_cols = len(data[0])


def mark_visible_rows(rows, cols):
    for i in rows:
        top = -1
        for j in cols:
            # print(f'{(i, j)} {trees[i, j]=}, {top=} {visible[i, j]=}')
            if trees[i, j] > top:
                visible[i, j] = True
                top = trees[i, j]


def mark_visible_cols(cols, rows):
    for i in cols:
        top = -1
        for j in rows:
            # print(f'{(j, i)} {trees[j, i]=}, {top=} {visible[j, i]=}')
            if trees[j, i] > top:
                visible[j, i] = True
                top = trees[j, i]


visible = defaultdict(lambda: False)
mark_visible_rows(range(n_rows), range(n_cols))  # left to right
mark_visible_rows(range(n_rows), range(n_cols - 1, -1, -1))  # right to left
mark_visible_cols(range(n_cols), range(n_rows))  # top to bottom
mark_visible_cols(range(n_cols), range(n_rows - 1, -1, -1))  # bottom to top
visible = dict(visible)

assert all(visible[0, j] for j in range(n_cols))
assert all(visible[n_rows - 1, j] for j in range(n_cols))
assert all(visible[i, 0] for i in range(n_rows))
assert all(visible[i, n_cols - 1] for i in range(n_rows))

print(sum(visible.values()))
#
# def print_visible(visible):
#     print('\n'.join(''.join('1' if visible[i, j] else '0' for j in range(n_cols)) for i in range(n_rows)))
#
# print_visible(visible)
# print('\n'.join(data))


def scenic_score(row, col):
    direction_top = 0
    for i in range(row-1, -1, -1):
        if trees[i, col] < trees[row, col]:
            direction_top += 1
        elif trees[i, col] >= trees[row, col]:
            direction_top += 1
            break
    direction_bottom = 0
    for i in range(row+1, n_rows):
        if trees[i, col] < trees[row, col]:
            direction_bottom += 1
        elif trees[i, col] >= trees[row, col]:
            direction_bottom += 1
            break
    direction_left = 0
    for j in range(col-1, -1, -1):
        if trees[row, j] < trees[row, col]:
            direction_left += 1
        elif trees[row, j] >= trees[row, col]:
            direction_left += 1
            break
    direction_right = 0
    for j in range(col+1, n_cols):
        if trees[row, j] < trees[row, col]:
            direction_right += 1
        elif trees[row, j] >= trees[row, col]:
            direction_right += 1
            break
    # print(f'{direction_top=} {direction_right=} {direction_left=} {direction_bottom=}')
    return direction_top * direction_right * direction_bottom * direction_left

print(max(scenic_score(i, j) for i in range(n_rows) for j in range(n_cols)))
