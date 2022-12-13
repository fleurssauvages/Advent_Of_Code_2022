#!/usr/bin/env python
import numpy as np

f = open("ressources/day1.txt", "r")
lines = f.readlines()

coutElf = []
total = 0

for line in lines:
    if len(line) > 1:
        total = total + int(line)
    else:
        coutElf.append(total)
        total = 0

coutElf.sort(reverse=True)

print("Max Cal by an elf is: {}".format(coutElf[0]))

print("Max Cal by top 3 elves are: {}".format(coutElf[0]+coutElf[1]+coutElf[2]))