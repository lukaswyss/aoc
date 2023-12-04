import os
import re

current_directory = os.getcwd()

with open(current_directory + '/aoc/2023/Day4/text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

scratchcards = [] #card , instances
count = 0

for index,input in enumerate(lines):
    scratchcards.append([index + 1, 1])

for line in scratchcards:
    lineId = line[0] -1
    value = line[1]
    line = lines[lineId].split("\n")
    line = line[0].split(":")[1]
    winningNumbers= [int(s) for s in re.findall(r'\d+',line.split("|")[0])]
    numbersYouHave= [int(s) for s in re.findall(r'\d+',line.split("|")[1])]
    matching = set(winningNumbers) & set(numbersYouHave)
    x= len(matching)

    for index in range(0, x):
        if len(scratchcards) > index + 1:
            scratchcards[index + lineId + 1][1] += value

for record in scratchcards:
    count += record[1]
print(count)