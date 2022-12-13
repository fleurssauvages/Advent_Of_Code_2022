#!/usr/bin/env python

f = open("ressources/day6.txt", "r")
lines = f.readlines()

message = lines[0]
start = 0

while True:
    chaine = message[start:start+4]
    if len(set(chaine)) == len(chaine):
        break
    else:
        start += 1
            
print("Length of start is: {}".format(start+4))

while True:
    chaine = message[start:start+14]
    if len(set(chaine)) == len(chaine):
        break
    else:
        start += 1
            
print("Length of start is: {}".format(start+14))