import datetime
#print(registers)
#print(program)
def instructions(opcode,operand,combo_dictionary,registers,pointer,output):
    if opcode == 0:
        #print("adv")
        registers[0] = registers[0]//(2**combo_dictionary.get(str(operand)))
        combo_dictionary.update({"4":registers[0]})
        pointer +=2
    elif opcode == 1:
       # print("bxl")
        registers[1] = registers[1]^operand
        combo_dictionary.update({"5":registers[1]})
        pointer +=2
    elif opcode == 2:
        #print("bst")
        registers[1] = combo_dictionary.get(str(operand))%8
        combo_dictionary.update({"5":registers[1]})
        pointer +=2
    elif opcode == 3:
       # print("jnz")
        if registers[0] == 0:
            pointer+=2
        else:
            pointer = operand
    elif opcode == 4:
        #print("bxc")
        registers[1] = registers[1]^registers[2]
        combo_dictionary.update({"5":registers[1]})
        pointer+=2
    elif opcode == 5:
        #print("out")
        #print(operand)
        #print(combo_dictionary.get(str(operand)))
        output.append(combo_dictionary.get(str(operand)) % 8)
        #print(output)
        pointer+=2
    elif opcode == 6:
        #print("bdv")
        registers[1] = registers[0]//(2**combo_dictionary.get(str(operand)))
        combo_dictionary.update({"5":registers[1]})
        pointer +=2
    elif opcode == 7:
        #print("cdv")
        registers[2] = registers[0]//(2**combo_dictionary.get(str(operand)))
        combo_dictionary.update({"6":registers[2]})
        pointer +=2
    return pointer,registers,output,combo_dictionary
        
#print(combo_dictionary.get("4"))
def opcodes(program,registers,combo_dictionary,output):
    pointer = 0
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        pointer,registers,output, combo_dictionary = instructions(opcode,operand,combo_dictionary,registers,pointer,output)
        #print(registers)
    return output

start = datetime.datetime.now()
text = open("text/day17.txt").read()     
registers, program = text.split("\n\n")
program = list(map(int,program.split(": ")[1].split(",")))
regVals = []
registers=registers.split("\n")
for line in registers:
    a = line.split(": ")[1]
    regVals.append(int(a))
registers = regVals
combo_dictionary = {"0":0,"1":1,"2":2,"3":3,"4":registers[0],"5":registers[1],"6":registers[2]}

output = []
answer = opcodes(program,registers,combo_dictionary,output)
print(answer)
#print(registers[0])
print("Time: "+ str(datetime.datetime.now() - start))
print(program)