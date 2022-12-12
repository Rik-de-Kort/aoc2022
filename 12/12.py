from tqdm import tqdm

with open('12/input') as handle:
    data = handle.read().splitlines(keepends=False)

height = len(data)
width = len(data[0])
start = [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == 'S'][0]
end = [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == 'E'][0]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
height_map = {c: i for i, c in enumerate(alphabet)} | {'S': 0, 'E': 25}
map = {(i, j): height_map[char] for i, line in enumerate(data) for j, char in enumerate(line)}


def neighbours(i, j):
    if i > 0:
        yield i - 1, j
    if i < height - 2:
        yield i + 1, j
    if j > 0:
        yield i, j - 1
    if j < width - 2:
        yield i, j + 1


visitable_neighbours = {(i, j): [(i_, j_) for i_, j_ in neighbours(i, j) if map[i_, j_] <= h + 1] for (i, j), h in
                        map.items()}
INF = height * width + 1


def dijkstra(start, end):
    distances = {p: INF for p in map.keys()} | {start: 0}
    previous = {p: None for p in map.keys()}
    unvisited = sorted([p for p in map.keys()], key=lambda p: distances[p])
    while unvisited:
        u = unvisited.pop(0)
        for v in visitable_neighbours[u]:
            if v in unvisited:
                from_u = distances[u] + 1
                if from_u < distances[v]:
                    distances[v] = from_u
                    previous[v] = u
        unvisited = sorted(unvisited, key=lambda p: distances[p])
    return distances[end]


print(dijkstra(start, end))
print(min(dijkstra(s, end) for s, h in tqdm(map.items()) if h == 0))
