#!/usr/bin/env python
import numpy as np
from collections import defaultdict

blizzards = {'<':(0, -1), '>':(0, 1), '^':(-1, 0) ,'v':(1, 0)}

f = open("ressources/day24.txt", "r")
lines = f.readlines()

blizzardMap = []
for line in lines:
    mapLine = line.replace("\n", "")
    blizzardMap.append(list(mapLine))

blizzardSet = set()
fullGrid = set()

height = 0
width = 0

for i, blizzardLine in enumerate(blizzardMap[1:-1]):
    for j, blizzardItem in enumerate(blizzardLine[1:-1]):
        if blizzardItem in blizzards.keys():
            blizzardSet.add(((i,j), blizzards[blizzardItem]))
        fullGrid.add((i, j))
        height = max(height, i+1)
        width = max(width, j+1)

startPoint, endPoint = (-1, 0), (height, width-1)
fullGrid.add(startPoint)
fullGrid.add(endPoint)

def moveBlizzards(fullGrid, blizzardSet, width, height):
    newBlizzardSet = set()
    for blizzardItem in blizzardSet:
        (i, j), (windI, windJ) = blizzardItem
        newI, newJ = (i + windI) % height, (j + windJ) % width
        newBlizzardSet.add(((newI,newJ), (windI, windJ)))
    freeCoordinates = fullGrid - set(blizzardItem[0] for blizzardItem in blizzardSet)
    return newBlizzardSet, freeCoordinates

presentPoints = set()
presentPoints.add(startPoint)

def step(presentPoints, freeCoordinates):
    exploration = [(1,0), (-1,0), (0,1), (0,-1), (0,0)]
    endPoints = set()
    for point in presentPoints:
        for direction in exploration:
            newPoint = (point[0]+direction[0], point[1]+direction[1])
            if newPoint in freeCoordinates and newPoint not in endPoints:
                endPoints.add(newPoint)
    return endPoints

time = -1
while True:
    blizzardSet, freeCoordinates = moveBlizzards(fullGrid, blizzardSet, width, height)
    presentPoints = step(presentPoints, freeCoordinates)
    time += 1
    if endPoint in presentPoints:
        break

print("Time to reach the end is: {}".format(time))

endPoint, startPoint = (-1, 0), (height, width-1)
presentPoints = set()
presentPoints.add(startPoint)
while True:
    blizzardSet, freeCoordinates = moveBlizzards(fullGrid, blizzardSet, width, height)
    presentPoints = step(presentPoints, freeCoordinates)
    time += 1
    if endPoint in presentPoints:
        break
    
endPoint, startPoint = (height, width-1), (-1, 0)
presentPoints = set()
presentPoints.add(startPoint)
while True:
    blizzardSet, freeCoordinates = moveBlizzards(fullGrid, blizzardSet, width, height)
    presentPoints = step(presentPoints, freeCoordinates)
    time += 1
    if endPoint in presentPoints:
        break
    
print("Time to get the snack is: {}".format(time))