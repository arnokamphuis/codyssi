
# read command-line parameters and based on that read the input file
import math
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day16-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]
idx = lines.index([])
instructions = [l for l in lines[:idx]]
twists = [list(l[0]) for l in lines[idx+1:]][0]

# print(f"Instructions: {instructions}")
# print(f"Twists: {twists}")

# grid_size = 3 if runtype == "test" else 80
grid_size = 80

cube_faces = [[[1 for _ in range(grid_size)] for _ in range(grid_size)] for _ in range(6)]

def rotate_ccw(matrix):
    return [list(row) for row in zip(*matrix)][::-1]

def rotate_cw(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

#
#     1
#   3 0 4
#     2
#     5
#

absorptions = { k: 0 for k in range(6) }

up = { 0: 1, 1: 5, 2: 0, 3: 1, 4: 1, 5: 2 }

faces = { 'front': 0, 'back': 5, 'left': 3, 'right': 4, 'up': 1, 'down': 2 }

def get_face_orientation():
    global faces
    up_orientation = up[faces['front']]
    
    if faces['left'] == up_orientation:
        return 1
    if faces['right'] == up_orientation:
        return 3
    if faces['up'] == up_orientation:
        return 0
    if faces['down'] == up_orientation:
        return 2
    assert(False, "This should not happen")

def rotate_up():
    global faces
    current_front = faces['front']
    faces['front'] = faces['up']
    faces['up'] = faces['back']
    faces['back'] = faces['down']
    faces['down'] = current_front

def rotate_down():
    global faces
    current_front = faces['front']
    faces['front'] = faces['down']
    faces['down'] = faces['back']
    faces['back'] = faces['up']
    faces['up'] = current_front
    
def rotate_left():
    global faces
    current_front = faces['front']
    faces['front'] = faces['left']
    faces['left'] = faces['back']
    faces['back'] = faces['right']
    faces['right'] = current_front
    
def rotate_right():
    global faces
    current_front = faces['front']
    faces['front'] = faces['right']
    faces['right'] = faces['back']
    faces['back'] = faces['left']
    faces['left'] = current_front

def update_face(operation):
    global cube_faces, absorptions
    
    face = faces['front']
    orientation = get_face_orientation()
    
    for i in range(orientation):
        cube_faces[face] = rotate_ccw(cube_faces[face])
    
    if operation[0] == "FACE":
        value = int(operation[3])
        absorptions[face] += value * grid_size * grid_size
        for i in range(grid_size):
            for j in range(grid_size):
                cube_faces[face][i][j] += value
                while cube_faces[face][i][j] > 100:
                    cube_faces[face][i][j] -= 100
        
    if operation[0] == "COL":
        index = int(operation[1])-1
        value = int(operation[4])
        absorptions[face] += value * grid_size
        for i in range(grid_size):
            cube_faces[face][i][index] += value
            while cube_faces[face][i][index] > 100:
                cube_faces[face][i][index] -= 100
        
    if operation[0] == "ROW":
        index = int(operation[1])-1
        value = int(operation[4])
        absorptions[face] += value * grid_size
        for i in range(grid_size):
            cube_faces[face][index][i] += value
            while cube_faces[face][index][i] > 100:
                cube_faces[face][index][i] -= 100
        
    for i in range(orientation):
        cube_faces[face] = rotate_cw(cube_faces[face])

def dominant_sum(face):
    return max(
        [*[sum([cube_faces[face][i][j] for j in range(grid_size)]) for i in range(grid_size)],
         *[sum([cube_faces[face][j][i] for j in range(grid_size)]) for i in range(grid_size)]]
    )

def extend_row(instruction):
    for _ in range(3):
        rotate_left()
        update_face(instruction)
    rotate_left()

def extend_col(instruction):
    for _ in range(3):
        rotate_up()
        update_face(instruction)
    rotate_up()

def perform(extend=False):
    for inst_idx in range(len(instructions)):
        update_face(instructions[inst_idx])
        
        if extend:
            if instructions[inst_idx][0] == "ROW":
                extend_row(instructions[inst_idx])
            if instructions[inst_idx][0] == "COL":
                extend_col(instructions[inst_idx])
        
        if inst_idx < len(twists):
            if twists[inst_idx] == "U":
                rotate_up()
            if twists[inst_idx] == "D":
                rotate_down()
            if twists[inst_idx] == "L":
                rotate_left()
            if twists[inst_idx] == "R":
                rotate_right()

def part1():
    global absorptions, cube_faces
    cube_faces = [[[1 for _ in range(grid_size)] for _ in range(grid_size)] for _ in range(6)]
    perform()
    absorps = sorted([v for v in absorptions.values()], reverse=True)[:2]
    return absorps[0] * absorps[1]

def part2():
    global cube_faces
    cube_faces = [[[1 for _ in range(grid_size)] for _ in range(grid_size)] for _ in range(6)]
    perform()
    ans = 1
    for f in range(len(cube_faces)):
        ans *= dominant_sum(f)
    return ans

def part3():
    global cube_faces
    cube_faces = [[[1 for _ in range(grid_size)] for _ in range(grid_size)] for _ in range(6)]
    perform(extend=True)
    ans = 1
    for f in range(len(cube_faces)):
        ans *= dominant_sum(f)
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
    
