import functools

navigation, lines  =  open('C:/Desktop/aoc/aoc/2023/Day8/text.txt', 'r', encoding='utf-8').read().split("\n\n")
simultaneousSteps = []
lines = lines.split("\n")
startingLines = [i for i in lines if i[2]== "A"]

def kgve(numbers):
	return functools.reduce(lambda a,b: a * b // ggt([a, b]), numbers)
def ggt(numbers):
	for i in range(0, len(numbers)-1):
		while numbers[1]:      
			numbers[0], numbers[1] = numbers[1], numbers[0] % numbers[1]
		numbers[1] = numbers[i+1]
	return numbers[0]

for staringLine in startingLines:
    currentPosition = staringLine[0:3]
    steps = 0
    while currentPosition[2] != "Z":
        for step in navigation:
            line = [i for i in lines if i.startswith(currentPosition)][0]
            leftDestination = line[7:10]
            rightDestination = line[12:15]

            if step == "L":
                currentPosition = leftDestination
            if step == "R":
                currentPosition = rightDestination

            steps += 1
    simultaneousSteps.append(steps)


result = kgve(steps)
print(result)