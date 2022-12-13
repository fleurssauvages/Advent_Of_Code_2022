#!/usr/bin/env python
import numpy as np

class Monkey():
    def __init__(self, items, lambdaFunc, divisibleNumber, passTrue, passFalse):
        self.items = items
        self.operation = lambdaFunc
        self.divisibleTest = divisibleNumber
        self.passTrue = passTrue
        self.passFalse = passFalse
        self.inspectedItems = 0

monkey0 = Monkey([65,78], lambda x:x*3, 5, 2, 3)
monkey1 = Monkey([54, 78, 86, 79, 73, 64, 85, 88], lambda x:x+8, 11, 4, 7)
monkey2 = Monkey([69, 97, 77, 88, 87], lambda x:x+2, 2, 5, 3)
monkey3 = Monkey([99], lambda x:x+4, 13, 1, 5)
monkey4 = Monkey([60, 57, 52], lambda x:x*19, 7, 7, 6)
monkey5 = Monkey([91, 82, 85, 73, 84, 53], lambda x:x+5, 3, 4, 1)
monkey6 = Monkey([88, 74, 68, 56], lambda x:x*x, 17, 0, 2)
monkey7 = Monkey([54, 82, 72, 71, 53, 99, 67], lambda x:x+1, 19, 6, 0)

monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

for i in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspectedItems += 1
            worryLevel = monkey.operation(item)//3
            if worryLevel % monkey.divisibleTest == 0:
                monkeys[monkey.passTrue].items.append(worryLevel)
            else:
                monkeys[monkey.passFalse].items.append(worryLevel)
        monkey.items = []

monkeyInspected = []
for monkey in monkeys:
    # print("Monkey inspected items is: {}".format(monkey.inspectedItems))
    monkeyInspected.append(monkey.inspectedItems)
    
monkeyInspected.sort(reverse=True)
print("Monkey business is: {}".format(monkeyInspected[0]*monkeyInspected[1]))

## PART 2

monkey0 = Monkey([65,78], lambda x:x*3, 5, 2, 3)
monkey1 = Monkey([54, 78, 86, 79, 73, 64, 85, 88], lambda x:x+8, 11, 4, 7)
monkey2 = Monkey([69, 97, 77, 88, 87], lambda x:x+2, 2, 5, 3)
monkey3 = Monkey([99], lambda x:x+4, 13, 1, 5)
monkey4 = Monkey([60, 57, 52], lambda x:x*19, 7, 7, 6)
monkey5 = Monkey([91, 82, 85, 73, 84, 53], lambda x:x+5, 3, 4, 1)
monkey6 = Monkey([88, 74, 68, 56], lambda x:x*x, 17, 0, 2)
monkey7 = Monkey([54, 82, 72, 71, 53, 99, 67], lambda x:x+1, 19, 6, 0)

monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

mod = 1
for monkey in monkeys:
    mod *= monkey.divisibleTest

for i in range(10000):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspectedItems += 1
            worryLevel = monkey.operation(item) % mod
            if worryLevel % monkey.divisibleTest == 0:
                monkeys[monkey.passTrue].items.append(worryLevel)
            else:
                monkeys[monkey.passFalse].items.append(worryLevel)
        monkey.items = []

monkeyInspected = []
for monkey in monkeys:
    # print("Monkey inspected items is: {}".format(monkey.inspectedItems))
    monkeyInspected.append(monkey.inspectedItems)
    
monkeyInspected.sort(reverse=True)
print("Monkey business is: {}".format(monkeyInspected[0]*monkeyInspected[1]))