#!/usr/bin/env python
import numpy as np

def rightPush(rock, rockTower):
    for pixel in rock:
        pixelPosition = rock[pixel]
        if pixelPosition[1] == 6:
            return rock
        if rockTower[pixelPosition[0], pixelPosition[1]+1] > 0:
            return rock
    for pixel in rock:
        rock[pixel] = [rock[pixel][0], rock[pixel][1]+1]
    return rock

def leftPush(rock, rockTower):
    for pixel in rock:
        pixelPosition = rock[pixel]
        if pixelPosition[1] == 0:
            return rock
        if rockTower[pixelPosition[0], pixelPosition[1]-1] > 0:
            return rock
    for pixel in rock:
        rock[pixel] = [rock[pixel][0], rock[pixel][1]-1]
    return rock

def moveDownOne(rock, rockTower):
    for pixel in rock:
        pixelPosition = rock[pixel]
        if pixelPosition[0] == 0:
            return rock, False
        if rockTower[pixelPosition[0]-1, pixelPosition[1]] > 0:
            return rock, False
    for pixel in rock:
        rock[pixel] = [rock[pixel][0]-1, rock[pixel][1]]
    return rock, True

def rockFall(rock, rockTower, currentJetInstructionId, jet, currentHeight):
    hasMove = True
    while hasMove:
        if jet[currentJetInstructionId % len(jet)] == '>':
            rock = rightPush(rock, rockTower)
        else:
            rock = leftPush(rock, rockTower)
        rock, hasMove = moveDownOne(rock, rockTower)
        currentJetInstructionId +=1
        
    for pixel in rock:
        pixelPosition = rock[pixel]
        rockTower[pixelPosition[0], pixelPosition[1]] = 1
        if pixelPosition[0] > currentHeight:
            currentHeight = pixelPosition[0]
            
    return rockTower, currentJetInstructionId, currentHeight

f = open("ressources/day17.txt", "r")
lines = f.readlines()

jet = list(lines[0].replace("\n", ""))
rockTower = np.zeros((6000, 7))
currentHeight = -1
currentJetInstructionId = 0

rock_tiret = {"0":[0,0], "1":[0,1], "2":[0,2], "3":[0,3]}
rock_plus = {"0":[0,1], "1":[1,0], "2":[1,1], "3":[1,2], "4":[2,1]}
rock_lshape = {"0":[0,0], "1":[0,1], "2":[0,2], "3":[1,2], "4":[2,2]}
rock_bar = {"0":[0,0], "1":[1,0], "2":[2,0], "3":[3,0]}
rock_cube = {"0":[0,0], "1":[0,1], "2":[1,0], "3":[1,1]}

rockShapes = [rock_tiret, rock_plus, rock_lshape, rock_bar, rock_cube]

for i in range(2022):
    rock = rockShapes[i%5].copy()
    for pixel in rock:
        rock[pixel] = [rock[pixel][0]+currentHeight+4, rock[pixel][1]+2]
    rockTower, currentJetInstructionId, currentHeight = rockFall(rock, rockTower, currentJetInstructionId, jet, currentHeight)

print("Height after 2022 rock fell is: {}".format(currentHeight+1))

jet = list(lines[0].replace("\n", ""))
rockTower = np.zeros((6000, 7))
currentHeight = -1
currentJetInstructionId = 0

totalHeight = 0
patterns = {}

numberOfRocks = 1000000000000
keepGoing = True
i = 0

while keepGoing:
    rock = rockShapes[i%5].copy()
    for pixel in rock:
        rock[pixel] = [rock[pixel][0]+currentHeight+4, rock[pixel][1]+2]
    rockTower, currentJetInstructionId, currentHeight = rockFall(rock, rockTower, currentJetInstructionId, jet, currentHeight)
    
    rockCycle = i % 5
    jetCycle = currentJetInstructionId % len(jet)
    cycleIndex = (rockCycle, jetCycle)
    if cycleIndex in patterns:
        previousIndex, previousHeight = patterns[cycleIndex]
        period = i - previousIndex
        if i % period == numberOfRocks % period:
            elevationPerCycle = currentHeight - previousHeight
            leftRocks = numberOfRocks - i
            leftCycles = (leftRocks // period) + 1
            totalHeight = previousHeight + (leftCycles * elevationPerCycle)
            keepGoing = False
    else:
        patterns[cycleIndex] = (i, currentHeight)
    i+=1
        
print("Height after 1000000000000 rock fell is: {}".format(totalHeight))
