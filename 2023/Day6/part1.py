import os
import re

timestring, distancestring =  open(os.getcwd() + '/aoc/2023/Day6/text.txt', 'r', encoding='utf-8').read().split("\n")

times = [int(s) for s in re.findall(r'\d+',timestring)]
distances = [int(s) for s in re.findall(r'\d+',distancestring)]
races = []
numbersofwayrtobeattherecord = []
result = 1
for time in times:
    idx = times.index(time)
    races.append([time, distances[idx]])

for x in races:
    time = x[0]
    distance = x[1]
    beatRecords = 0
    for milicecond in range(time):
        TimeButtonWasHold = milicecond
        TimeTraveled = time - milicecond
        speed = TimeButtonWasHold
        isCorect = time == TimeButtonWasHold + TimeTraveled
        if TimeTraveled * speed > distance:
            beatRecords += 1
    numbersofwayrtobeattherecord.append(beatRecords)

for x in numbersofwayrtobeattherecord:
    result *= x

print(numbersofwayrtobeattherecord)
print(result)