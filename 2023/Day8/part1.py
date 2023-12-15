import os
import re

navigation, lines  =  open(os.getcwd() + '/aoc/2023/Day8/text.txt', 'r', encoding='utf-8').read().split("\n\n")

steps = 0
current = "AAA"
lines = lines.split("\n")

while current != "ZZZ":
    for step in navigation:
        line = [i for i in lines if i.startswith(current)][0]
        leftDestination = line[7:10]
        rightDestination = line[12:15]

        if step == "L":
            current = leftDestination
        if step == "R":
            current = rightDestination

        steps += 1
print(steps)