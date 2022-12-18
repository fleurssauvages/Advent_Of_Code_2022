#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def moveOne(starting, map):
    if map[starting[0], starting[1]-1] == 0:
        return [starting[0], starting[1]-1]
    elif map[starting[0], starting[1]-1] > 0:
        if map[starting[0]-1, starting[1]-1] == 0:
            return [starting[0]-1, starting[1]-1]
        elif map[starting[0]+1, starting[1]-1] == 0:
            return [starting[0]+1, starting[1]-1]
    return starting

def move(starting, map):
    ending = moveOne(starting, map)
    while ending != starting:
        starting = ending
        ending = moveOne(starting, map)
        if ending[1] < 2:
            return ending
    return ending

f = open("ressources/day14.txt", "r")
lines = f.readlines()

sizeX = 200
sizeY = 200
map = np.zeros((sizeX,sizeY))

for line in lines:
    path = line.replace("\n", "").split("->")
    instructions = []
    for item in path:
        coordinates = item.split(",")
        x = coordinates[0]
        y = coordinates[1]
        instructions.append([int(x),int(y)])
    for i in range(1,len(instructions)):
        lineStartX = instructions[i-1][0]
        lineEndX = instructions[i][0]
        
        if lineStartX > lineEndX:
            lineStartX, lineEndX = lineEndX, lineStartX
        
        lineStartY = instructions[i-1][1]+1
        lineEndY = instructions[i][1]+1
        
        if lineStartY < lineEndY:
            lineStartY, lineEndY = lineEndY, lineStartY
        
        if lineStartX != lineEndX:
            map[lineStartX-500+sizeX//2:lineEndX-500+sizeX//2+1, sizeY-lineStartY] = 1
        elif lineStartY != lineEndY:
            map[lineStartX-500+sizeX//2, sizeY-lineStartY:sizeY-lineEndY+1] = 1

plt.imshow(255-np.flip(np.transpose(map), axis=0)*120, cmap='gray', vmin=0, vmax=255)
plt.show()

sandStart = [sizeX//2, sizeY]

nbSand = 0
while True:
    sandPosition = move(sandStart, map)
    map[sandPosition[0], sandPosition[1]] = 2
    nbSand += 1
    if sandPosition[1] < 2:
        break
    
print("Number of sand falling before the abyss: {}".format(nbSand-1))
plt.imshow(255-np.flip(np.transpose(map), axis=0)*120, cmap='gray', vmin=0, vmax=255)
plt.show()

sizeX = 500
sizeY = 200
map = np.zeros((sizeX,sizeY))
map = np.zeros((sizeX,sizeY))

for line in lines:
    path = line.replace("\n", "").split("->")
    instructions = []
    for item in path:
        coordinates = item.split(",")
        x = coordinates[0]
        y = coordinates[1]
        instructions.append([int(x),int(y)])
    for i in range(1,len(instructions)):
        lineStartX = instructions[i-1][0]
        lineEndX = instructions[i][0]
        
        if lineStartX > lineEndX:
            lineStartX, lineEndX = lineEndX, lineStartX
        
        lineStartY = instructions[i-1][1]+1
        lineEndY = instructions[i][1]+1
        
        if lineStartY < lineEndY:
            lineStartY, lineEndY = lineEndY, lineStartY
        
        if lineStartX != lineEndX:
            map[lineStartX-500+sizeX//2:lineEndX-500+sizeX//2+1, sizeY-lineStartY] = 1
        elif lineStartY != lineEndY:
            map[lineStartX-500+sizeX//2, sizeY-lineStartY:sizeY-lineEndY+1] = 1

floorlevel = np.amax(sizeY-np.argwhere(map>0)[:,1])
map[:, sizeY-floorlevel-2] = 1
sandStart = [sizeX//2, sizeY]

nbSand = 0
while True:
    sandPosition = move(sandStart, map)
    map[sandPosition[0], sandPosition[1]] = 2
    nbSand += 1
    if sandPosition[1] == sizeY-1:
        break

print("Number of sand before reaching the top: {}".format(nbSand))
plt.imshow(255-np.flip(np.transpose(map), axis=0)*120, cmap='gray', vmin=0, vmax=255)
plt.show()