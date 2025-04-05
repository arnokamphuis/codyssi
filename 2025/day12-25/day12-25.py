
# read command-line parameters and based on that read the input file
from copy import deepcopy
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day12-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]

idx = lines.index([])
amplitudes = lines[:idx]
amplitudes = [[int(amp) for amp in row] for row in amplitudes]

original_amplitudes =  deepcopy(amplitudes)

lines = lines[idx+1:]
idx = lines.index([])
instructions = lines[:idx]
lines = lines[idx+1:]
flowcontrol = [l[0] for l in lines]

mod_value = 1073741824
# print(amplitudes)
# print(instructions)
# print(flowcontrol)

def update_row(row, instruction, amount):
    global amplitudes
    # print(row, instruction, amount)
    if instruction == "SHIFT":
        # print("before", amplitudes[row])
        amplitudes[row] = amplitudes[row][-amount:] + amplitudes[row][:-amount] 
        # print("after", amplitudes[row])
    else:
        for i in range(len(amplitudes[row])):
            if instruction == "MULTIPLY":
                amplitudes[row][i] = (amplitudes[row][i] * amount) % mod_value
            elif instruction == "ADD":
                amplitudes[row][i] = (amplitudes[row][i] + amount) % mod_value
            elif instruction == "SUB":
                amplitudes[row][i] = (amplitudes[row][i] - amount) % mod_value
            else:
                print("Unknown instruction")
                assert(False)
            assert(amplitudes[row][i] >= 0)
            assert(amplitudes[row][i] < mod_value)

def update_col(col, instruction, amount):
    global amplitudes
    amplitudes = list(map(list, zip(*amplitudes)))
    update_row(col, instruction, amount)
    amplitudes = list(map(list, zip(*amplitudes)))

def update_all(instruction, amount):
    global amplitudes
    for i in range(len(amplitudes)):
        update_row(i, instruction, amount)

def max_sum_row():
    global amplitudes
    max_sum = 0
    for i in range(len(amplitudes)):
        row_sum = sum(amplitudes[i])
        max_sum = max(max_sum, row_sum)
    return max_sum

def max_sum_col():
    global amplitudes
    amplitudes = list(map(list, zip(*amplitudes)))
    max_sum = max_sum_row()
    amplitudes = list(map(list, zip(*amplitudes)))
    return max_sum

insts = []
for instruction in instructions:
    inst_type = instruction[0]
    col_or_row = 'ALL'
    if "COL" in instruction:
        col_or_row = 'COL'
    elif "ROW" in instruction:
        col_or_row = 'ROW'
    if col_or_row != 'ALL':
        idx = instruction.index(col_or_row)
        col_or_row_id = int(instruction[idx+1]) - 1
    else:
        col_or_row_id = -1
    val = int(instruction[-1]) if inst_type == "SHIFT" else int(instruction[1])            

    insts.append((col_or_row, col_or_row_id, inst_type, val))

def do_instruction(inst):
    col_or_row, col_or_row_id, inst_type, val = inst
    if col_or_row == 'COL':
        update_col(col_or_row_id, inst_type, val)
    elif col_or_row == 'ROW':
        update_row(col_or_row_id, inst_type, val)
    else:
        update_all(inst_type, val)

def part1():
    global amplitudes
    amplitudes = deepcopy(original_amplitudes)

    for inst in insts:
        do_instruction(inst)
    return max(max_sum_row(), max_sum_col())

def part2():
    global amplitudes
    amplitudes = deepcopy(original_amplitudes)

    inst = None
    instructions = insts.copy()
    for flow in flowcontrol:
        if flow == "TAKE":
            inst = instructions.pop(0)
        elif flow == "CYCLE":
            instructions.append(inst)
        else:
            do_instruction(inst)            
    return max(max_sum_row(), max_sum_col())

def part3():
    global amplitudes
    amplitudes = deepcopy(original_amplitudes)

    fidx = 0
    instructions = insts.copy()
    while True:
        flow = flowcontrol[fidx]
        if flow == "TAKE":
            inst = instructions.pop(0)
        elif flow == "CYCLE":
            instructions.append(inst)
        else:
            do_instruction(inst)
            if len(instructions) == 0:
                break
        fidx = (fidx+1) % len(flowcontrol)

    return max(max_sum_row(), max_sum_col())

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
    
