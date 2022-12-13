#!/usr/bin/env python
import numpy as np

f = open("ressources/day8.txt", "r")
lines = f.readlines()

treeArray = np.zeros((99, 99))
i = 0
for line in lines:
    treeSTR = line.replace("\n", "")
    treeList = [int(tree) for tree in str(treeSTR)]
    treeArray[i, :] = treeList
    i += 1

isVisibleArray = np.zeros(treeArray.shape)
isVisibleArray[0,:] = 1
isVisibleArray[-1,:] = 1
isVisibleArray[:,0] = 1
isVisibleArray[:,-1] = 1

for i in range(1,isVisibleArray.shape[0]-1):
    for j in range(1,isVisibleArray.shape[1]-1):
        treeValue = treeArray[i,j]
        maxUp = np.amax(treeArray[0:i,j])
        maxDown = np.amax(treeArray[i+1:,j])
        maxRight = np.amax(treeArray[i,j+1:])
        maxLeft = np.amax(treeArray[i,0:j])
        if treeValue > np.amin([maxUp,maxDown,maxRight,maxLeft]):
            isVisibleArray[i,j] = 1

print("Number of visible trees is: {}".format(np.sum(isVisibleArray)))

VisiblityScoreMax = 0
for i in range(1,isVisibleArray.shape[0]-1):
    for j in range(1,isVisibleArray.shape[1]-1):
        treeValue = treeArray[i,j]
        
        Up = treeArray[0:i,j][::-1]
        tallerTrees = (Up>=treeValue)*1
        tallerTrees[-1] = 1
        firstUp = np.argmax(tallerTrees)+1
        
        Down = treeArray[i+1:,j]
        tallerTrees = (Down>=treeValue)*1
        tallerTrees[-1] = 1
        firstDown = np.argmax(tallerTrees)+1
        
        Right = treeArray[i,j+1:]
        tallerTrees = (Right>=treeValue)*1
        tallerTrees[-1] = 1
        firstRight = np.argmax(tallerTrees)+1
        
        Left = treeArray[i,0:j][::-1]
        tallerTrees = (Left>=treeValue)*1
        tallerTrees[-1] = 1
        firstLeft = np.argmax(tallerTrees)+1
        
        VisiblityScore = firstUp*firstDown*firstLeft*firstRight
        if VisiblityScoreMax < VisiblityScore:
            VisiblityScoreMax = VisiblityScore

print("Biggest visibility score is: {}".format(VisiblityScoreMax))        