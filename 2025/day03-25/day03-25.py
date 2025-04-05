
# read command-line parameters and based on that read the input file
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day03-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]

def part1():
    total = 0
    for line in lines:
        for range in line:
            min, max = map(int,range.split('-'))
            total += max - min + 1
    return total

def overlap(r1, r2):
    if r1[0] > r2[1] or r2[0] > r1[1]:
        return []
    else:
        return [max(r1[0], r2[0]), min(r1[1], r2[1])]

def size(r):
    return r[1] - r[0] + 1

def part2():
    total = 0
    for line in lines:
        ranges = []
        for range in line:
            ranges.append(list(map(int,range.split('-'))))
        overlap_range = overlap(ranges[0], ranges[1])
        total += size(ranges[0]) + size(ranges[1])
        if len(overlap_range) > 0:
            total -= size(overlap_range)
    return total

def part3():
    max_size = 0
    adj = list(zip(lines[:-1], lines[1:]))
    for a1, a2 in adj:
        intervals = [list(map(int, l.split('-'))) for l in list([*a1, *a2])]            
        intervals.sort()
        new_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            ni = new_intervals[-1]
            overlap_range = overlap(ni, intervals[i])
            if overlap_range:
                new_intervals[-1] = [min(ni[0], intervals[i][0]), max(ni[1], intervals[i][1])]
            else:
                new_intervals.append(intervals[i])
              
        max_size = max(max_size, sum(list(map(size, new_intervals))))
    return max_size

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
    
