f = open("./2015/Day2/text1.txt", "r")
lines = f.readlines()

boxes = lines
totalsqarefeet = 0

for box in boxes:

    size = [int(numeric_string) for numeric_string in box.split('x')]
    l = int(size[0])
    w = int(size[1])
    h = int(size[2])
    smallest = sorted(size)[0] * sorted(size)[1]

    sqarefeet = 2*l*w + 2*w*h + 2*h*l + smallest
    totalsqarefeet += sqarefeet

print(totalsqarefeet)