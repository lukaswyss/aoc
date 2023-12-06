import os
import re
x, y =  open(os.getcwd() + '/aoc/2023/Day6/text.txt', 'r', encoding='utf-8').read().split("\n")

timestring = x.replace(" ", "")
distancestring = y.replace(" ", "")
times = [int(s) for s in re.findall(r'\d+',timestring)]
distances = [int(s) for s in re.findall(r'\d+',distancestring)]
races = []
numbersofwayrtobeattherecord = 0

for time in times:
    idx = times.index(time)
    races.append([time, distances[idx]])

for x in races:
    time = x[0]
    distance = x[1]
    for milicecond in range(time):
        TimeButtonWasHold = milicecond
        TimeTraveled = time - milicecond
        speed = TimeButtonWasHold

        isCorect = time == TimeButtonWasHold + TimeTraveled
        if TimeTraveled * speed > distance:
            numbersofwayrtobeattherecord += 1
print(numbersofwayrtobeattherecord)
