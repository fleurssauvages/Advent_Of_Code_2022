#!/usr/bin/env python
import numpy as np

f = open("ressources/day25.txt", "r")
lines = f.readlines()

snafuToDecimal = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}

def translateSNAFU(snafu, snafuToDecimal):
    decimal = 0
    for index, snafuCharacter in enumerate(snafu[::-1]):
        decimal += np.power(5, index) * snafuToDecimal[snafuCharacter]
    return decimal

total = 0

for line in lines:
    snafu = line.replace("\n", "")
    total += translateSNAFU(snafu, snafuToDecimal)
    
decimalToSnafu = {3: "=", 4: "-", 0: "0", 1: "1", 2: "2"}

def translateDecimal(decimal, decimalToSnafu):
    snafu = ""
    while decimal != 0:
        remainder = decimal % 5
        if remainder > 2:
            decimal += remainder
        snafu = decimalToSnafu[remainder] + snafu
        decimal //= 5
    return snafu

snafuToFuel = translateDecimal(total, decimalToSnafu)

print("Total Snafu is: {}".format(snafuToFuel))
