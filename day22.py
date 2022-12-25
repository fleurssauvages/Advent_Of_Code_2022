#!/usr/bin/env python
import numpy as np

def doInstruction(startingPos, monkeyMap, instruction):
    nbSteps = int(instruction[:-1])
    directionChange = instruction[-1]
    Rmapping = {"up":"right", "right":"down", "down":"left", "left":"up"}
    Lmapping = {"right":"up", "down":"right", "left":"down", "up":"left"}
    
    if startingPos[1] == "right":
        for _ in range(nbSteps):
            if startingPos[0][1] == monkeyMap.shape[1]-1:
                teleportColumn = np.amin(np.argwhere(monkeyMap[startingPos[0][0],:] != 3))
                if monkeyMap[startingPos[0][0], teleportColumn] == 1:
                    startingPos[0][1] = teleportColumn
            elif monkeyMap[startingPos[0][0], startingPos[0][1]+1] == 1:
                startingPos[0][1] += 1
            elif monkeyMap[startingPos[0][0], startingPos[0][1]+1] == 2:
                pass
            elif monkeyMap[startingPos[0][0], startingPos[0][1]+1] == 3:
                teleportColumn = np.amin(np.argwhere(monkeyMap[startingPos[0][0],:] != 3))
                if monkeyMap[startingPos[0][0], teleportColumn] == 1:
                    startingPos[0][1] = teleportColumn
                
    elif startingPos[1] == "left":
        for _ in range(nbSteps):
            if startingPos[0][1] == 0:
                teleportColumn = np.amax(np.argwhere(monkeyMap[startingPos[0][0],:] != 3))
                if monkeyMap[startingPos[0][0], teleportColumn] == 1:
                    startingPos[0][1] = teleportColumn
            elif monkeyMap[startingPos[0][0], startingPos[0][1]-1] == 1:
                startingPos[0][1] -= 1
            elif monkeyMap[startingPos[0][0], startingPos[0][1]-1] == 2:
                pass
            elif monkeyMap[startingPos[0][0], startingPos[0][1]-1] == 3:
                teleportColumn = np.amax(np.argwhere(monkeyMap[startingPos[0][0],:] != 3))
                if monkeyMap[startingPos[0][0], teleportColumn] == 1:
                    startingPos[0][1] = teleportColumn
                    
    elif startingPos[1] == "down":
        for _ in range(nbSteps):
            if startingPos[0][0] == monkeyMap.shape[0]-1:
                teleportRow = np.amin(np.argwhere(monkeyMap[:,startingPos[0][1]] != 3))
                if monkeyMap[teleportRow, startingPos[0][1]] == 1:
                    startingPos[0][0] = teleportRow
            elif monkeyMap[startingPos[0][0]+1, startingPos[0][1]] == 1:
                startingPos[0][0] += 1
            elif monkeyMap[startingPos[0][0]+1, startingPos[0][1]] == 2:
                pass
            elif monkeyMap[startingPos[0][0]+1, startingPos[0][1]] == 3:
                teleportRow = np.amin(np.argwhere(monkeyMap[:,startingPos[0][1]] != 3))
                if monkeyMap[teleportRow, startingPos[0][1]] == 1:
                    startingPos[0][0] = teleportRow
                    
    elif startingPos[1] == "up":
        for _ in range(nbSteps):
            if startingPos[0][0] == 0:
                teleportRow = np.amax(np.argwhere(monkeyMap[:,startingPos[0][1]] != 3))
                if monkeyMap[teleportRow, startingPos[0][1]] == 1:
                    startingPos[0][0] = teleportRow
            elif monkeyMap[startingPos[0][0]-1, startingPos[0][1]] == 1:
                startingPos[0][0] -= 1
            elif monkeyMap[startingPos[0][0]-1, startingPos[0][1]] == 2:
                pass
            elif monkeyMap[startingPos[0][0]-1, startingPos[0][1]] == 3:
                teleportRow = np.amax(np.argwhere(monkeyMap[:,startingPos[0][1]] != 3))
                if monkeyMap[teleportRow, startingPos[0][1]] == 1:
                    startingPos[0][0] = teleportRow
                    
    if directionChange == 'R':
        startingPos[1] = Rmapping[startingPos[1]]
    elif directionChange == 'L':
        startingPos[1] = Lmapping[startingPos[1]]
    return startingPos
                    

