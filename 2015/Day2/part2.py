f = open("./2015/Day2/text1.txt", "r")
lines = f.readlines()

boxes = lines
totalribbon = 0

for box in boxes:

    size = [int(numeric_string) for numeric_string in box.split('x')]
    l = int(size[0])
    w = int(size[1])
    h = int(size[2])
    smallesttwo = sorted(size)[0] , sorted(size)[1]

    ribbon = w * h * l + sum(smallesttwo) * 2

    totalribbon += ribbon

print(totalribbon)