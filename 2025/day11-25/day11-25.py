
# read command-line parameters and based on that read the input file
from math import ceil, exp, log
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day11-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]

# The file uses many number bases, from 2 to 62. For your information, the digits from 0 to 9 represent numbers 0 to 9, 
# the uppercase characters from A to Z represent numbers 10 to 35, and the lowercase characters from a to z represent 
# numbers 36 to 61. For example, h represents 43, and W represents 32.
def get_val(c):
    if c.isdigit():
        return int(c)
    if c.isupper():
        return ord(c) - 55
    if c.islower():
        return ord(c) - 61
    return 0

def to_digit68(d):
    extra_digits = { 62: '!', 63: '@', 64: '#', 65: '$', 66: '%', 67: '^'}
    if d < 10:
        return str(d)
    if d < 36:
        return chr(d + 55)
    if d < 62:
        return chr(d + 61)
    return extra_digits[d]

def to_base68(n):
    res = ""
    while n > 0:
        res = to_digit68(n % 68) + res
        n //= 68
    return res

def get_base10(s, base):
    ans = 0
    for c in s:
        ans = ans * base + get_val(c)
    return ans

def part1():
    res = 0
    for line in lines:
        ans = get_base10(line[0], int(line[1]))
        res = max(res, ans)    
    return res

def part2():
    res = 0
    for line in lines:
        res += get_base10(line[0], int(line[1]))
    return to_base68(res)

def part3():
    res = 0
    for line in lines:
        res += get_base10(line[0], int(line[1]))
    return ceil(exp(log(res) / 4))

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
    
