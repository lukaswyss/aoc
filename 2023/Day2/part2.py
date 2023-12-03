import os

current_directory = os.getcwd()

with open(current_directory + '/2023/Day2/text1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

powers = []
colors = ["red", "green", "blue"]
lineId = 0

for line in lines:
    lineId += 1
    MinumumCubes = [0,0,0]
    firstchar = 8
    if lineId >= 10:
        firstchar += 1
        if lineId >= 100:
            firstchar += 1
    linesliced = line.strip()[firstchar:len(line)]
    sets = linesliced.split("; ")

    for set in sets:
        PickedColors = [0,0,0]
        cubes = set.split(", ")
        for cube in cubes:
            numberlength = cube.index(" ")
            number = int(cube[0:numberlength])
            cubecolor = cube[numberlength+1:len(cube)]
            index = colors.index(cubecolor)
            PickedColors[index] += number
            if (MinumumCubes[index] < number):
                MinumumCubes[index] = number

    powers.append(MinumumCubes[0] * MinumumCubes[1] * MinumumCubes[2])

print(sum(powers))

