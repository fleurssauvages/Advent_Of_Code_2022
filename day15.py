#!/usr/bin/env python
import numpy as np

f = open("ressources/day15.txt", "r")
lines = f.readlines()

sensors = []
beacons = []

for line in lines:
    report = line.replace("\n", "").replace("=", " ").replace(":", " ").replace(",", " ").split()
    sensors.append([int(report[3]), int(report[5])])
    beacons.append([int(report[11]), int(report[13])])
    
rowToLook = 2000000
minRange = -10000000
maxRange = 10000000
nbPositionsToExplore = maxRange-minRange+1

rowIsNotPossible = np.zeros(nbPositionsToExplore)

for sensor, beacon in zip(sensors, beacons):
    distance = abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1])
    width = max(-1, distance-abs(sensor[1]-rowToLook))
    if width >= 0:
        rowIsNotPossible[sensor[0]-width-minRange:sensor[0]+width+1-minRange] = 1

for beacon in beacons:
    if beacon[1] == rowToLook:
        rowIsNotPossible[beacon[0]-minRange] = 0
nbPositions = np.sum(rowIsNotPossible)
        
print("Number of non possible positions is: {}".format(int(nbPositions)))

minRow = 0
maxRow = 4000000
minColumn = 0
maxColumn = 4000000
boundaries = [[minRow, maxRow], [minColumn, maxColumn]]

def isValid(point, sensors, distances, boundaries):
    if point[0] < boundaries[0][0]:
        return False
    if point[0] > boundaries[0][1]:
        return False
    if point[1] < boundaries[1][0]:
        return False
    if point[1] > boundaries[1][1]:
        return False
    for sensor, distance in zip(sensors, distances):
        distanceOfPoint = abs(sensor[0]-point[0])+abs(sensor[1]-point[1])
        if distanceOfPoint <= distance:
            return False
    return True

def findUniquePoint(sensors, distances, boundaries):
    for sensor, distance in zip(sensors, distances):
        positiveStep = np.array(range(0,distance+2))
        negativeStep = np.array(range(distance+1, -1, -1))
        
        xCandidates = np.concatenate((sensor[0]+positiveStep, sensor[0]+positiveStep, sensor[0]-positiveStep, sensor[0]-positiveStep))
        yCandidates = np.concatenate((sensor[1]+negativeStep, sensor[1]-negativeStep, sensor[0]+negativeStep, sensor[1]-negativeStep))
        for x,y in zip(xCandidates, yCandidates):
            if isValid([x,y], sensors, distances, boundaries):
                return [x,y]
    return "No Solution"

distances = []
for sensor, beacon in zip(sensors, beacons):
    distances.append(abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1]))
    
uniqueBeaconPoint = findUniquePoint(sensors, distances, boundaries)

print("Tuning frequency is: {}".format(int(uniqueBeaconPoint[0]*4000000+uniqueBeaconPoint[1])))