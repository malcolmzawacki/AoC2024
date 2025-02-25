"""In particular, each buyer's secret number evolves into the next secret number in the sequence via the following process:

Calculate the result of multiplying the secret number by 64. 
Then, mix this result into the secret number. 
Finally, prune the secret number."""

def step_one(secret):
    result = secret*64
    to_prune = mix(result,secret)
    pruned = prune(to_prune)
    return pruned


"""Calculate the result of dividing the secret number by 32. 
Round the result down to the nearest integer. 
Then, mix this result into the secret number. 
Finally, prune the secret number."""

def step_two(secret):
    result = secret//32
    to_prune = mix(result,secret)
    pruned = prune(to_prune)
    return pruned

"""Calculate the result of multiplying the secret number by 2048. 
Then, mix this result into the secret number. Finally, prune the secret number."""

def step_three(secret):
    result = secret*2048
    to_prune = mix(result,secret)
    pruned = prune(to_prune)
    return pruned
    
def nested(secret):
    nested1 = prune(mix(secret*64,secret))
    nested2 = prune(mix(nested1//32,nested1))
    nested3 = prune( mix(nested2*2048,nested2))
    return nested3

"""Each step of the above process involves mixing and pruning:
To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. 
Then, the secret number becomes the result of that operation. 
(If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
To prune the secret number, calculate the value of the secret number modulo 16777216. 
Then, the secret number becomes the result of that operation. 
(If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
"""
def mix(val1,val2):
    mixed = val1^val2
    return mixed
def prune(secret):
    pruned = secret%16777216
    return pruned

def iterate(init_val):
    loops = 2000
    i = 1
    while i <= loops:
        init_val = nested(init_val)
        i+=1
    return init_val

def sum(init_val_list):
    sum = 0
    for i in range(len(init_val_list)):
        init_val = int(init_val_list[i])
        sum+=iterate(init_val)

    return sum


def onOpen():
    with open("text/day22.txt") as f:
        text = f.read()
        init_val_list = text.splitlines()
        total = sum(init_val_list)
    return total

import datetime
start = datetime.datetime.now()

print(f"The total is {onOpen()}")

print("Time: "+ str(datetime.datetime.now() - start))