
# read command-line parameters and based on that read the input file
from collections import defaultdict, deque
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day17-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]
idx = lines.index([])
stairs_descriptions = lines[:idx]
moves = list(map(int, ' '.join(lines[-1]).removeprefix("Possible Moves : ").split(", ")))

edges = defaultdict(list)
for i in range(len(stairs_descriptions)):
    stairs = int(stairs_descriptions[i][0].removeprefix('S'))
    f = int(stairs_descriptions[i][2])
    t = int(stairs_descriptions[i][4])

    a = int(stairs_descriptions[i][7].removeprefix('S')) if i > 0 else 1
    b = int(stairs_descriptions[i][9].removeprefix('S')) if i > 0 else 1

    for j in range(f, t + 1):
        if (stairs, j) not in edges:
            edges[(stairs, j)] = []

        if j > f:
            edges[(stairs,j-1)].append((stairs,j))

    if i == 0:
        begin = (stairs, f)
        end = (stairs, t)
    if i > 0:
        edges[(a, f)] += [(stairs, f)]
        edges[(stairs, t)] += [(b, t)]

def reachable(position, moves):
    s, j = position
    result = set()
    q = deque([(0, (s, j))])
    max_moves = max(moves)
    while q:
        d, (s, j) = q.popleft()
        
        if d > max_moves:
            continue

        if d in moves:
            result.add((s, j))

        if d+1 <= max_moves:
            for i in edges[(s, j)]:
                q.append((d + 1, i))
    return result

def make_graph(edges, moves):
    steps = defaultdict(set)
    for v in edges.keys():
        steps[v] = set()
        vertices = reachable(v, moves)
        for i in vertices:
            steps[v].add(i)
    return steps

def count_paths(steps, begin, end):
    timestamps = defaultdict(int)
    timestamps[begin] = 0
    current = set([begin])
    time = 1
    while current:
        next_current = set()
        for c in current:
            for i in steps[c]:
                if i not in timestamps or timestamps[i] < time:
                    timestamps[i] = time
                    next_current.add(i)
        time += 1
        current = next_current
    max_time = max(timestamps.values())
    timestamps = {k: max_time - v for k, v in timestamps.items()}

    timed = defaultdict(list)
    for k, v in timestamps.items():
        timed[v].append(k)

    counter = defaultdict(int)
    counter[end] = 1
    for t in range(max_time + 1):
        for vertex in timed[t]:
            for next in steps[vertex]:
                counter[vertex] += counter[next]
    return counter

def part1():
    stairs = {k: v for k, v in edges.items() if k[0] == 1}
    stairs = {k: {fv for fv in v if fv[0] == 1} for k, v in stairs.items()}
    graph = make_graph(stairs, moves)
    return count_paths(graph, begin, end)[begin]

def part2():
    graph = make_graph(edges, moves)
    return count_paths(graph, begin, end)[begin]

def part3():
    graph = make_graph(edges, moves)
    counter = count_paths(graph, begin, end)
    
    target = 100000000000000000000000000000
    path = [begin]
    while path[-1] != end:
        vertex = path[-1]
        reachable_vertices_sorted = sorted(graph[vertex])
        path += [reachable_vertices_sorted[0]]
        for next_vertex in reachable_vertices_sorted:
            path[-1] = next_vertex
            if target - counter[next_vertex] <= 0:
                break
            target -= counter[next_vertex]
    return '-'.join(f"S{vertex[0]}_{vertex[1]}" for vertex in path)

if runpart == 1 or runpart == 0:
    for run in range(runs):
        resp1 = part1()
    print("Part 1: {}".format(resp1))

if runpart == 2 or runpart == 0:
    for run in range(runs):
        resp2 = part2()
    print("Part 2: {}".format(resp2))
    
if runpart == 3 or runpart == 0:
    for run in range(runs):
        resp3 = part3()
    print("Part 3: {}".format(resp3))
    
