import os
import math 
input  =  open(os.getcwd() + '/2023/Day11/text.txt', 'r', encoding='utf-8').read().split("\n")



def expand(grid):
    exdGrid = grid.copy()
    IndexInLineValid = []
    for index in range(len(grid[0])):
        IndexInLineValid.append([index, True])
    x = 0
    for i, line in enumerate(grid):
        if "#" not in line:
            exdGrid.insert(i + x,line)
            x += 1
        for idx, char in enumerate(line):
            if char == "#":
                IndexInLineValid[idx][1] = False
    for lineId, line in enumerate(exdGrid):
        added = 0
        for validIndex in IndexInLineValid:
            if validIndex[1] == True:
                line = line[:validIndex[0] + added] +  '.' + line[validIndex[0] + added:]
                added += 1
        exdGrid[lineId] = line
    return exdGrid

def getGalaxies(grid):
    galaxies = []
    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char == "#":
                galaxies.append([x, y])
    return galaxies

def getShortestDistance(glaxyOne, galaxyTwo):
    return math.dist([glaxyOne[0]], [galaxyTwo[0]]) + math.dist([glaxyOne[1]], [galaxyTwo[1]])


    

expendedGrid = expand(input)
galaxies = getGalaxies(expendedGrid)
result = 0
for i, galaxyOne in enumerate(galaxies):
    for galaxyTwo in galaxies[i+1:]:
        result += getShortestDistance(galaxyOne, galaxyTwo)
            

print(result)