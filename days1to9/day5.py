# # # timing # # #
import datetime
start = datetime.datetime.now()

# # # file handing # # #
f = open("text/day5.txt")
text = f.read()
x = text.rsplit("\n")
x.remove('')
page_orders = [] # rules about pages
updates = [] # sequences of page numbers
for i in range(len(x)):
    if x[i].count("|") > 0:
        front = x[i].split("|")[0]
        back = [x[i].split("|")[1]]
        page_orders.append([front,back])
    else:
        updates.append(x[i].split(","))

# # # filtering repeats # # #
# sorting by leading number (must come before)
page_orders = sorted(page_orders, reverse = True, key=lambda x: x[0])
# counting repeats for range limits
count = 0
for i in range(len(page_orders)-1):
    if page_orders[i][0] == page_orders[i+1][0]:
       count+=1
# true number of iterations = unique numbers
b = len(page_orders) - count - 1

i = 0
tempArray = []
while i < b:
    tempArray.append(page_orders[i][0]) # add leading term to tempArray
    while page_orders[i][0] == page_orders[i+1][0]:
        page_orders[i][1].append(page_orders[i+1][1][0]) # add trailing term from repeat to lead's array
        page_orders.remove(page_orders[i+1]) # remove repeat leading term array
    if not page_orders[i][0] == page_orders[i+1][0]: # if the next leading term is different
        tempArray.append(page_orders[i][1]) # add the full trailing array to tempArray
        if i == b - 1: # if this is the last leading term, just add both lead and trailing array
            tempArray.append(page_orders[i+1][0])
            tempArray.append(page_orders[i+1][1])
    i+=1
# reset filtered pages
page_orders = tempArray


# # # separating leads from trails (this probably could be combined with above at some point) # # #
pages = [] # leading terms
behind = [] # trailing term array
for i in range(len(page_orders)//2): # these are 'pairs' so only need half length
    pages.append(page_orders[2*i])
    behind.append(page_orders[2*i + 1]) 

# edge cases : number that will show up in sequences but have no designated trails
for i in range(len(behind)):
    for a in behind[i]:
        if a not in pages:
            pages.append(a) # add it to leading terms
            behind.append(['0']) # but give it no valid trailing terms

# # # F I N A L L Y analyzing # # #
sum = 0
i = 0
valid = 0
broke = 1 # index for part 2
part2 = []
while i < len(updates):
    part2.append(updates[i])
    add = int(updates[i][len(updates[i])//2]) # potential middle term, if sequence valid
    j=len(updates[i]) - 1 # working from back to check for trails in front of lead
    while j > 0:
        currentLead = str(updates[i][j]) # last term in sequence
        updates[i].pop(updates[i].index(currentLead)) # removes the last number from the list
        check = behind[pages.index(currentLead)] #grabs the numbers that CANNOT be in front of current last
        overlap = set(updates[i]) & set(check) # should be empty, no 'trailing' terms in front of lead
        if not overlap == set(): # if it isn't empty
            j = 0 # this sequence is bad, go to the next one
            broke += 1 # index for part 2, permanently added to
        elif j == 1: # if the second to last term passed, we good
            sum+= add
            valid+=1
            part2.remove(part2[broke-1])
        j-=1
    i+=1

print("Total: " + str(sum))
print()
print("Out of " + str(len(updates)) + " sequences, " + str(valid) + " were valid")
print()
part1time = datetime.datetime.now()
print("Part 1 Time: "+ str( datetime.datetime.now() - start))

# # # Part 2 # # #
# starts out similarly
i = 0
sum = 0
part2check = []
while i < len(part2):
    j = len(part2[i]) - 1
    newUpdate = [] # new home for sorted update
    while j > 0:
        currentLead = str(part2[i][j]) # last term in sequence
        tempindex = part2[i].index(currentLead)
        part2[i].pop(tempindex)
        check = behind[pages.index(currentLead)] #grabs the numbers that CANNOT be in front of current last
        overlap = set(part2[i]) & set(check)
        if overlap == set(): # if this number has no issues, put it in the order it was removed
            newUpdate.insert(0,currentLead)
            j-=1
        else: # put currentLead in front
            part2[i].insert(0,currentLead)
            j = len(part2[i]) - 1 # and start over
    sum += int(newUpdate[len(newUpdate)//2])
    part2check.append(newUpdate)
    i+=1

part2time = datetime.datetime.now() - part1time
print("Part 2 Time: "+ str(part2time))
print(sum)

i = 0
valid = 0
sum = 0
while i < len(part2check):
    add = int(part2check[i][len(part2check[i])//2]) # potential middle term, if sequence valid
    j=len(part2check[i]) - 1 # working from back to check for trails in front of lead
    while j > 0:
        currentLead = str(part2check[i][j]) # last term in sequence
        part2check[i].pop(part2check[i].index(currentLead)) # removes the last number from the list
        check = behind[pages.index(currentLead)] #grabs the numbers that CANNOT be in front of current last
        overlap = set(part2check[i]) & set(check) # should be empty, no 'trailing' terms in front of lead
        if not overlap == set(): # if it isn't empty
            j = 0 # this sequence is bad, go to the next one
        elif j == 1: # if the second to last term passed, we good
            sum+= add
            valid+=1
        j-=1
    i+=1

print("Total: " + str(sum))
print()
print("Out of " + str(len(part2check)) + " sequences, " + str(valid) + " were valid")
print()
print("Time: "+ str(datetime.datetime.now() - start))