f = open("ressources/day22.txt", "r")
lines = f.readlines()

monkeyMap = []
instructions = ""
mapWidth = 0
nextInstructions = False
for line in lines:
    if len(line.strip()) == 0:
        nextInstructions = True
    elif nextInstructions:
        instructions = line.replace("\n", "")
    else:
        mapLine = line.replace("\n", "").replace(" ", "3")
        monkeyMap.append(list(mapLine.replace("#", "2").replace(".", "1")))
        mapWidth = max(len(line), mapWidth)
for mapLine in monkeyMap:
    if len(mapLine) < mapWidth:
        while len(mapLine) < mapWidth:
            mapLine.append("3")
            
instructions = instructions.replace("R","R ").replace("L","L ")
instructions = instructions.split(' ')
instructions[-1] = instructions[-1]+"S"

monkeyMap = [map(int, monkeyLine) for monkeyLine in monkeyMap]
monkeyMap = np.array(monkeyMap)

yStart = np.amin(np.argwhere(monkeyMap[0,:] == 1))
startingPos = [[0,yStart], "right"]

for instruction in instructions:
    startingPos = doInstruction(startingPos, monkeyMap, instruction)

row = int(startingPos[0][0])+1
column = int(startingPos[0][1])+1
if startingPos[1] == "right":
    direction = 0
if startingPos[1] == "down":
    direction = 1
if startingPos[1] == "left":
    direction = 2
if startingPos[1] == "up":
    direction = 3
print("Password is: {}".format(row*1000+4*column+direction))

faces = {}
mappings = {}

#        +------+------+
#        |  g   |   e  |
#        |f 1   |   2 d|
#        |      |  b   |
#        +------+------+
#        |      |
#        |a  3 b|
#        |      |
# +------+------+
# |   a  |      |
# |f  4  |   5 d|
# |      |   c  |
# +------+------+
# |      |
# |g  6 c|
# |   e  |
# +------+

width = 50
face1 = monkeyMap[0:width, width:2*width]
facemapping1 = {"up": ["6", "left"], "down":["3", "up"], "left":["4", "left"], "right":["2", "left"]}

face2 = monkeyMap[0:width, 2*width:3*width]
facemapping2 = {"up": ["6", "down"], "down":["3", "right"], "left":["1", "right"], "right":["5", "right"]}

face3 = monkeyMap[width:2*width, width:2*width]
facemapping3 = {"up": ["1", "down"], "down":["5", "up"], "left":["4", "up"], "right":["2", "down"]}

face4 = monkeyMap[2*width:3*width, 0:width]
facemapping4 = {"up": ["3", "left"], "down":["6", "up"], "left":["1", "left"], "right":["5", "left"]}

face5 = monkeyMap[2*width:3*width, width:2*width]
facemapping5 = {"up": ["3", "down"], "down":["6", "right"], "left":["4", "right"], "right":["2", "right"]}

face6 = monkeyMap[3*width:4*width, 0:width]
facemapping6 = {"up": ["4", "down"], "down":["2", "up"], "left":["1", "up"], "right":["5", "down"]}

faces = {"1":face1, "2":face2, "3":face3, "4":face4, "5":face5, "6":face6}

mappings = {"1":facemapping1, "2":facemapping2, "3":facemapping3, "4":facemapping4, "5":facemapping5, "6":facemapping6}
            
