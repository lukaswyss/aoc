import os
import re

current_directory = os.getcwd()

with open(current_directory + '/2023/Day3/text.txt', 'r', encoding='utf-8') as f:
    input = f.readlines()

lines = []
for x in input:
    x = "." + x[:-1] + "."
    lines.append(x)
partNumbers = []
currentLineId = -1
len = len(lines)

def getPrevious(LineId):
    previousLine = "...."
    if LineId > 0:
        previousLine = lines[LineId - 1]
    return previousLine

def getNext(LineId):
    nextLine = "...."
    if LineId < len -1:
        nextLine = lines[LineId + 1]
    return nextLine


for line in lines:
    currentLineId += 1
    previousLine = getPrevious(currentLineId)
    nextLine = getNext(currentLineId)
    n = re.findall(r'\d+', line)
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
        n =     nextLine[number[1]-1:number[1]+number[2]+1]
        x = line[number[1]-1:number[1]+number[2]]
        y = line[number[1]-1:number[1]+number[2]+ 1]
        
        for char in p:
            if char != ".":
                isValid = True
        for char in n:
            if char != ".":
                isValid = True
        if line[number[1]-1] != "." or line[number[1] + number[2]] != ".":
            isValid = True
        if isValid:
            partNumbers.append(int(number[0]))

        # print(p)
        # print(line[number[1]-1:number[1]+number[2]+ 1])
        # print(n)
        # print(isValid)
        #elif isValid and isNeg:
            #partNumbers.append(-int(number[0]))

print(sum(partNumbers))