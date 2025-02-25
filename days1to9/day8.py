import datetime
import math
start = datetime.datetime.now()

def grid(text_lines):
    rows = len(text_lines)
    cols = len(text_lines[0])
    return rows,cols

def construct_antenna_dict(text_lines):
    antenna_dict = {}
    for i in range(len(text_lines)):
        for j in range(len(text_lines[i])):
            char = text_lines[i][j]
            if char.isalnum():
                if char not in antenna_dict:
                    antenna_dict[char] = [(i,j)]
                else:
                    antenna_dict[char].append((i,j))
    return antenna_dict

def antinode_ID(rows,cols,antenna_dict):
    antinode_set = set()
    resonant_set = set()
    for entry in antenna_dict.keys():
        tuples = antenna_dict[entry]
        for tuple1 in tuples:
            for tuple2 in tuples:
                if tuple1 != tuple2:
                    dx = tuple2[0] - tuple1[0]
                    dy = tuple2[1] - tuple1[1]
                    if (0<=tuple1[0]+dx<rows and 0<=tuple1[1]+dy<cols):
                        antinode_set.add((tuple1[0]+dx,tuple1[1]+dy))
                    if (0<=tuple2[0]-dx<rows and 0<=tuple2[1]-dy<cols):
                        antinode_set.add((tuple2[0]-dx,tuple2[1]-dy))
                    gcd = math.gcd(abs(dx), abs(dy))
                    step_x = dx // gcd
                    step_y = dy // gcd
                    current = tuple1
                    while 0 <= current[0] < rows and 0 <= current[1] < cols:
                        resonant_set.add(current)
                        current = (current[0] + step_x, current[1] + step_y)
                    current = (tuple1[0] - step_x, tuple1[1] - step_y)
                    while 0 <= current[0] < rows and 0 <= current[1] < cols:
                        resonant_set.add(current)
                        current = (current[0] - step_x, current[1] - step_y)
    return len(antinode_set),len(resonant_set)

def onOpen():
    with open("text/day8.txt") as f:
        text_lines = f.read().splitlines()
    rows, cols = grid(text_lines)
    antenna_dict = construct_antenna_dict(text_lines)
    antinode_count,resonant_count =  antinode_ID(rows,cols,antenna_dict)
    return antinode_count, resonant_count

antinode_count, resonant_count = onOpen()
print(antinode_count)
print(resonant_count)
print("Time: "+ str(datetime.datetime.now() - start))