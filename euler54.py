'''
Created on Aug 30, 2012

1 - High Card: Highest value card.
2 - One Pair: Two cards of the same value.
3 - Two Pairs: Two different pairs.
4 - Three of a Kind: Three cards of the same value.
5 - Straight: All cards are consecutive values.
6 - Flush: All cards of the same suit.
7 - Full House: Three of a kind and a pair.
8 - Four of a Kind: Four cards of the same value.
9 - Straight Flush: All cards are consecutive values of same suit.
10 - Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

How many hands does Player 1 win?

@author: frouglas
'''

def parseHand(arr1):
    numArray = [0 for i in range(0,13)]
    for i in range(0,len(arr1)):
        numArray[arr1[i]-2] += 1
    return numArray

def flush(arr1):
    suit = arr1[0]
    for i in range(1,len(arr1)):
        if arr1[i] != suit:
            return 0
    return 1

def value(arr1,arr2):
    handVal = ""
    if max(arr1) == 4:
        handVal = "8"
        cardVal = arr1.index(4)+2
        if cardVal < 10:
            handVal += "0" + str(cardVal)
        else:
            handVal += str(cardVal)
        remVal = arr1.index(1) + 2
        handVal += str(remVal)
    elif max(arr1) == 3:
        threeKind = str(arr1.index(3)+2)
        if len(threeKind) == 1:
            threeKind = "0" + threeKind
        try:
            loc = str(arr1.index(2)+2)
            if len(loc) == 1:
                loc = "0" + loc
            handVal = "7" + threeKind + loc
        except ValueError:
            handVal = "4" + str(threeKind)
            revHand = copy.copy(arr1)
            revHand.reverse()
            startLoc = 0
            for i in range(0,2):
                newLoc = revHand.index(1,startLoc)
                startLoc = newLoc + 1
                newLoc = str(14 - newLoc)
                if len(newLoc) == 1:
                    newLoc = "0" + newLoc
                handVal += newLoc                
    elif max(arr1) == 2:
        firstPr = str(arr1.index(2)+2)
        if len(firstPr) == 1:
                firstPr = "0" + firstPr
        try: 
            secPr = str(arr1.index(2,int(firstPr)-1)+2)
            if len(secPr) == 1:
                secPr = "0" + secPr
            fifth = str(arr1.index(1)+2)
            if len(fifth) == 1:
                fifth = "0" + fifth
            handVal = "3" + secPr + firstPr + fifth
        except ValueError:
            handVal = "2" + firstPr
            revHand = copy.copy(arr1)
            revHand.reverse()
            startLoc = 0
            for i in range(0,3):
                newLoc = revHand.index(1,startLoc)
                startLoc = newLoc + 1
                newLoc = str(14 - newLoc)
                if len(newLoc) == 1:
                    newLoc = "0" + newLoc
                handVal += newLoc
    else:
        strLen = 1
        startPt = arr1.index(1)
        straight = 1
        while(strLen<5):
            if arr1[startPt + 1] == 1:
                strLen += 1
                startPt += 1
                continue
            else:
                straight = 0
                break
        if straight==1:            
            if flush(arr2)==1:
                handVal = "9"
            else:
                handVal = "5"
            hiStr = str(arr1[startPt])
            if len(hiStr) == 1:
                    hiStr = "0" + hiStr
            handVal += hiStr
        else:
            if flush(arr2)==1:
                handVal = "6"
            else:
                handVal = "1"
            revHand = copy.copy(arr1)
            revHand.reverse()
            startLoc = 0
            for i in range(0,5):
                newLoc = revHand.index(1,startLoc)
                startLoc = newLoc + 1
                newLoc = str(14 - newLoc)
                if len(newLoc) == 1:
                    newLoc = "0" + newLoc
                handVal += newLoc
    while(len(handVal)<12):
        handVal += "0"
    return int(handVal)
                    
import copy     

f = open('/Users/frouglas/Documents/poker.txt','r')
cont = 1
i = 0
p1wins = 0

while (cont == 1):
    currLine = f.readline()
    i += 1
    p1Num = []
    p1Suit = []
    p2Num = []
    p2Suit = []
    for j in range(0,5):
        currCard = currLine[j*3]
        if currCard == "T":
            currCard = 10
        elif currCard == "J":
            currCard = 11
        elif currCard == "Q":
            currCard = 12
        elif currCard == "K":
            currCard = 13
        elif currCard == "A":
            currCard = 14
        else:
            currCard = int(currCard)
        p1Num.append(currCard)
        p1Suit.append(currLine[j*3+1])
    for j in range(5,10):
        currCard = currLine[j*3]
        if currCard == "T":
            currCard = 10
        elif currCard == "J":
            currCard = 11
        elif currCard == "Q":
            currCard = 12
        elif currCard == "K":
            currCard = 13
        elif currCard == "A":
            currCard = 14
        else:
            currCard = int(currCard)
        p2Num.append(currCard)
        p2Suit.append(currLine[j*3+1])
    parse1 = parseHand(p1Num)
    parse2 = parseHand(p2Num)
    handVal1 = value(parse1,p1Suit)
    handVal2 = value(parse2,p2Suit)
    if handVal1 > handVal2:
        p1wins += 1
        print("hand " + str(i) + ": player 1 wins, " + currLine[0:14] + " | " + currLine[15:len(currLine)-1])
        print("total hands won: " + str(p1wins))
        
        
    