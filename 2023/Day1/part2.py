import os
current_directory = os.getcwd()

with open(current_directory + '\Day1\\texttwo.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total = 0
for line in lines:
    indexes = [] # 1, 2
    digits = [char for char in line if char.isdigit()] # 1, 2
    
    for digit in digits:
        indexes.append([line.find(digit), digit])

    matches = [] # 4, 3, (four, three)
    for number in numbers:
        if number in line:
            matches.append(numbers.index(number))
    for match in matches:
        indexes.append([line.find((numbers[match])), str(match)])

    indexesSorted= sorted(indexes, key=lambda x: x[0])
    indexesSliced = indexesSorted[0], indexesSorted[len(indexesSorted)-1]
    resultstring = (indexesSliced[0][1] + indexesSliced[-1][1]) 
    total += int(resultstring)    

print(total)





