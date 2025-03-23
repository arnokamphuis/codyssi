
# read command-line parameters and based on that read the input file
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day07-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]
idx = 0
while lines[idx] != []:
    idx += 1

freqs = [int(x[0]) for x in lines[:idx]]
swaps = [list(map(int,x[0].split('-'))) for x in lines[idx+1:-2]]
test  = int(lines[-1][0])

def part1():
    new_freqs = freqs.copy()
    for swap in swaps:
        new_freqs[swap[0]-1], new_freqs[swap[1]-1] = new_freqs[swap[1]-1], new_freqs[swap[0]-1]
    return new_freqs[test-1]

def part2():
    new_freqs = freqs.copy()
    combs = zip(swaps, [*swaps[1:], swaps[0]])
    for swap1, swap2 in combs:
        new_freqs[swap1[1]-1], new_freqs[swap2[0]-1], new_freqs[swap1[0]-1] = new_freqs[swap1[0]-1], new_freqs[swap1[1]-1], new_freqs[swap2[0]-1]
    return new_freqs[test-1]

def part3():
    sorted_swaps = [sorted(s) for s in swaps]
    new_freqs = freqs.copy()
    n = len(freqs)
    for swap in sorted_swaps:
        swap_size = min(n - swap[1] + 1, swap[1] - swap[0])
        for idx in range(swap_size):
            new_freqs[swap[0]+idx-1], new_freqs[swap[1]+idx-1] = new_freqs[swap[1]+idx-1], new_freqs[swap[0]+idx-1]
    return new_freqs[test-1]

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
    
