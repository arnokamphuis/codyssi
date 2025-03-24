
import re
# read command-line parameters and based on that read the input file
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day08-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]


def part1():
    rgx = re.compile('[a-zA-Z]')
    return sum([len(rgx.findall(line[0])) for line in lines])

def reduce(line, hyphen_included):
    rgx = re.compile(r'([a-zA-Z]|\-)(\d)|(\d)([a-zA-Z]|\-)') if hyphen_included else re.compile(r'([a-zA-Z])(\d)|(\d)([a-zA-Z])')
    matches = rgx.findall(line)
    if len(matches) > 0:
        for match in matches:
            toberemove = match[0] + match[1]
            if match[0] == '':
                toberemove = match[2] + match[3]
            line = line.replace(toberemove, '')
    else:
        return line
    return reduce(line, hyphen_included)

def part2():
    return sum([len(reduce(line[0], True)) for line in lines])

def part3():
    return sum([len(reduce(line[0], False)) for line in lines])

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
    
