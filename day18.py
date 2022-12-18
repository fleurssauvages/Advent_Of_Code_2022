#!/usr/bin/env python
import numpy as np

f = open("ressources/day18.txt", "r")
lines = f.readlines()
cubes = np.zeros((len(lines), 3))

i = 0
for line in lines:
    x,y,z = line.replace("\n", "").split(",")
    cubes[i, :] = [int(x), int(y), int(z)]
    i += 1

nbFaces = 0
for cube in cubes:
    face1 = cube - [1,0,0]
    face2 = cube + [1,0,0]
    face3 = cube - [0,1,0]
    face4 = cube + [0,1,0]
    face5 = cube - [0,0,1]
    face6 = cube + [0,0,1]
    faces = [face1, face2, face3, face4, face5, face6]
    for face in faces:
        if np.amin(np.sum(np.abs(cubes-face), axis=1))>0:
            nbFaces +=1
            
print("Number of uncovered faces is: {}".format(nbFaces))

depth = 22
width = 22
height = 22

class floodMap():
    def __init__(self, cubes, maxDimensions):
        self.map = np.zeros((maxDimensions[0]+1, maxDimensions[1]+1, maxDimensions[2]+1))+1000000
        self.cubes = cubes
        self.currentNodes = []
        
    def checkNeighbours(self, node):
        i = node[0]
        j = node[1]
        k = node[2]
        currentDistance = self.map[i, j, k]
        
        nodesToVisit = []
        if i > 0:
            nodesToVisit.append([i-1,j, k])
        if j > 0:
            nodesToVisit.append([i,j-1, k])
        if i < self.map.shape[0]-1:
            nodesToVisit.append([i+1,j, k])
        if j < self.map.shape[1]-1:
            nodesToVisit.append([i,j+1, k])
        if k > 0:
            nodesToVisit.append([i,j, k-1])
        if k < self.map.shape[2]-1:
            nodesToVisit.append([i,j, k+1])
            
        for nodeVisiting in nodesToVisit:
            isCube = (np.amin(np.sum(np.abs(cubes-nodeVisiting), axis=1))==0)
            newDistance = self.map[nodeVisiting[0], nodeVisiting[1], nodeVisiting[2]]
            if (not isCube) and newDistance > currentDistance+1:
                self.map[nodeVisiting[0], nodeVisiting[1], nodeVisiting[2]] = currentDistance+1
                self.currentNodes.append(nodeVisiting)
                
    def fillMap(self, start):
        self.map[start[0],start[1], start[2]] = 0
        self.currentNodes.append(start)
        while len(self.currentNodes) > 0:
            node = self.currentNodes.pop(0)
            self.checkNeighbours(node)

lava = floodMap(cubes, [depth, width, height])
start = [0,0,0]
lava.fillMap(start)

nbFaces = 0
for cube in cubes:
    face1 = cube - [1,0,0]
    face2 = cube + [1,0,0]
    face3 = cube - [0,1,0]
    face4 = cube + [0,1,0]
    face5 = cube - [0,0,1]
    face6 = cube + [0,0,1]
    faces = [face1, face2, face3, face4, face5, face6]
    for face in faces:
        if lava.map[int(face[0]), int(face[1]), int(face[2])] < 10000:
            nbFaces +=1
                    
print("Number of uncovered external faces is: {}".format(nbFaces))