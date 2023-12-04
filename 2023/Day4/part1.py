import os
import re

current_directory = os.getcwd()

with open(current_directory + '/aoc/2023/Day4/text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

total = 0

for line in lines:
    line = line.split("\n")
    line = line[0].split(":")[1]
    winningNumbers= [int(s) for s in re.findall(r'\d+',line.split("|")[0])]
    numbersYouHave= [int(s) for s in re.findall(r'\d+',line.split("|")[1])]
    matching = set(winningNumbers) & set(numbersYouHave)
    value = 0
    if len(matching) > 0:
        value = 1
        ele = matching.pop()
        for e in matching:
            value *= 2           
    total += value
    
print(total)

