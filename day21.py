#!/usr/bin/env python
import numpy as np

class Monkey():
    def __init__(self, name, childs, operation, number):
        self.name = name
        self.childs = childs
        self.operation = operation
        self.number = number
    def calculateNumber(self, monkeys):
        if self.number is not None:
            return self.number
        monkeys[self.childs[0]].calculateNumber(monkeys)
        monkeys[self.childs[1]].calculateNumber(monkeys)
        self.number = self.operation(monkeys[self.childs[0]].number, monkeys[self.childs[1]].number)
        return self.number

f = open("ressources/day21.txt", "r")
lines = f.readlines()

monkeys = {}

for line in lines:
    instructions = line.replace("\n", "").replace(":", "").split()
    monkeyName = instructions[0]
    if len(instructions[1]) > 3:
        childs = [instructions[1], instructions[3]]
        if instructions[2] == "+":
            operation = lambda x,y: x+y
        if instructions[2] == "-":
            operation = lambda x,y: x-y
        if instructions[2] == "*":
            operation = lambda x,y: x*y
        if instructions[2] == "/":
            operation = lambda x,y: x/y
        monkey = Monkey(monkeyName, childs, operation, None)
    else:
        monkey = Monkey(monkeyName, None, None, float(instructions[1]))
    monkeys[monkeyName] = monkey
    
monkeys["root"].calculateNumber(monkeys)

print("Root Monkey number is: {}".format(int(monkeys["root"].number)))

monkeys["root"].operation = lambda x,y: x-y
lowerBound = -10000000000000
upperBound = 10000000000000

while True:
    mid = (lowerBound+upperBound)//2
    for monkeyName in monkeys:
        if monkeys[monkeyName].childs is not None:
            monkeys[monkeyName].number = None
    monkeys["humn"].number = mid
    monkeys["root"].calculateNumber(monkeys)
    if monkeys["root"].number < 0:
        upperBound = mid
    elif monkeys["root"].number > 0:
        lowerBound = mid
    else:
        break
    
print("Human correct number is: {}".format(int(mid)))