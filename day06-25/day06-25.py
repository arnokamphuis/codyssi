# read command-line parameters and based on that read the input file
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day06-{runtype}.txt", "r")

lines = [line.split()[0] for line in text_file.readlines()]

def value(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 27
    return None

def score(s, count_only, amend):
    ret = 0
    prev_val = None
    for c in s:
        val = None
        uncorrupted = ('a' <= c <= 'z') or ('A' <= c <= 'Z')
        if uncorrupted:
            if count_only:
                ret += 1
            else:
                ret += value(c)
            if amend:
                val = value(c)
        else:
            if amend and prev_val is not None:                
                val = (prev_val * 2 - 5) % 52
                ret += val
        prev_val = val
    return ret

def part1():
    ans = 0
    for line in lines:
        ans += score(line, True, False)
    return ans

def part2():
    ans = 0
    for line in lines:
        ans += score(line, False, False)
    return ans

def part3():
    ans = 0
    for line in lines:
        ans += score(line, False, True)
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
    
