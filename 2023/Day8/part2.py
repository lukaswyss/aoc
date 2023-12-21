import os
import functools

navigation, lines  =  open(os.getcwd() + '/aoc/2023/Day8/text.txt', 'r', encoding='utf-8').read().split("\n\n")

steps = []
lines = lines.split("\n")
currents = [i for i in lines if i[2]== "A"]

def kgve(numbers):
	return functools.reduce(lambda a,b: a * b // ggt([a, b]), numbers)
def ggt(numbers):
	for i in range(0, len(numbers)-1):
		while numbers[1]:      
			numbers[0], numbers[1] = numbers[1], numbers[0] % numbers[1]
		numbers[1] = numbers[i+1]
	return numbers[0]


for current in currents:
    current = current[0:3]
    while current.endswith != "Z":
        x = 0
        for step in navigation:
            line = [i for i in lines if i.startswith(current)][0]
            leftDestination = line[7:10]
            rightDestination = line[12:15]

            if step == "L":
                current = leftDestination
            if step == "R":
                current = rightDestination

            x += 1
        steps.append[x]


result = kgve(steps)
print(result)