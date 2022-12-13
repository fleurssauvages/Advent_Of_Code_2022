#!/usr/bin/env python
import numpy as np
import json

def compare(left, right):
    if type(left) is int and type(right) is int:
        return left - right
    elif type(left) is not int and type(right) is int:
        return compare(left, [right])
    elif type(left) is int and type(right) is not int:
        return compare([left], right)
    
    for leftElement, rightElement in zip(left, right):
        difference = compare(leftElement, rightElement)
        if difference != 0:
            return difference
    
    return len(left) - len(right)
    
f = open("ressources/day13.txt", "r")
lines = f.readlines()

inRightOrder = []

for i in range(0, len(lines), 3):
    firstLine = json.loads(lines[i])
    secondLine = json.loads(lines[i+1])
    
    result = compare(firstLine, secondLine)
    if result <= 0:
        inRightOrder.append(i//3+1)
            
print("Number of correct packets is: {}".format(sum(inRightOrder)))

listOfPackets = []
for i in range(0, len(lines), 3):
    firstLine = json.loads(lines[i])
    secondLine = json.loads(lines[i+1])
    listOfPackets.append(firstLine)
    listOfPackets.append(secondLine)

organizedPackets = [listOfPackets.pop()]

while len(listOfPackets)> 0:
    elementToOrganize = listOfPackets.pop()
    idx = 0
    isEnd = False
    while compare(organizedPackets[idx], elementToOrganize) < 0:
        idx += 1
        if idx >= len(organizedPackets):
            isEnd = True
            break
    if isEnd:
        organizedPackets.append(elementToOrganize)
    else:
        organizedPackets.insert(idx, elementToOrganize)

idx2 = 0
while compare(organizedPackets[idx2], [[2]]) < 0:
    idx2 += 1
organizedPackets.insert(idx2, elementToOrganize)

idx6 = 0
while compare(organizedPackets[idx6], [[6]]) < 0:
    idx6 += 1
organizedPackets.insert(idx2, elementToOrganize)

print("Signal emergency is: {}".format((idx2+1)*(idx6+1)))