f = open("./2015/Day1/text1.txt", "r")
inputs = f.read()

floor = 0

for char in inputs:
    if char == '(':
        floor += 1
    else:
        floor -= 1

print(floor)
