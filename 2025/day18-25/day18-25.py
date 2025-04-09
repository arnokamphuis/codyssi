
# read command-line parameters and based on that read the input file
from collections import defaultdict, deque
import heapq
from math import gcd
import sys
runtype = sys.argv[1]
runpart = int(sys.argv[2])
if len(sys.argv) > 3:
    runs = int(sys.argv[3])
else:
    runs = 1

text_file = open(f"day18-{runtype}.txt", "r")

lines = [line.split() for line in text_file.readlines()]




class KeyAwareDefaultDict(dict):
    """
    A dictionary subclass that calls a factory function with the key
    when a missing key is accessed.
    """
    def __init__(self, factory, *args, **kwargs):
        """
        Initializes the dictionary.

        Args:
            factory: A callable that accepts one argument (the key)
                     and returns the default value for that key.
            *args, **kwargs: Standard dictionary initialization arguments.
        """
        if not callable(factory):
            raise TypeError("first argument must be callable")
        self.factory = factory
        # Initialize the underlying dictionary using standard dict.__init__
        super().__init__(*args, **kwargs)

    def __missing__(self, key):
        """
        Handles missing key access by calling the factory.
        This method is automatically called by dict.__getitem__ (i.e., d[key])
        when 'key' is not found.
        """
        # Call the factory *with* the missing key
        value = self.factory(key)
        # Store the generated value in the dictionary for future access
        self[key] = value
        # Return the generated value
        return value

    # Optional: Improve representation for clarity
    def __repr__(self):
        return f"{type(self).__name__}({self.factory!r}, {super().__repr__()})"

    # Optional: Make copy/deepcopy work correctly if needed
    def __copy__(self):
        return type(self)(self.factory, self)

    def __deepcopy__(self, memo):
        import copy
        return type(self)(self.factory, copy.deepcopy(dict(self), memo))


















rules = [[l[2], int(l[4]), int(l[7]), list(map(int,''.join(l[11:])[1:-1].split(',')))] for l in lines]

max_x = 3
max_y = 3
max_z = 5
min_a = -1
max_a = +1

# 10 by 15 by 60 by 3
max_x = 10
max_y = 15
max_z = 60
# min_a = -1
# max_a = +1


def check_bounds(pos):
    x, y, z, a = pos
    if x < 0 or x >= max_x:
        return False
    if y < 0 or y >= max_y:
        return False
    if z < 0 or z >= max_z:
        return False
    if a < min_a or a > max_a:
        return False
    return True

def calculate_rule(rule, divide, remainder, position):
    coefs = list(map(int,[r[:-1] for r in rule.split('+')]))
    # print(f'{coefs=}, {position=}, {divide=}, {remainder=}, {sum([c*p for (c,p) in zip(coefs, position)])} % {divide} == {remainder}')
    return (sum((c*p for (c,p) in zip(coefs, position))) % divide == remainder)

def determine_debris(rules):
    debris = defaultdict(list)
    counter = [0] * len(rules)
    for r_id, rule in enumerate(rules):
        for x in range(max_x):
            for y in range(max_y):
                for z in range(max_z):
                    for a in range(min_a, max_a+1):
                        position = (x, y, z, a)
                        if calculate_rule(rule[0], rule[1], rule[2], position):
                            # print(f'{position=}, {rule[3]=}')
                            debris[position].append(tuple(rule[3]))
                            counter[r_id] += 1
    return debris, counter    

def part1():
    _, counter = determine_debris(rules)
    return sum(counter)

def check_debris(debris, position):
    if position != (0, 0, 0, 0):
        if position in debris:
            return True
    return False

def get_in_bounds(x, low, high, period):
    while x < low:
        x += period
    while x > high:
        x -= period
    return x

