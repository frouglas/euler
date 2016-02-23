'''

In England the currency is made up of pound and pence, p, 
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p).
It is possible to make 2 in the following way:

1 1 + 150p + 220p + 15p + 12p + 31p
How many different ways can 2 be made using any number of coins?

ANSWER: 73682

'''


lb2Yes = 0

runTot = 0 

for lb2 in range(0,2):
    runTot = round(200*lb2,0)
    if runTot==200:
        lb2Yes += 1
        if lb2 >= 1:
            print("holla 2 LB")
        #print(str(lb2) + " 2LB, Combinations found: " + str(lb2Yes))
        break
    uLim1Lb = int(round((200-runTot)/100,2))+1
    for lb1 in range(0, uLim1Lb):
        runTot = round(200*lb2 + 100*lb1,0)     
        if runTot==200:
            lb2Yes += 1
            if lb1 == 2:
                print("holla 1 LB")
            #print(str(lb2) + " 2LB, " + str(lb1) + " 1LB, Combinations found: " + str(lb2Yes))
            break
        uLim50p = int(round((200-runTot)/50,2))+1
        for p50 in range(0,uLim50p):
            runTot = round(200*lb2 + 100*lb1 + 50*p50,0)
            if runTot==200:
                lb2Yes += 1
                if p50 >= 4:
                    print("holla 50 p")
                #print(str(lb2) + " 2LB, " + str(lb1) + " 1LB, " + str(p50) + " 50p, Combinations found: " + str(lb2Yes))
                break
            uLim20p = int(round((200-runTot)/20,2))+1
            for p20 in range(0,uLim20p):
                runTot = round(200*lb2 + 100*lb1 + 50*p50 + 20*p20,0)
                if runTot==200:
                    lb2Yes += 1
                    if p20 >= 10:
                        print("holla 20 p") 
                    #print(str(lb2) + " 2LB, " + str(lb1) + " 1LB, " + str(p50) + " 50p, " + str(p20) + " 20p, Combinations found: " + str(lb2Yes))
                    break
                uLim10p = int(round((200-runTot)/10,2))+1
                for p10 in range(0,uLim10p):
                    runTot = round(200*lb2 + 100*lb1 + 50*p50 + 20*p20 + 10*p10,0)
                    if runTot==200:
                        lb2Yes += 1
                        #print(str(lb2) + " 2LB, " + str(lb1) + " 1LB, " + str(p50) + " 50p, " + str(p20) + " 20p, " + str(p10) + " 10p, Combinations found: " + str(lb2Yes))
                        if p10 >= 20:
                            print("holla 10 p")
                        break
                    uLim5p = int(round((200-runTot)/5,2)) + 1
                    for p5 in range(0,uLim5p):
                        runTot = round(200*lb2 + 100*lb1 + 50*p50 + 20*p20 + 10*p10 + 5*p5,0)
                        if runTot==200:
                            lb2Yes += 1
                            if p5>=40:
                                print("holla 5 p")
                            #print(str(lb2) + " 2LB, " + str(lb1) + " 1LB, " + str(p50) + " 50p, " + str(p20) + " 20p, " + str(p10) + " 10p, " + str(p5) + " 5p, Combinations found: " + str(lb2Yes))
                            break
                        uLim2p = int(round((200-runTot)/2,2))+1
                        for p2 in range(0,uLim2p):
                            runTot = round(200*lb2 + 100*lb1 + 50*p50 + 20*p20 + 10*p10 + 5*p5 + 2*p2,2)
                            if runTot == 200:
                                lb2Yes += 1
                                #print(str(lb2) + " 2LB, " + str(lb1) + " 1LB, " + str(p50) + " 50p, " + str(p20) + " 20p, " + str(p10) + " 10p, " + str(p5) + " 5p, " + str(p2) + " 2p, Combinations found: " + str(lb2Yes))
                                if p2 >= 100:
                                    print("holla 2 p")
                                break
                            else:
                                p1 = 200 - runTot
                                if p1>=200:
                                    print("holla 1 p")
                                lb2Yes += 1
                                #print(str(lb2) + " 2LB, " + str(lb1) + " 1LB, " + str(p50) + " 50p, " + str(p20) + " 20p, " + str(p10) + " 10p, " + str(p5) + " 5p, " + str(p2) + " 2p, " + str(p1) + " 1p, Combinations found: " + str(lb2Yes))

print(str(lb2Yes) + " Combinations Found")
            