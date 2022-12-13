#!/usr/bin/env python
import numpy as np

class distanceMap():
    def __init__(self, heightMap):
        self.map = np.zeros(heightMap.shape)+1000000
        self.heightMap = heightMap
        self.currentNodes = []
        
    def checkNeighbours(self, node):
        i = node[0]
        j = node[1]
        currentHeight = self.heightMap[i, j]
        currentDistance = self.map[i, j]
        
        nodesToVisit = []
        if i > 0:
            nodesToVisit.append([i-1,j])
        if j > 0:
            nodesToVisit.append([i,j-1])
        if i < self.map.shape[0]-1:
            nodesToVisit.append([i+1,j])
        if j < self.map.shape[1]-1:
            nodesToVisit.append([i,j+1])
            
        for nodeVisiting in nodesToVisit:
            newHeight = self.heightMap[nodeVisiting[0], nodeVisiting[1]]
            newDistance = self.map[nodeVisiting[0], nodeVisiting[1]]
            if (newHeight - currentHeight) <= 1 and newDistance > currentDistance+1:
                self.map[nodeVisiting[0], nodeVisiting[1]] = currentDistance+1
                self.currentNodes.append(nodeVisiting)
                
    def fillMap(self, start):
        self.map[start[0],start[1]] = 0
        self.currentNodes.append(start)
        while len(self.currentNodes) > 0:
            node = self.currentNodes.pop(0)
            self.checkNeighbours(node)
        

f = open("ressources/day12.txt", "r")
lines = f.readlines()

heightMap = np.zeros((len(lines), len(lines[0].replace("\n", ""))))

start = [0,0]
end = [0,0]

i = 0
for line in lines:
    charList = list(line.replace("\n", ""))
    j = 0
    for char in charList:
        if char.isupper():
            if char == "E":
                heightMap[i][j] = 26
                end = [i, j]
            if char == "S":
                heightMap[i][j] = 0
                start = [i, j]
        else:
            heightMap[i][j] = ord(char)-96
        j += 1
    i += 1

distancePathMap = distanceMap(heightMap)
distancePathMap.fillMap(start)
shortestDistance = distancePathMap.map[end[0],end[1]]
print("Shortest Path from start is: {}".format(shortestDistance))

for i in range(heightMap.shape[0]):
    for j in range(heightMap.shape[1]):
        if heightMap[i,j] == 1:
            distancePathMap = distanceMap(heightMap)
            distancePathMap.fillMap([i,j])
            if shortestDistance > distancePathMap.map[end[0],end[1]]:
                shortestDistance = distancePathMap.map[end[0],end[1]]

print("Shortest Path from low ground is: {}".format(shortestDistance))