#!/usr/bin/env python
import numpy as np
from collections import defaultdict
    
f = open("ressources/day23.txt", "r")
lines = f.readlines()

elvesArrangement = []
for line in lines:
    mapLine = line.replace("\n", "").replace(".", "0").replace("#", "1")
    elvesArrangement.append(list(mapLine))

elvesArrangement = [map(int, line) for line in elvesArrangement]
elvesMap = np.array(elvesArrangement)
elves = list(np.argwhere(elvesMap == 1))
elves = set(elf[0]+elf[1]*1j for elf in elves)

directions = [[-1, -1+1j, -1-1j], [1, 1+1j, 1-1j], [-1j, -1-1j, 1-1j], [1j, -1+1j, 1+1j]]
neighbours = [-1, 1, -1j, 1j, -1-1j, -1+1j, 1-1j, 1+1j]

def moveElves(elves, directions, neighbours):
    noOneMove = True
    moveProposals = defaultdict(list)

    for elf in elves:
        neighboursSet = set(elf + neighbour for neighbour in neighbours)
        if len(neighboursSet.intersection(elves)) == 0:
            continue
        noOneMove = False
        for direction in directions:
            desiredSet = set(elf + subDirection for subDirection in direction)
            if len(desiredSet.intersection(elves)) == 0:
                moveProposals[elf + direction[0]].append(elf)
                break

    for proposal in moveProposals:
        if len(moveProposals[proposal]) == 1:
            elves.remove(moveProposals[proposal][0])
            elves.add(proposal)
    
    return noOneMove

for _ in range(10):
    moveElves(elves, directions, neighbours)
    directions.append(directions.pop(0))
    
x, y = [elf.real for elf in elves], [elf.imag for elf in elves]
empty = int((max(x) - min(x) + 1) * (max(y) - min(y) + 1) - len(elves))
print("Empty tiles number is: {}".format(empty))
    
round = 10
noOneMove = False
while not noOneMove:
    noOneMove = moveElves(elves, directions, neighbours)
    directions.append(directions.pop(0))
    round += 1
    
print("Needed rounds are: {}".format(round))