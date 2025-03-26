from collections import deque
# read command-line parameters and based on that read the input file
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day10-{runtype}.txt", "r")

map = [list(map(int,line.split())) for line in text_file.readlines()]

def part1():
    mn = 10**9
    transmap = list(zip(*map))
    for i in range(len(map)):
        mn = min(mn, sum(map[i]), sum(transmap[i]))    
    return mn

def get_min_length(s, t):
    dirs = [(1,0), (0,1)]
    
    def floodfill(s, t):
        filled = {s: map[s[1]][s[0]]}
        q = deque([s])
        while q:
            x,y = q.popleft()
            for dx,dy in dirs:
                nx,ny = x+dx,y+dy
                if 0 <= nx <= t[1] and 0 <= ny <= t[0] and ((ny,nx) not in filled.keys() or filled[(ny,nx)] > filled[(y,x)] + map[ny][nx]):
                    q.append((nx,ny))
                    filled[(ny,nx)] = filled[(y,x)] + map[ny][nx]
        return filled
    
    fill = floodfill(s,t)
    return fill[t]
    
def part2():
    return get_min_length((0,0), (14,14))


def part3():
    return get_min_length((0,0), (len(map)-1,len(map)-1))

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
    
