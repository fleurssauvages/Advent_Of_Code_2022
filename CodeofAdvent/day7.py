#!/usr/bin/env python

class directory():
    def __init__(self, name, parent):
        self.name = name
        self.directories = {}
        self.files = []
        self.parent = parent
        self.size = -1
    def calculateSize(self):
        if self.size >= 0:
            return self.size
        size = 0
        for file in self.files:
            size += file.size
        for directoryName in self.directories:
            size += self.directories[directoryName].calculateSize()
        self.size = size
        return self.size
        
class file():
    def __init__(self, name, size):
        self.name = name
        self.size = size

f = open("ressources/day7.txt", "r")
lines = f.readlines()

root = directory("/", None)
currentDirectory = root
allDirectories = []

for line in lines[1:]:
    instructions = line.replace("\n", "").split(" ")
    if instructions[0] == '$':
        if instructions[1] == 'cd':
            if instructions[2] == '..':
                currentDirectory = currentDirectory.parent
            else:
                currentDirectory = currentDirectory.directories[instructions[2]]
        if instructions[1] == 'ls':
            pass
    else:
        if instructions[0] == 'dir':
            newDirectory = directory(instructions[1], currentDirectory)
            currentDirectory.directories[instructions[1]] = newDirectory
            allDirectories.append(newDirectory)
        else:
            newFile = file(instructions[1], int(instructions[0]))
            currentDirectory.files.append(newFile)

root.calculateSize()

totalSize = 0
for dir in allDirectories:
    if dir.size <= 100000:
        totalSize += dir.size
        
print("Your Total Size of small files is: {}".format(totalSize))

occupiedSpace = root.size
requiredSpace = 30000000
availableSpace = 70000000
toDeleteSpace = root.size - (availableSpace-requiredSpace)

closestSpace = availableSpace
for dir in allDirectories:
    if dir.size > toDeleteSpace and dir.size < closestSpace:
        closestSpace = dir.size
        
print("You need to delete a directory of size: {}".format(closestSpace))