def nextPosition(startingPos, startFace, mappings):
    endFace = startFace
    direction = startingPos[1]
    
    if direction == "right":
        if startingPos[0][1] < width-1:
            goTo, endFace = [startingPos[0][0], startingPos[0][1]+1], startFace
        else:
            endFace, side = mappings[startFace][direction]
            x,y = startingPos[0][0], startingPos[0][1]
            w = width-1
            if side == "left":
                direction = "right"
                goTo = [x, w-y]
            elif side == "up":
                goTo = [w-y, w-x]
                direction = "down"
            elif side == "down":
                direction = "up"
                goTo = [y, x]
            elif side == "right":
                direction = "left"
                goTo = [w-x, y]
        return goTo, direction, endFace
    
    
    if direction == "left":
        if startingPos[0][1] > 0:
            goTo, endFace = [startingPos[0][0], startingPos[0][1]-1], startFace
        else:
            endFace, side = mappings[startFace][direction]
            x,y = startingPos[0][0], startingPos[0][1]
            w = width-1
            if side == "left":
                goTo = [w-x,y]
                direction = "right"
            elif side == "up":
                goTo = [w-y, x]
                direction = "down"
            elif side == "down":
                direction = "up"
                goTo = [w-y,w-x]
            elif side == "right":
                goTo = [x, w-y]
                direction = "left"
        return goTo, direction, endFace
    
    if direction == "up":
        if startingPos[0][0] > 0:
            goTo, endFace = [startingPos[0][0]-1, startingPos[0][1]], startFace
        else:
            endFace, side = mappings[startFace][direction]
            x,y = startingPos[0][0], startingPos[0][1]
            w = width-1
            if side == "up":
                goTo = [w-y, w-x]
                direction = "down"
            elif side == "down":
                direction = "up"
                goTo = [w-x, y]
            elif side == "left":
                direction = "right"
                goTo = [y, x]
            elif side == "right":
                goTo = [w-y, w-x]
                direction = "left"
        return goTo, direction, endFace
    
    if direction == "down":
        if startingPos[0][0] < width-1:
            goTo, endFace = [startingPos[0][0]+1, startingPos[0][1]], startFace
        else:
            endFace, side = mappings[startFace][direction]
            x,y = startingPos[0][0], startingPos[0][1]
            w = width-1
            if side == "up":
                goTo = [w-x, y]
                direction = "down"
            elif side == "down":
                goTo = [x, w-y]
                direction = "up"
            elif side == "left":
                direction = "right"
                goTo = [w-y, w-x]
            elif side == "right":
                goTo = [y, x]
                direction = "left"
        return goTo, direction, endFace

def doInstruction(startingPos, startingFace, instruction, faces, mappings):
    nbSteps = int(instruction[:-1])
    directionChange = instruction[-1]
    
    Rmapping = {"up":"right", "right":"down", "down":"left", "left":"up"}
    Lmapping = {"right":"up", "down":"right", "left":"down", "up":"left"}
    
    for _ in range(nbSteps):
        goTo, direction, endFace = nextPosition(startingPos, startingFace, mappings)
        if faces[endFace][goTo[0], goTo[1]] == 1:
            startingPos, startingFace = [goTo, direction], endFace
        else:
            continue
            
    if directionChange == 'R':
        startingPos[1] = Rmapping[startingPos[1]]
    elif directionChange == 'L':
        startingPos[1] = Lmapping[startingPos[1]]
                    
    return startingPos, startingFace

startingFace = "1"
yStart = np.amin(np.argwhere(face1[0,:] == 1))
startingPos = [[0,yStart], "right"]

for instruction in instructions:
    startingPos, startingFace = doInstruction(startingPos, startingFace, instruction, faces, mappings)

if startingFace == '"1':
    startingPos[0][1] += width
elif startingFace == '2':
    startingPos[0][1] += width*2
elif startingFace == '3':
    startingPos[0][0] += width
    startingPos[0][1] += width
elif startingFace == '4':
    startingPos[0][0] += 2*width
elif startingFace == '5':
    startingPos[0][0] += 2*width
    startingPos[0][1] += width
elif startingFace == '6':
    startingPos[0][0] += 3*width

row = int(startingPos[0][0])+1
column = int(startingPos[0][1])+1
if startingPos[1] == "right":
    direction = 0
elif startingPos[1] == "down":
    direction = 1
elif startingPos[1] == "left":
    direction = 2
elif startingPos[1] == "up":
    direction = 3
    
print("Cubic Password is: {}".format(row*1000+4*column+direction))