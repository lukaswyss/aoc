import os
lines =  open(os.getcwd() + '/2023/Day9/text.txt', 'r', encoding='utf-8').read().split("\n")

for line in lines:
    numbers = line.split(" ")

    for i ,number in numbers:
        next = numbers[i + 1]
        value =  next - number
        print(value)


