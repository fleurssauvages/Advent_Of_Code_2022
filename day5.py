#!/usr/bin/env python

stack0 = ['V','J', 'B', 'D']
stack1 = ['F','D', 'R', 'W', 'B', 'V', 'P']
stack2 = ['Q', 'W', 'C', 'D', 'L', 'F', 'G', 'K']
stack3 = ['B', 'D', 'N', 'L', 'M', 'P', 'J', 'W']
stack4 = ['Q', 'S', 'C', 'P', 'B', 'N', 'H']
stack5 = ['G', 'N', 'S', 'B', 'D', 'R']
stack6 = ['H','S', 'F', 'Q', 'M', 'P', 'B', 'Z']
stack7 = ['F','L', 'W']
stack8 = ['R','M', 'F', 'V', 'S']

stacks = [stack0,stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8]
for stack in stacks:
    stack.reverse()

f = open("ressources/day5.txt", "r")
lines = f.readlines()

for line in lines[10:]:
    instructions = line.replace("\n", "").split(" ")
    nbToMove = int(instructions[1])
    fromWhere = int(instructions[3])-1
    toWhere = int(instructions[5])-1
    for i in range(nbToMove):
        item = stacks[fromWhere].pop()
        stacks[toWhere].append(item)
        
word = ""
for stack in stacks:
    word+=stack[-1]
    
print("Your Final Stack is: {}".format(word))

stack0 = ['V','J', 'B', 'D']
stack1 = ['F','D', 'R', 'W', 'B', 'V', 'P']
stack2 = ['Q', 'W', 'C', 'D', 'L', 'F', 'G', 'K']
stack3 = ['B', 'D', 'N', 'L', 'M', 'P', 'J', 'W']
stack4 = ['Q', 'S', 'C', 'P', 'B', 'N', 'H']
stack5 = ['G', 'N', 'S', 'B', 'D', 'R']
stack6 = ['H','S', 'F', 'Q', 'M', 'P', 'B', 'Z']
stack7 = ['F','L', 'W']
stack8 = ['R','M', 'F', 'V', 'S']

stacks = [stack0,stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8]

for line in lines[10:]:
    instructions = line.replace("\n", "").split(" ")
    nbToMove = int(instructions[1])
    fromWhere = int(instructions[3])-1
    toWhere = int(instructions[5])-1
    
    items = stacks[fromWhere][0:nbToMove]
    stacks[fromWhere] = stacks[fromWhere][nbToMove:]
    stacks[toWhere] = items+stacks[toWhere]
    
word = ""
for stack in stacks:
    word+=stack[0]
    
print("Your Final Stack is: {}".format(word))