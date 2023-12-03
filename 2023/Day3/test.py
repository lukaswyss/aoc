import os
import re

current_directory = os.getcwd()

with open(current_directory + '/2023/Day3/text.txt', 'r', encoding='utf-8') as f:
    input_data = f.readlines()

lines = []
for x in input_data:
    x = "." + x[:-1] + "."
    lines.append(x)

part_numbers = []
length = len(lines)

def get_previous(line_id):
    previous_line = "...."
    if line_id > 0:
        previous_line = lines[line_id - 1]
    return previous_line

def get_next(line_id):
    next_line = "...."
    if line_id < length - 1:
        next_line = lines[line_id + 1]
    return next_line

for line_id, line in enumerate(lines):
    previous_line = get_previous(line_id)
    next_line = get_next(line_id)

    for match in re.finditer(r'(\d+)', line):
        number = int(match.group(0))
        number_start = match.start(0)
        number_length = len(match.group(0))

        # Check surroundings for non-period characters
        is_valid = any(char != "." for char in previous_line[number_start - 1 :number_start + number_length + 2]) or \
                   any(char != "." for char in line[number_start - 1:number_start + number_length + 2]) or \
                   any(char != "." for char in next_line[number_start - 1:number_start + number_length + 2 ])

        if is_valid:
            part_numbers.append(number)

print(sum(part_numbers))
