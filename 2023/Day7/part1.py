import os
import re

input =  open(os.getcwd() + '/aoc/2023/Day7/text.txt', 'r', encoding='utf-8').read().split("\n")

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
hands = []
for x in input:
    y, c= x.split(" ")
    hands.append([y, int(c)])

sortedHands = [] 
totalwinnings = 0


def getType(hand):
    counts = [hand.count(card) for card in hand]
    if 5 in counts:
        return 1
    elif 4 in counts:
        return 2
    if 3 in counts:
        if 2 in counts:
            return 3
        return 4
    if counts.count(2) == 4:
        return 5
    if 2 in counts:
        return 6
    return 7
    


for hand in hands:
    type = getType(hand[0])
    if not sortedHands:
        sortedHands.append([hand[0], hand[1], type])
    else:
        for sortedHand in sortedHands:
            if type == sortedHand[2]:
                sortedHand.insert(1, [hand[0], hand[1], type])
            if type 

for hand in sortedHands:
    totalwinnings += hand[1] * hand[2]
print(totalwinnings)