#class Reader
# printInitMessage - prints a string 
# readCalcExpression - reads expr from input and checks if it RPN
# isRPN - returns bool sequence param
class Reader:
    """Reads from console
    Returns:
        string -- returns string expression and bool type of expression
    """
    InitMessage = '*** RELEASE v-1.0 ***\n*** Write the calc expression\n*** Put "$" symbol first to calculate the expression in Reverse Polish notation\n*** If the expression is not in RPN - write the expression according to the template: "(arg1) (operation) (arg2)"\n*** Suported operations list: "+", "-", "*", "/" \n*** Put "F" before a number to calc n-th Fibonacci sequence number\n*** Put "!" before a number to calc factorial of number'
    CalcExpression = ''
    FIB = False
    RPN = False
    FAC = False
    def pringInitMessage(self):
        print(self.InitMessage)
    def readCalcExpression(self):
        OPERATORS = ['+', '-', '*', '/', ' ']
        print('>>> ', end='')
        self.CalcExpression = input()
        if (self.CalcExpression[0] == '$'):
            self.RPN = True
            self.CalcExpression = self.CalcExpression.replace('$', '')
        elif (self.CalcExpression[0] == 'F'):
            self.FIB = True
            self.CalcExpression = self.CalcExpression.replace('F', '')
            self.CalcExpression = self.CalcExpression.replace(' ', '')
        elif (self.CalcExpression[0] == '!'):
            self.FAC = True
            self.CalcExpression = self.CalcExpression.replace('!', '')
            self.CalcExpression = self.CalcExpression.replace(' ', '')
        else: 
            if (len(self.CalcExpression.split(' ')) != 3):
                return 'The input expression is incorrect'
        for token in self.CalcExpression:
            if (not token.isdecimal() and not token in OPERATORS):
                return 'The input expression is incorrect'
        return  self.CalcExpression
    def isFAC(self):
        return self.FAC
    def isRPN(self):
        return self.RPN
    def isFIB(self): 
        return self.FIB