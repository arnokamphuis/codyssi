
# read command-line parameters and based on that read the input file
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day05-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]
coordinates = [(int(line[0][1:-1]), int(line[1][:-1])) for line in lines]

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def part1():
    distances = [dist(c, (0,0)) for c in coordinates]
    min_dist = min(distances)
    max_dist = max(distances)
    return max_dist - min_dist

def find_closest(current, candidates):
    distances = [(dist(c, current), c) for c in candidates if c != current]
    distances.sort()
    return distances[0][1]

def part2():
    distances = [(dist(c, (0,0)), c) for c in coordinates]
    distances.sort()
    closest = distances[0][1]
    return dist(closest,find_closest(closest, coordinates))

def part3():
    ans = 0
    candidates = coordinates
    current = (0,0)
    while candidates:
        closest = find_closest(current, candidates)
        candidates.remove(closest)
        ans += dist(current, closest)
        current = closest
    
    return ans

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
    
