#!/usr/bin/env python
import numpy as np

f = open("ressources/day10.txt", "r")
lines = f.readlines()

nbCycle = [0]
listToAdd = [1]

for line in lines:
    instructions = line.replace("\n", "").split(" ")
    command = instructions[0]
    if command == "noop":
        listToAdd.append(0)
        nbCycle.append(1)
    if command == "addx":
        numberToAdd = int(instructions[1])
        nbCycle.append(1)
        listToAdd.append(0)
        nbCycle.append(1)
        listToAdd.append(numberToAdd)

cycleList = np.cumsum(nbCycle)
registerAtCycle = np.cumsum(listToAdd)
signalPower = 0

for i in [20,60,100,140,180,220]:
    index_i = np.argwhere(cycleList == i-1)
    signalPower += i * registerAtCycle[index_i][0][0]

print("Signal strength is: {}".format(signalPower))

drawing = ""
for i in range(0,240):
    index_i = np.argwhere(cycleList == i)
    value = registerAtCycle[index_i][0][0]

    if i%40 in [value-1, value, value+1]:
        drawing += "#"
    else:
        drawing += "."

print("Line is: {}".format(drawing[0:40]))
print("Line is: {}".format(drawing[40:80]))
print("Line is: {}".format(drawing[80:120]))
print("Line is: {}".format(drawing[120:160]))
print("Line is: {}".format(drawing[160:200]))
print("Line is: {}".format(drawing[200:240]))