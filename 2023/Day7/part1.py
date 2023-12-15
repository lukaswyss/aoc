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

def convertToNumber(cardString):
    value = ""
    for char in cardString:
        value += str(cards.index(char) + 10)  
    return int(value) 

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

handsToAdd = [[], [], [], [], [], [], []]

for hand in hands:
    type = getType(hand[0])
    hand.append(convertToNumber(hand[0]))
    handsToAdd[type-1].append(hand)
        
for hands in handsToAdd:
    hands.sort(key=lambda x:x[2])
    for hand in hands:
        sortedHands.append(hand)

sortedHands.reverse()
for hand in sortedHands:
    val = (sortedHands.index(hand) + 1)
    totalwinnings += val * hand[1]
print(totalwinnings)