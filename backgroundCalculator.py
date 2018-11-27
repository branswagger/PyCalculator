class backgroundCalculator():
    def calculateByString(self, stringToCalcBy):
        calcEqu = self.parseStringToEquation(stringToCalcBy)
        return "23"

    def parseStringToEquation(self, stringToParse):
        #create equ
        res = calcEquation()

        #split string
        listOfChars = list(stringToParse)

        #loop
        curVariable = None
        for curChar in listOfChars:
            if curVariable = None:
                curVariable = calcVariable()
            
            

        return res

class calcVariable():
    variable = ""

class calcEquation():
    calcList = []