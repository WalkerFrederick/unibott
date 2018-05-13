import random

def roll(commandArray):
    returningArray = []
    if len(commandArray) == 3:
        multiplier = int(commandArray[1])
        maxRoll = commandArray[2]
        if multiplier > 10:
            multiplier = 10
        while multiplier != 0:
            returningArray.append(random.randint(1,int(maxRoll)))
            multiplier = multiplier - 1;
        return returningArray
        print (returningArray)
    else:
        maxRoll = commandArray[1]
        returningArray.append(random.randint(1,int(maxRoll)))
        print (returningArray)
        return returningArray


#TESTER     
