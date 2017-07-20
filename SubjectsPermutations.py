class Choice:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.visited = False

def generateNext(table):
    nextPerm = {}

    for i in range(len(table)):
        if(allFalseInList(table[i])):
            nextPerm[table[i][0].name] = table[i][0].code
            table[i][0].visited = True
        elif(allTrueInTable(table[i+1:])):
            setAllFalse(table[(i+1):])
            firstFalse = firstFalseIndex(table[i])
            nextPerm[table[i][firstFalse].name] = table[i][firstFalse].code
            table[i][firstFalse].visited = True
        else:
            lastTrue = lastTrueIndex(table[i])
            nextPerm[table[i][lastTrue].name] = table[i][lastTrue].code

    return nextPerm

def allFalseInList(choicesList):
    for choice in choicesList:
        if(choice.visited == True):
            return False
    return True

def allTrueInTable(table):
    for row in table:
        for choice in row:
            if(choice.visited == False):
                return False
    return True

def setAllFalse(table):
    for row in table:
        for choice in row:
            choice.visited = False

def firstFalseIndex(choicesList):
    for i in range(len(choicesList)):
        if(choicesList[i].visited == False):
            return i
def lastTrueIndex(choicesList):
    for i in range(len(choicesList)-1):
        if(choicesList[i+1].visited == False):
            return i
    return len(choicesList)-1
