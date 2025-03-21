
# read command-line parameters and based on that read the input file
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day04-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]

def bytes(s):
    b = 0
    for c in s:
        if ord('0') <= ord(c) <= ord('9'):
            b += int(c)
        else:
            b += ord(c)-ord('A')+1
    return b

def part1():
    ans = 0
    for line in lines:
        ans += bytes(line[0])
        # ans += sum([ord(c)-ord('A')+1 for c in line[0]])
    return ans

def part2():
    ans = 0
    for line in lines:
        s = line[0]
        l = len(s)//10
        ns = ''.join([*s[:l], str(len(s)-2*l), *s[len(s)-l:]])
        ans += bytes(ns)
    return ans

def part3():
    ans = 0
    for line in lines:
        new_s = ''
        s = line[0]
        offset = 0
        while offset < len(s):
            c = s[offset]
            i = offset
            while i < len(s) and s[i] == c:
                i += 1
            l = i - offset
            new_s += str(l) + c
            offset = i
        ans += bytes(new_s)
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
    
