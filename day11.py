"""If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
If the stone is engraved with a number that has an even number of digits, it is replaced by two stones; 
    The left half of the digits are engraved on the new left stone, 
    and the right half of the digits are engraved on the new right stone. 
    (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone; 
the old stone's number multiplied by 2024 is engraved on the new stone."""

def if_zero(num):
    num = 1
    return num

def even_check(num):
    num = str(num)
    if len(num)%2 != 0:
        return False
    else:
        powers = (len(num)/2)
        num = int(num)
        a = int(num // (10**powers))
        b = int(num - a*(10**powers))
    return a, b

def oh_well(num):
    num = num*2024
    return num

def onOpen():
    with open("text/day11.txt") as f:
        text = f.read()
        text= "17639 47 3858 0 470624 9467423 5 188"
        init_list = blink(list(map(int,text.split(" "))),25)
        return len(init_list)

def construct_new_list(init_list):
    new_list = list()
    for num in init_list:
        if num == 0:
            new_list.append(1)
        elif even_check(num) != False:
            a, b = even_check(num)
            new_list.append(a)
            new_list.append(b)
        else:
            new_list.append(num*2024)
    return new_list

def blink(init_list,blinks):
    i = 0
    while i < blinks:
        init_list = construct_new_list(init_list)
        i+=1
    return init_list


"""okay time to be smart for part 2 lol. maybe i can just count how often a number comes up?
Like, for 0, it becomes 1, then 2024, then 20 and 24, and then 2 0 2 4! so right there, it reproduces itself, yknow?
It will, whenever encountered, produce itself and 3 other numbers (2 unique other numbers). 
so it adds a specific amount of numbers to the sequence after a reliable number of steps. how would i leverage that?
cuz like, okay, i would need to look up what 0 does, but if I also knew that 2 and 4 lead back to themselves? idk.
still feels inefficient. how would i count occurences, too?

what if i stopped running the loop when the loop contains the starting number? ehhh are all numbers guaranteed to contain themselves?
"""

import datetime
start = datetime.datetime.now()
part1 = onOpen()
print(f"Length of List after 25 blinks is {part1}")


print("Time: "+ str(datetime.datetime.now() - start))