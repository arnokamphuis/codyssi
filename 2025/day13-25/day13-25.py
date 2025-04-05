
# read command-line parameters and based on that read the input file
from collections import deque
from copy import deepcopy
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day13-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]
paths = {(line[0], line[2]) : int(line[4]) for line in lines}

edges = {}
for path in paths.items():
    edges[path[0][0]] = {}
    edges[path[0][1]] = {}

for path in paths:
    edges[path[0]][path[1]] = paths[path]

def find_all_paths(edges, path):
    start = path[-1]
    if start not in edges.keys() or len(edges[start]) == 0:
        return [path]
    
    paths = []
    for edge in edges[start].keys():
        if edge in path:
            continue
        new_paths = find_all_paths(edges, path + [edge])
        for np in new_paths:
            if np not in paths:
                paths.append(np)
        paths.extend(new_paths)
    return paths

def find_shortest_path(edges, start, end, use_length=False):
    previous = {n: {} for n in edges.keys()}
    distances = {n: 10**9 for n in edges.keys()}
        
    def construct_path(prevs, start, end, path, path_length):
        if start == end:
            return (path_length, path)
        for n in prevs[end].keys():
            new_path = construct_path(prevs, start, n, [n] + path, path_length + previous[end][n])
            if new_path is not None:
                return new_path
        return None
    
    q = deque([(0, start)])
    while len(q) > 0:
        length, node = q.popleft()
        if node == end:
            return construct_path(previous, start, end, [end], 0)
        
        for n in edges[node].keys():
            d = edges[node][n] if use_length else 1
            if length + d <= distances[n]:
                distances[n] = length + d
                previous[n] = {node: d}
                q.append((length + d, n))   
    return None

def longest_shortest_paths(start, use_length=False):
    paths = []
    for n in edges.keys():
        paths.append(find_shortest_path(edges, start, n, use_length))
    lengths = sorted([p[0] for p in paths], reverse=True)
    return lengths[0] * lengths[1] * lengths[2]

def part1():
    return longest_shortest_paths("STT", False)

def part2():
    return longest_shortest_paths("STT", True)

def part3():
    max_lenght = 0
    for f in edges.keys():
        for t in edges[f].keys():
            res = find_shortest_path(edges, t, f, True)
            if res is not None:
                length, _ = res
                max_lenght = max(max_lenght, length + edges[f][t])
           
    return max_lenght

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
    
