#!/usr/bin/env python
import numpy as np

f = open("ressources/day20.txt", "r")
lines = f.readlines()

encryptedList = []
for line in lines:
    encryptedList.append(int(line.replace("\n", "")))

decryptedList = [(encryptedList[i], i) for i in range(len(encryptedList))]

length = len(encryptedList)-1
for i in range(len(encryptedList)):
    elem = encryptedList[i]
    index = decryptedList.index((elem,i))
    poppedElement = decryptedList.pop(index)
    if index+elem == 0:
        decryptedList.append(poppedElement)
    else:
        decryptedList.insert((index+elem) % length, poppedElement)
        
elem0 = (0, encryptedList.index(0))
position0 = decryptedList.index(elem0)
elem1 = decryptedList[(position0+1000)%(length+1)][0]
elem2 = decryptedList[(position0+2000)%(length+1)][0]
elem3 = decryptedList[(position0+3000)%(length+1)][0]

print(elem1, elem2, elem3)
print("Grove coordinate is: {}".format(elem1+elem2+elem3))

encryptedList = []
for line in lines:
    encryptedList.append(int(line.replace("\n", "")))

encryptedList = [elem*811589153 for elem in encryptedList]
decryptedList = [(encryptedList[i], i) for i in range(len(encryptedList))]

length = len(encryptedList)-1
for _ in range(10):
    for i in range(len(encryptedList)):
        elem = encryptedList[i]
        index = decryptedList.index((elem,i))
        poppedElement = decryptedList.pop(index)
        if index+elem == 0:
            decryptedList.append(poppedElement)
        else:
            decryptedList.insert((index+elem) % length, poppedElement)
        
elem0 = (0, encryptedList.index(0))
position0 = decryptedList.index(elem0)
elem1 = decryptedList[(position0+1000)%(length+1)][0]
elem2 = decryptedList[(position0+2000)%(length+1)][0]
elem3 = decryptedList[(position0+3000)%(length+1)][0]

print(elem1, elem2, elem3)
print("Grove coordinate is: {}".format(elem1+elem2+elem3))