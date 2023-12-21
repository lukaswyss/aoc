import os
lines  =  open(os.getcwd() + '/2023/Day10/text.txt', 'r', encoding='utf-8').read().split("\n")
result = 0

def calculate(numbers, value): # calculate the last number of next list 
    if not all(i == numbers[0] for i in numbers):
        newNumbers = []
        for x, number in enumerate(numbers[:-1]):
            newNumbers.append( number - numbers[x + 1])
        value += newNumbers[0]
        return calculate(newNumbers, value )
    else:   
        return value

for line in lines:
    numbers = [int(s) for s in line.split()]
    resultInLine = calculate(numbers, numbers[0])
    result += resultInLine

print(result)