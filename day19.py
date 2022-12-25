#!/usr/bin/env python
import numpy as np
from collections import defaultdict
from heapq import heapify, heappop, heappush

def optimalSolution(seenStates, startingRessources, startingRobots, robotCosts, time, currentMax):
    if time == 0:
        return startingRessources[3]
    
    state = str([time]+list(startingRobots)+list(startingRessources))
    maxGeodes = seenStates[state]
    if maxGeodes > 0:
        return maxGeodes
    
    maxGeodes = startingRessources[3] + startingRobots[3]*time
    upperGeodesEstimation = ((time + startingRobots[3]) * (time + startingRobots[3] + 1)) // 2 - (startingRobots[3] * (startingRobots[3] + 1)) // 2 + startingRessources[3]
    if upperGeodesEstimation <= currentMax:
        return 0
    
    for i in reversed(range(4)):
        if i < 3 and np.all(startingRobots[i] >= robotCosts[:,i]):
            continue
        timeBeforeBuildingRobot = -1
        for j in range(4):
            if startingRobots[j] == 0 and robotCosts[i,j] > 0:
                timeBeforeBuildingRobot = 1000
            elif startingRobots[j] == 0:
                timeBeforeBuildingRobot = max(-1, timeBeforeBuildingRobot)
            elif startingRessources[j] >= robotCosts[i,j]:
                timeBeforeBuildingRobot = max(0, timeBeforeBuildingRobot)
            else:
                timeBeforeBuildingRobot = max(timeBeforeBuildingRobot, np.ceil((robotCosts[i,j] - startingRessources[j]) / startingRobots[j]))
        if timeBeforeBuildingRobot < 0:
            continue
        elif timeBeforeBuildingRobot < time:
            newTime = time - (timeBeforeBuildingRobot+1)
            newRobots = startingRobots.copy()
            newRobots[i] += 1
            newRessources = startingRessources + startingRobots*(timeBeforeBuildingRobot+1) - robotCosts[i, :]
            maxGeodes = max(maxGeodes, optimalSolution(seenStates, newRessources, newRobots, robotCosts, newTime, maxGeodes))
            if i == 4:
                seenStates[state] = maxGeodes
                return maxGeodes
            
    seenStates[state] = maxGeodes
    return maxGeodes

f = open("ressources/day19.txt", "r")
lines = f.readlines()

ressourcesLabel = ["ore", "clay", "obsidian", "geode"]

total = 0
for line in lines:
    blueprint = line.replace("\n", "").replace(":", "").replace(".", "").split()
    
    startingRessources = np.array([0, 0, 0, 0])
    startingRobots = np.array([1, 0, 0, 0])
    robotCosts = np.zeros((4,4))
    
    id = blueprint[1]
    robotCosts[0, 0] = blueprint[6]
    robotCosts[1, 0] = blueprint[12]
    robotCosts[2, 0], robotCosts[2, 1] = blueprint[18], blueprint[21]
    robotCosts[3, 0], robotCosts[3, 2] = blueprint[27], blueprint[30]

    seenStates = defaultdict(int)
    maxGeodes = optimalSolution(seenStates, startingRessources, startingRobots, robotCosts, 24, 0)
    print(id, maxGeodes)
    total += int(id) * maxGeodes
    
print("Quality level of blueprints is: {}".format(total))

total = 1
for line in lines[0:3]:
    blueprint = line.replace("\n", "").replace(":", "").replace(".", "").split()
    
    startingRessources = np.array([0, 0, 0, 0])
    startingRobots = np.array([1, 0, 0, 0])
    robotCosts = np.zeros((4,4))
    
    id = blueprint[1]
    robotCosts[0, 0] = blueprint[6]
    robotCosts[1, 0] = blueprint[12]
    robotCosts[2, 0], robotCosts[2, 1] = blueprint[18], blueprint[21]
    robotCosts[3, 0], robotCosts[3, 2] = blueprint[27], blueprint[30]
    
    seenStates = defaultdict(int)
    maxGeodes = optimalSolution(seenStates, startingRessources, startingRobots, robotCosts, 32, 0)
    print(id, maxGeodes)
    total *= maxGeodes
    
print("Quality level of blueprints is: {}".format(total))