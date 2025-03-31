
# read command-line parameters and based on that read the input file
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day15-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]
idx = lines.index([])
artifacts = [[l[0], int(l[2])] for l in lines[:idx]]

checks = [[l[0], int(l[2])] for l in lines[idx+1:]]
print(checks)


def compare(art1, art2):
    if art1[1] < art2[1]:
        return -1
    elif art1[1] > art2[1]:
        return 1
    else:
        return 0

def insert(node, artifact, no_insert=False):
    cmp = compare(artifact, node[0])
    name = [node[0][0]]
    if cmp < 0:
        if node[1][0] == None and not no_insert:
            node[1][0] = [artifact, [None, None]]
        else:
            name = [*name, *insert(node[1][0], artifact)]
    elif cmp > 0:
        if node[1][1] == None and not no_insert:
            node[1][1] = [artifact, [None, None]]
        else:
            name = [*name, *insert(node[1][1], artifact)]
    return name

def get_layer_nodes(root, level):
    if level == 0:
        return [root[0]]
    else:
        nodes = []
        if root[1][0] != None:
            nodes += get_layer_nodes(root[1][0], level - 1)
        if root[1][1] != None:
            nodes += get_layer_nodes(root[1][1], level - 1)
        return nodes

root = [artifacts[0], [None, None]]
for i in range(1, len(artifacts)):
    insert(root, artifacts[i])

def part1():
    l = 0
    max_size = 0
    while get_layer_nodes(root, l) != []:
        s = sum([a[1] for a in get_layer_nodes(root, l)])
        if s > max_size:
            max_size = s
        l+=1

    return l * max_size

def part2():
    return '-'.join(insert(root, ["new", 500000], no_insert=True))

def part3():
    check1 = insert(root, checks[0], no_insert=True)
    check2 = insert(root, checks[1], no_insert=True)
    for l in range(min(len(check1), len(check2))):
        if check1[l] != check2[l]:
            return check1[l-1]
    return 0

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
    
