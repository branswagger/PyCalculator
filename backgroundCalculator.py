class backgroundCalculator():
    def calculateByString(self, stringToCalcBy):
        calcEqu = self.parseStringToEquation(stringToCalcBy)
        return self.solveEquation(calcEqu)

    def solveEquation(self, equation):
        lsModifers = ["*", "+", "-", "/"]

        solution = 0

        curFirstInt = None
        curSecondInt = None
        curMod = ""
        for variable in equation.variableList:
            if variable.variable not in lsModifers:
                if curFirstInt == None:
                    curFirstInt = int(variable.variable)
                else:
                    curSecondInt = int(variable.variable)
            else:
                curMod = variable.variable

        if curMod == "+":
            solution = curFirstInt + curSecondInt
        elif curMod == "-":
            solution = curFirstInt - curSecondInt
        elif curMod == "*":
            solution = curFirstInt * curSecondInt
        elif curMod == "/":
            solution = curFirstInt / curSecondInt

        return solution


    def parseStringToEquation(self, stringToParse):
        lsModifers = ["*", "+", "-", "/"]
        
        #create equ
        res = calcEquation()

        #split string
        listOfChars = list(stringToParse)

        #loop
        curVariable = None
        for curChar in listOfChars:
            if curVariable == None:
                curVariable = calcVariable()
            
            if curChar in lsModifers:
                res.variableList.append(curVariable)
                curVariable = calcVariable()
                curVariable.variable += str(curChar)
                res.variableList.append(curVariable)
                curVariable = None
            else:
                curVariable.variable += curChar

        if curVariable != None:
            res.variableList.append(curVariable)

        return res

class calcVariable():
    def __init__(self):
        self.variable = ""

class calcEquation(): 
    def __init__(self):
        self.variableList = []