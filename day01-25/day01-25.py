
# read command-line parameters and based on that read the input file
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day01-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]
numbers = [int(line[0]) for line in lines[:-1]]
symbols = list(lines[-1][0])

def part1():
    value = numbers[0]
    for i in range(1, len(numbers)):
        if symbols[i-1] == '+':
            value += numbers[i]
        else:
            value -= numbers[i]
    return value

def part2():
    value = numbers[0]
    for i in range(1, len(numbers)):
        if symbols[len(symbols)-i] == '+':
            value += numbers[i]
        else:
            value -= numbers[i]
    return value

def part3():
    new_numbers = [ numbers[i]*10 + numbers[i+1] for i in range(0, len(numbers), 2) ]
    value = new_numbers[0]
    for i in range(1, len(new_numbers)):
        if symbols[len(symbols)-i] == '+':
            value += new_numbers[i]
        else:
            value -= new_numbers[i]
    return value

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
    
