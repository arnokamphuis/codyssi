
# read command-line parameters and based on that read the input file
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day09-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]
idx = lines.index([])
start_balances = lines[:idx]
transactions = lines[idx+1:]


def part1():
    balances = { line[0]: int(line[2]) for line in start_balances }
    for ta in transactions:
        balances[ta[1]] -= int(ta[5])
        balances[ta[3]] += int(ta[5])
    return sum([v[1] for v in sorted(balances.items(), key=lambda x: x[1])[-3:]])

def part2():
    balances = { line[0]: int(line[2]) for line in start_balances }
    for ta in transactions:
        amt = min(int(ta[5]), balances[ta[1]])
        balances[ta[1]] -= amt
        balances[ta[3]] += amt
    return sum([v[1] for v in sorted(balances.items(), key=lambda x: x[1])[-3:]])

def part3():
    balances = { line[0]: int(line[2]) for line in start_balances }
    debts = { line[0]: [] for line in start_balances }
    
    def repay(t, amt):
        if amt == 0:
            return
        if len(debts[t]) == 0:
            balances[t] += amt
            return
        while amt > 0 and len(debts[t]) > 0:
            debt = debts[t][0]
            if debt[0] > amt:
                debts[t][0] = (debt[0] - amt, debt[1])
                repay(debt[1], amt)
                amt = 0
            else:
                amt -= debt[0]
                debts[t].pop(0)
                repay(debt[1], debt[0])
        if amt > 0:
            balances[t] += amt
    
    for ta in transactions:
        amt = min(int(ta[5]), balances[ta[1]])
        balances[ta[1]] -= amt

        if amt != int(ta[5]):
            debts[ta[1]].append((int(ta[5]) - amt, ta[3]))
            
        repay(ta[3], amt)

    return sum([v[1] for v in sorted(balances.items(), key=lambda x: x[1])[-3:]])

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
    
