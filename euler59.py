
import csv

def findKey(thisChar, thisLetter):
    thisKey = 0   
    for i in range(97,123):
        if chr(thisChar ^ i) == thisLetter:
            thisKey = i
            break
    return thisKey
    
coherentMessage = 0    
 

currKey = [0,0,0]
currK = 0
keyFound = 0

cipher = []

with open('/Volumes/TRANSFERS/gitHub/euler/support files/p059_cipher.txt', 'rb') as csvFile:
    reader = csv.reader(csvFile,delimiter = ',')
    for row in reader:
        cipher.extend(row)
    csvFile.close   
 
lastCheck = 0 
   
while coherentMessage == 0:    
    
    for i in range(lastCheck,len(cipher)-2):
        currK = findKey(int(cipher[i]), "a") 
        if currK == 0:
            currKey = [0,0,0]
            continue
        else:
            currKey[i % 3] = currK
            currK = findKey(int(cipher[i+1]),"n")
            if currK == 0:
                currKey = [0,0,0]
                continue
            else:
                currKey[(i+1) % 3] = currK
                currK = findKey(int(cipher[i+2]), "d")
                if currK == 0:
                    currKey = [0,0,0]
                    continue
                else:
                    currKey[(i+2) % 3] = currK
                    for j in range(0, len(cipher)-2):
                        if chr(int(cipher[j]) ^ currKey[j % 3]) == "t":
                            if chr(int(cipher[j+1]) ^ currKey[(j+1) % 3]) == "h":
                                if chr(int(cipher[j+2]) ^ currKey[(j+2) % 3]) == "e":
                                    print "potential key found!"
                                    keyFound = 1
                                    lastCheck = i + 1
                                    break
        if keyFound == 1:
            keyFound = 0
            break
    
    asciiTot = 0
    fullMess = ""
        
    for i in range(0,len(cipher)):
        thisChar = int(cipher[i]) ^ currKey[i % 3]
        asciiTot += thisChar
        fullMess = fullMess + chr(thisChar)
        
    print fullMess
    
    coherentMessage = input("does that look right? ")
    coherentMessage = int(coherentMessage)

print str(asciiTot)