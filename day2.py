#!/usr/bin/env python

f = open("ressources/day2.txt", "r")
lines = f.readlines()

score = 0
association = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

for line in lines:
    opponentchoice = association[line[0]]
    mychoice = line[2]
    if mychoice == opponentchoice:
        score += 3
        
    if mychoice == 'X':
        score += 1
        if opponentchoice == 'Z':
            score += 6
    if mychoice == 'Y':
        score += 2
        if opponentchoice == 'X':
            score += 6
    if mychoice == 'Z':
        score += 3
        if opponentchoice == 'Y':
            score += 6
            
print("Your Score is: {}".format(score))

score = 0
loss = {
    'X': 3,
    'Y': 1,
    'Z': 2
}
draw = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
win = {
    'X': 2,
    'Y': 3,
    'Z': 1
}

for line in lines:
    opponentchoice = association[line[0]]
    result = line[2]
    if result == 'X':
        score += loss[opponentchoice]
    if result == 'Y':
        score +=3
        score += draw[opponentchoice]
    if result == 'Z':
        score +=6
        score += win[opponentchoice]

print("Your Score is: {}".format(score))