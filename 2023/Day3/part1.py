import os
import re

current_directory = os.getcwd()

with open(current_directory + '/2023/Day3/text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

partNumbers = []

currentLineId = -1
len = len(lines) -1


def getPreviousAndNextLine(LineId):
    if LineId >= len:
        previousLine = lines[LineId - 1]
        nextLine = []
    elif LineId <= 0:
        nextLine = lines[LineId + 1]
        previousLine = []
    else:
        previousLine = lines[LineId - 1]
        nextLine = lines[LineId + 1]
    return [previousLine, nextLine]


for line in lines:
    currentLineId += 1
    previousLine, nextLine = getPreviousAndNextLine(currentLineId)
    # print(previousLine)
    print(line)
    # print(nextLine)
    # Finde alle ganzen Zahlen im String
    n = re.findall(r'\d+', line)
    numbers = [[]]
    id = -1
    for num in n:
        id + 1
        numbers[id].append(int(num))
        numbers[id].append(line.index(num))
        numbers[id].append(len(num))
    print(numbers)
    
    for num in numbers:
        num = "." + num + "."
    #for set in numbers:
        
    # Konvertiere die gefundenen Zahlen von Strings zu ganzen Zahlen und speichere sie in einem Array
    integer_array = [int(num) for num in numbers]






 
print(partNumbers)