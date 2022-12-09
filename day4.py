#!/usr/bin/env python

f = open("ressources/day4.txt", "r")
lines = f.readlines()

score = 0
for line in lines:
    sections = line.replace("\n", "").split(",")
    sections1 = sections[0].split("-")
    sections2 = sections[1].split("-")
    if int(sections1[0]) <= int(sections2[0]) and int(sections1[1]) >= int(sections2[1]):
        score += 1
    elif int(sections2[0]) <= int(sections1[0]) and int(sections2[1]) >= int(sections1[1]):
        score += 1
        
print("Your Score is: {}".format(score))

score = 0
for line in lines:
    sections = line.replace("\n", "").split(",")
    sections1 = sections[0].split("-")
    sections2 = sections[1].split("-")
    if int(sections2[0]) >= int(sections1[0]) and int(sections2[0]) <= int(sections1[1]):
        score += 1
    elif int(sections2[1]) >= int(sections1[0]) and int(sections2[1]) <= int(sections1[1]):
        score += 1
    elif int(sections1[0]) >= int(sections2[0]) and int(sections1[0]) <= int(sections2[1]):
        score += 1
    elif int(sections1[1]) >= int(sections2[0]) and int(sections1[1]) <= int(sections2[1]):
        score += 1
        
print("Your Score is: {}".format(score))