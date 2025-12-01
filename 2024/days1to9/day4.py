# min of 26 lines
import datetime
start = datetime.datetime.now()

f = open("text/day4.txt")
text = f.read()
x = text.rsplit("\n")
rows = len(x)
cols = len(x[0])
count = 0

for i in range(0,rows):
    for j in range(0,cols):
        up, down, left, right = i >= 3, i < rows - 3, j >= 3, j < cols - 3
        if down and x[i][j] == "X" and x[i+1][j] == "M" and x[i+2][j] == "A" and x[i+3][j] == "S":
            count +=1 # down
        if right and x[i][j] == "X" and x[i][j+1] == "M" and x[i][j+2] == "A" and x[i][j+3] == "S":
            count+=1 # right
        if left and x[i][j] == "X" and x[i][j-1] == "M" and x[i][j-2] == "A" and x[i][j-3] == "S":
            count+=1 # left
        if up and x[i][j] == "X" and x[i-1][j] == "M" and x[i-2][j] == "A" and x[i-3][j] == "S":
            count +=1 # up
        if up and right and x[i][j] == "X" and x[i-1][j+1] == "M" and x[i-2][j+2] == "A" and x[i-3][j+3] == "S":
            count +=1 # up and right
        if up and left and x[i][j] == "X" and x[i-1][j-1] == "M" and x[i-2][j-2] == "A" and x[i-3][j-3] == "S":
            count +=1 # up and left
        if down and right and x[i][j] == "X" and x[i+1][j+1] == "M" and x[i+2][j+2] == "A" and x[i+3][j+3] == "S":
            count +=1 # down and right
        if down and left and x[i][j] == "X" and x[i+1][j-1] == "M" and x[i+2][j-2] == "A" and x[i+3][j-3] == "S":
            count +=1 # down and left
print(count)
print()
print("Time: "+ str(datetime.datetime.now() - start))
# 0.023 seconds

# part 2

import datetime
start = datetime.datetime.now()
xmas = 0

def msams(array,rowStart,rowEnd,colStart,colEnd):
    count = 0
    for i in range(rowStart,rowEnd):
        for j in range(colStart,colEnd):
            if array[i][j] == "A" and \
            ((array[i-1][j-1] == "M" and array[i+1][j-1] == "M" and \
            array[i+1][j+1] == "S" and array[i-1][j+1] == "S") or \
            (array[i-1][j-1] == "M" and array[i-1][j+1] == "M" and \
            array[i+1][j+1] == "S" and array[i+1][j-1] == "S") or \
            (array[i-1][j+1] == "M" and array[i+1][j+1] == "M" and \
            array[i+1][j-1] == "S" and array[i-1][j-1] == "S") or \
            (array[i-1][j-1] == "S" and array[i-1][j+1] == "S" and \
            array[i+1][j+1] == "M" and array[i+1][j-1] == "M")):
                count+=1
    return count

xmas+=msams(x, 1,len(x)-1,1,len(x[0])-1)

print(xmas)
print("Time: "+ str(datetime.datetime.now() - start))