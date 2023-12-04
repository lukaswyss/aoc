f = open("./2015/Day1/text1.txt", "r")
inputs = f.read()

floor = 0
char = 0

for x in inputs:
    char += 1
    if x == '(':
        floor += 1
    else:
        floor -= 1

    if floor == -1:
        print(char)

print(floor)
