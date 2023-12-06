import os
import re
current_directory = os.getcwd()

with open(current_directory + '/aoc/2023/Day5/text.txt', 'r', encoding='utf-8') as f:
    seeds, soiltoseed, soiltofertilizer, fertilizertowater, watertolight, lighttotemperature, temperaturetohumidity , humiditytolocation = f.read().split("\n\n")

seeds = [int(s) for s in re.findall(r'\d+',seeds)]
mapsstrings = [soiltoseed, soiltofertilizer, fertilizertowater, watertolight, lighttotemperature, temperaturetohumidity , humiditytolocation]
for mapstring in mapsstrings:
    id = mapsstrings.index(mapstring)
    line = mapstring.split(":\n")[1]
    lines = line.split("\n")
    maps = []
    for map in lines:
        mapnumbers= [int(s) for s in re.findall(r'\d+',map)]
        maps.append(mapnumbers)
    for seed in seeds:
        for map in maps:
            destinationrangestart = map[0]
            sourcerangestart = map[1]
            rangelength = map[2]
            if seed in range(sourcerangestart, sourcerangestart + rangelength -1):
                seeds[seeds.index(seed)] = seed - sourcerangestart + destinationrangestart

print(seeds)
print(min(seeds))

