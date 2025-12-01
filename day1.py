import math

f = open('day1.txt')
text = f.read()
text = text.split('\n')

turns = []
dial = 50
zeroes = 0
zeroes_pt2 = 0

for line in text:
    line = list(line)
    if line[0] == "L":
        line[0] = -1
    else:
        line[0] = 1
    turn = 0
    for i in range(1,len(line)):
        val = int(line[i])
        turn = 10*turn + val
    turn *= line[0]
    dial += turn
    dial = dial%100
    if dial == 0:
        zeroes += 1

    turns.append(turn)

print(zeroes)

dial = 50
current_rotations = 0
for turn in turns:
    to_add = 0
    turned = dial + turn
    if turned < 0 < dial: # i was counting times when the marker was on zero and went left, which doesnt count
        to_add = 1 + abs(math.ceil(turned/100))
        
    if turned >= 100:
        to_add = turned//100

    if turned == 0:
        to_add = 1
    if to_add > 1:
        print(f"A turn of {turn} has taken dial from {dial} to {turned}, resulting in {to_add} rotations")
    zeroes_pt2 += to_add
    dial = turned%100

print(zeroes_pt2)

