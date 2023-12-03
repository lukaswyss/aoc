import os
import re

current_directory = os.getcwd()

with open(current_directory + '/2023/Day3/text.txt', 'r', encoding='utf-8') as f:
    input = f.readlines()

lines = []
partNumbers = []
currentLineId = -1

for x in input:
    x = "." + x[:-1] + "."
    lines.append(x)

len = len(lines) -1

def getPrevious(LineId):
    previousLine = ""
    if LineId > 0:
        previousLine = lines[LineId - 1]
    return previousLine

def getNext(LineId):
    nextLine = ""
    if LineId < len:
        nextLine = lines[LineId + 1]
    return nextLine


for line in lines:
    currentLineId += 1
    previousLine = getPrevious(currentLineId)
    nextLine = getNext(currentLineId)
    n = re.findall(r"\d+", line)
    numbers = []    
    for number in n:
        num = int(number)
        numberlength = 1
        if num >= 10:
            numberlength = 2
        if num >= 100:
            numberlength = 3
        if num >= 1000:
            numberlength = 4
        if num >= 10000:
            numberlength = 5
        numbers.append((number, line.index(number), numberlength))  # Updated line

    for number in numbers:
        isValid = False
        isNeg = False
        p = previousLine[number[1]-1:number[1]+number[2]+1]
        n = nextLine[number[1]-1:number[1]+number[2]+1]
        for char in p:
            if char != ".":
                isValid = True
        for char in n:
            if char != ".":
                isValid = True
        if line[number[1]-1] != "." or line[number[1] + number[2]] != ".":
            isValid = True
        if line[number[1]-1] == "-":
            isNeg = True
        if isValid and not isNeg:
            partNumbers.append(int(number[0]))
        elif isValid and isNeg:
            partNumbers.append(int(number[0]))

print(sum(partNumbers))