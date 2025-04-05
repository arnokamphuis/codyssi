
# read command-line parameters and based on that read the input file
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day02-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]
funcA = lines[0][2:]
funcB = lines[1][2:]
funcC = lines[2][2:]

room_qualities = sorted([int(line[0]) for line in lines[4:]])
median = len(room_qualities) // 2

def apply(command, value):
    if command[0] == 'ADD':
        return value + int(command[1])
    elif command[0] == 'SUBTRACT':
        return value - int(command[1])
    elif command[0] == 'MULTIPLY':
        return value * int(command[1])
    elif command[0] == 'DIVIDE':
        return value // int(command[1])
    elif command[0] == 'RAISE':
        return value ** int(command[5])
    
def part1():
    value = room_qualities[median]
    value = apply(funcC, value)
    value = apply(funcB, value)
    value = apply(funcA, value)
    return value

def part2():
    even_rooms = [room for room in room_qualities if room % 2 == 0]
    total_sum = sum(even_rooms)
    return apply(funcA, apply(funcB, apply(funcC, total_sum)))

def part3():
    for i in range(len(room_qualities)):
        price = apply(funcA, apply(funcB, apply(funcC, room_qualities[i])))
        if price > 15000000000000:
            return room_qualities[i-1]

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
    
