#!/usr/bin/env python

f = open("ressources/day3.txt", "r")
lines = f.readlines()

score = 0

for line in lines:
    sizeCompartment = len(line)
    compartment1 = line[:sizeCompartment/2]
    compartment2 = line[sizeCompartment/2:].strip()
    commonItem = list(set(compartment1)&set(compartment2))[0]
    
    if commonItem.isupper():
        score += ord(commonItem)-64+26
    else:
        score += ord(commonItem)-96

print("Your Score is: {}".format(score))

score = 0
for line1, line2, line3 in zip(lines[0::3], lines[1::3], lines[2::3]):
    commons = list(set(line1)&set(line2)&set(line3))
    commons.sort()
    commonItem = commons[1]
    if commonItem.isupper():
        score += ord(commonItem)-64+26
    else:
        score += ord(commonItem)-96
        
print("Your Score is: {}".format(score))