def get_debris(t, debris):
    print(f'{t=}')
    ans = set()    
    for pos, velocities in debris.items():
        for vel in velocities:
            pos_at_t = (get_in_bounds(pos[0] + t * vel[0], 0, max_x-1, max_x),
                get_in_bounds(pos[1] + t * vel[1], 0, max_y-1, max_y),
                get_in_bounds(pos[2] + t * vel[2], 0, max_z-1, max_z),
                get_in_bounds(pos[3] + t * vel[3], min_a, max_a, max_a - min_a + 1))
            ans.add(pos_at_t)
    return ans

def get_neighbours(position):
    deltas = [
        (-1, 0, 0, 0), (1, 0, 0, 0),
        (0, -1, 0, 0), (0, 1, 0, 0), 
        (0, 0, -1, 0), (0, 0, 1, 0), 
        # (0, 0, 0, -1), (0, 0, 0, 1), 
        (0, 0, 0, 0) 
    ]
    
    neighbours = []
    for delta in deltas:
        new_pos = (position[0] + delta[0], position[1] + delta[1], position[2] + delta[2], position[3] + delta[3])
        if check_bounds(new_pos):
            neighbours.append(new_pos)
    return neighbours
    

def part2():
    debris, _ = determine_debris(rules)
    
    velocities = defaultdict(set)
    for pos, vels in debris.items():
        for vel in vels:
            velocities[vel].add(pos)
    
    current = (0, 0, 0, 0)
    target  = (max_x-1, max_y-1, max_z-1, 0)
    result = None
    
    q = deque()
    q.append((0, current))
    visited = set()
    while q:
        t, position = q.popleft()
        # print(f'{t=}, {position=}, {len(q)=}')
        if (t,position) in visited:
            continue
        visited.add((t, position))
        
        hit_by_debris = False
        for vel, positions in velocities.items():
            orig_pos = (
                get_in_bounds(position[0]-t*vel[0], 0, max_x-1, max_x), 
                get_in_bounds(position[1]-t*vel[1], 0, max_y-1, max_y),
                get_in_bounds(position[2]-t*vel[2], 0, max_z-1, max_z),
                get_in_bounds(position[3]-t*vel[3], min_a, max_a, max_a - min_a + 1)
            )
            if orig_pos in positions:
                hit_by_debris = True
                break
        if hit_by_debris and position != (0,0,0,0):
            continue

        if position == target:
            result = t
            break

        for neighbour in get_neighbours(position):
            q.append((t+1, neighbour))
        
    return result

def part3():
    debris, _ = determine_debris(rules)
    
    def find_velocity_count(pos, position_count):
        for pc in position_count:
            if pc[0] == pos:
                return pc[1]
        return 0
    
    velocities = KeyAwareDefaultDict(lambda x: defaultdict(int))
    for pos, vels in debris.items():
        for vel in vels:
            velocities[vel][pos] += 1
    
    current = (0, 0, 0, 0)
    target  = (max_x-1, max_y-1, max_z-1, 0)
    result = None
    max_hits = 3
    
    q = []
    heapq.heappush(q, (0, 0, current))
    visited = set()
    while len(q) > 0:
        t, hits, position = heapq.heappop(q)

        if (t,position) in visited:
            continue
        visited.add((t, position))
        
        hit_by_debris = 0
        for vel in velocities.keys():
            orig_pos = (
                get_in_bounds(position[0]-t*vel[0], 0, max_x-1, max_x), 
                get_in_bounds(position[1]-t*vel[1], 0, max_y-1, max_y),
                get_in_bounds(position[2]-t*vel[2], 0, max_z-1, max_z),
                get_in_bounds(position[3]-t*vel[3], min_a, max_a, max_a - min_a + 1)
            )
            debris_count = velocities[vel][orig_pos]
            if debris_count > 0:
                hit_by_debris += debris_count
        if position != (0,0,0,0):
            hits += hit_by_debris
        if hits > max_hits:
            continue

        if position == target:
            result = t
            break

        for neighbour in get_neighbours(position):
            q.append((t+1, hits, neighbour))
        
    return result

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
    
