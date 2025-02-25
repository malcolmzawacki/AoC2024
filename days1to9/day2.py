# open file
import datetime
start = datetime.datetime.now()
f = open("text/day2.txt")

#format into list
lines = [line.strip() for line in f]
lines = [line.split() for line in lines]

# look for too big of a gap
def distanceTest(array):
    if max(array) < 4 and min(array) > -4:
        return True
    else: # if there's more than one too big jump?
        return False

# movement up or down
def signTest(array):
    increasing = 0
    zero = 0
    decreasing = 0
    for i in range(0,len(array)-1):
        if int(array[i]) < int(array[i+1]):
            increasing +=1
        elif int(array[i]) > int(array[i+1]):
            decreasing +=1
        elif int(array[i]) == int(array[i+1]):
            zero +=1
    signTest = [increasing, zero, decreasing]
    return signTest
# if theres 2 up and 2 down, removing one cannot fix things
# in fact, if there's two zeroes too, that would make it unfixable

# create difference array
def difference(array):
    diffArray = []
    for i in range(0,len(array)):
        subArray = []
        for j in range(0,len(array[i]) - 1):
            subArray.append(int(array[i][j+1]) - int(array[i][j]))
        diffArray.append(subArray)
    return diffArray

def minidifference(array):
    miniArray = []
    for i in range(0, len(array) -1):
        miniArray.append(int(array[i+1]) - int(array[i]))
    return miniArray
        
        
# part 1 solution
count = 0
passOneArray = []
diffArray = difference(lines)
i = 0
while i < len(diffArray):
    sign = signTest(lines[i])
    if distanceTest(diffArray[i]) == True and sign[1] == 0 and (sign[0] == 0 or sign[2] == 0):
        count+=1
    else:
        passOneArray.append(lines[i])
    i +=1
print("First Pass")
print("Definite working " + str(count))
print("Potentially fixable " + str(len(passOneArray)))
print()

i = 0
while i < len(passOneArray):
    j = 0
    blah2 = passOneArray[i]
    while j < len(passOneArray[i]):
        blah = blah2
        x = blah.pop(j)
        testArray = blah
        sign = signTest(testArray)
        if distanceTest(minidifference(testArray)) == True and sign[1] == 0 and (sign[0] == 0 or sign[2] == 0):
            count+=1
            j = len(passOneArray[i])
        else:
            blah.insert(int(j),int(x))
            j+=1
    i+=1

print("Final working " + str(count))

print("Time: "+ str(datetime.datetime.now() - start))