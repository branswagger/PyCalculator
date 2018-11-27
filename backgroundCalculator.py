#the backend logic to parse and solve Equations
class backgroundCalculator():

    #the only function that should really be called, it just parses then solves an equation
    def calculateByString(self, stringToCalcBy):
        calcEqu = self.parseStringToEquation(stringToCalcBy)
        return self.solveEquation(calcEqu)

    #all the difficult logic is here. Does all the math
    def solveEquation(self, equation):
        #create solution int for return
        solution = None
        
        #create a curMod to store what we are currently doing to our numbers
        curMod = ""

        #loop over variables in equation
        for variable in equation.variableList:
            #check if the variable is a modifer. Example: "+" or "-"
            if variable.isModifer == False:
                #if not a modifer, is the solution set to anything
                if solution == None:
                    #if not, set it to the current variable
                    solution = int(variable.value)
                else:
                    #else, parse the current int
                    curInt = int(variable.value)

                    #modify the solution with the modifer and the current variable as an int
                    if curMod == "+":
                        solution = solution + curInt
                    elif curMod == "-":
                        solution = solution - curInt
                    elif curMod == "*":
                        solution = solution * curInt
                    elif curMod == "/":
                        solution = solution / curInt
            else:
                #else, set current mod. Expect to use it on the next iteration of the loop
                curMod = variable.value

        return solution

    #converts a string Equation to an easier to program around Equation data structure
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
                #save current number
                res.variableList.append(curVariable)
                curVariable = calcVariable()

                #save mod
                curVariable.value += str(curChar)
                curVariable.isModifer = True
                res.variableList.append(curVariable)

                #null out for next loop
                curVariable = None
            else:
                curVariable.value += curChar

        #grab the last variable set during the end of the loop
        if curVariable != None:
            res.variableList.append(curVariable)

        return res

#Variable data structure
#Example of data it would hold: "3" or "+"
class calcVariable():
    def __init__(self):
        self.value = ""
        self.isModifer = False

#Equation data structure
#Example of data it would hold: "3+3"
class calcEquation(): 
    def __init__(self):
        self.variableList = []