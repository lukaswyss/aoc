import os

current_directory = os.getcwd()

with open(current_directory + '\Day1\\text1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

total = 0

for line in lines:
    digits = [char for char in line if char.isdigit()]
    if (len(digits) != 0):
        value = int(digits[0] + digits[-1])
        total += value


print(total)


