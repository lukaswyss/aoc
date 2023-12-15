import os
import re

input =  open(os.getcwd() + '/aoc/2023/Day7/text.txt', 'r', encoding='utf-8').read().split("\n")

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2" , "J"]
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
    values = []
    possibleHands = []
    for card in hand:
        mock = hand
        y = ""
        for x in enumerate(mock):
            if x[1] == 'J':
                y += card
            else:
                y += x[1]
        if y not in possibleHands:
            possibleHands.append(y)
            
    for hand in possibleHands:
        count = [hand.count(x) for x in hand]
        if 5 in count:
            values.append(1) 
        elif 4 in count:
            values.append(2) 
        if 3 in count:
            if 2 in count:
                values.append(3) 
            values.append(4) 
        if count.count(2) == 4:
            values.append(5) 
        if 2 in count:
            values.append(6)
        else:
            values.append(7) 
    return min(values)
    

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