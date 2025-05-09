# Code that creates a list of 100 'heads' or 'tails' values.
import random

streakBool = 0

for i in range(10000):
    numberOfStreaks = 0
    heads = 0
    tails = 0
    # Simulating 100 coin flips.
    listOfValues = []
    for i in range(1, 101):
        flip = random.randint(0,1)
        if flip == 0:
            listOfValues.append("H")
        elif flip == 1:
            listOfValues.append("T")
    # Checking if there is a streak of 6 'heads' or 'tails'
    for i in range(0, len(listOfValues)):
        if listOfValues[i] == 'H':
            tails = 0
            heads += 1
            if heads == 6:
                heads = 0
                numberOfStreaks += 1
        elif listOfValues[i] == 'T':
            heads = 0
            tails += 1
            if tails == 6:
                numberOfStreaks += 1

    if numberOfStreaks != 0:
        streakBool += 1
print(f'Chance of streak: {streakBool/100}%')