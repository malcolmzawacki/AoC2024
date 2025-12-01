
def onOpen():
    with open("text/day25.txt") as f:
        text = f.read()
        init_list = list(text.split("\n\n"))
        locks = []
        keys = []
        for str in init_list:
            thing = list(str.split("\n"))
            if '#' in thing[0]:
                locks.append(thing)
            else:
                keys.append(thing)
        lock_vals = []
        for lock in locks:
            lock_val = [-1,-1,-1,-1,-1]
            for lock_row in lock:
                lock_row_list = list(char for char in lock_row)
                for i in range(len(lock_row)):
                    if lock_row_list[i] == '#':
                        lock_val[i]+=1
            lock_vals.append(lock_val)
        
        key_vals = []
        for key in keys:
            key_val = [-1,-1,-1,-1,-1]
            for key_row in key:
                key_row_list = list(char for char in key_row)
                for i in range(len(key_row)):
                    if key_row_list[i] == '#':
                        key_val[i]+=1
            key_vals.append(key_val)          

        fits = 0
        for lock in lock_vals:
            for key in key_vals:
                overlap = False
                for i in range(len(key)):
                    if key[i]+lock[i] > 5:
                        overlap = True
                if overlap == False:
                    fits +=1
        return fits


import datetime
start = datetime.datetime.now()
part1 = onOpen()
print(f"The number of fits is {part1}")


print("Time: "+ str(datetime.datetime.now() - start))