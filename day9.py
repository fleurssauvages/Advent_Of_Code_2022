#!/usr/bin/env python
import numpy as np

f = open("ressources/day9.txt", "r")
lines = f.readlines()

HeadPosition = [0, 0]
TailPosition = [0, 0]
listOfTailPositions = []

for line in lines:
    instructions = line.replace("\n", "").split(" ")
    direction = instructions[0]
    numberOfSteps = int(instructions[1])
    for i in range(numberOfSteps):
        if direction == "D":
            HeadPosition[1] += -1
        if direction == "U":
            HeadPosition[1] += +1
        if direction == "L":
            HeadPosition[0] += -1
        if direction == "R":
            HeadPosition[0] += +1
        positionDifference = [HeadPosition[0]-TailPosition[0], HeadPosition[1]-TailPosition[1]]
        if abs(positionDifference[0]) > 1 or abs(positionDifference[1]) > 1:
            TailPosition[0] += np.sign(positionDifference[0])
            TailPosition[1] += np.sign(positionDifference[1])
            
        listOfTailPositions.append([TailPosition[0], TailPosition[1]])

listOfTailPositions = np.unique(listOfTailPositions,  axis=0)
print("Number of visited positions is: {}".format(len(listOfTailPositions)))

ropeLength = 10
ropeList = []
listOfTailPositions = []

for i in range(ropeLength):
    ropeList.append([0,0])

for line in lines:
    instructions = line.replace("\n", "").split(" ")
    direction = instructions[0]
    numberOfSteps = int(instructions[1])
    for i in range(numberOfSteps):
        if direction == "D":
            ropeList[0][1] += -1
        if direction == "U":
            ropeList[0][1] += +1
        if direction == "L":
            ropeList[0][0] += -1
        if direction == "R":
            ropeList[0][0] += +1
        for i in range(1,ropeLength):
            HeadPosition = ropeList[i-1]
            TailPosition = ropeList[i]
            positionDifference = [HeadPosition[0]-TailPosition[0], HeadPosition[1]-TailPosition[1]]
            if abs(positionDifference[0]) > 1 or abs(positionDifference[1]) > 1:
                ropeList[i][0] += np.sign(positionDifference[0])
                ropeList[i][1] += np.sign(positionDifference[1])
        
        listOfTailPositions.append([TailPosition[0], TailPosition[1]])

listOfTailPositions = np.unique(listOfTailPositions,  axis=0)         
print("Number of visited positions is: {}".format(len(listOfTailPositions)))
