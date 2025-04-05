
# read command-line parameters and based on that read the input file
from copy import deepcopy
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day14-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]

lines = [[l for l in line if l not in ["|", ":", "Quality", "Unique", "Materials", "Cost"]] for line in lines]
lines = [[l.replace(",", "") for l in line] for line in lines]
lines = [[int(l[0]), l[1], int(l[2]), int(l[3]), int(l[4])] for l in lines]

items = [(l[2], l[3], l[4], l[1]) for l in lines]

def part1():
    sorted_items = sorted([(l[2], l[3], l[4]) for l in lines], reverse=True)
    return sum([i[2] for i in sorted_items[:5]])

# 0-1 knapsack problem
def solve(items, budget):
    knapsack = {0: (0, 0)}
    for item in items:
        item_cost = item[1]
        item_quality = item[0]
        item_materials = item[2]
        
        updates = {}

        for cost, (quality, materials) in knapsack.items():
            new_cost = cost + item_cost
            
            if new_cost <= budget:
                new_quality = quality + item_quality
                new_materials = materials + item_materials

                existing_quality, existing_materials = updates.get(new_cost, knapsack.get(new_cost, (-1, 10**9)))
                
                if new_quality > existing_quality or (new_quality == existing_quality and new_materials < existing_materials):
                    updates[new_cost] = (new_quality, new_materials)
        knapsack.update(updates)
                
    best_quality = 0
    best_materials = 0
    
    for cost, (quality, materials) in knapsack.items():
        if quality > best_quality or (quality == best_quality and materials < best_materials):
            best_quality = quality
            best_materials = materials
            
    return best_quality * best_materials

def part2():
    return solve(items, 30)

def part3():
    return solve(items, 300)

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
    
