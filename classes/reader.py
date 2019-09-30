#class Reader
# printInitMessage - prints a string 
# readCalcExpression - reads expr from input and checks if it RPN
# isRPN - returns RPN param
class Reader:
    InitMessage = '*** Write the calc expression\n*** Put "$" symbol first to calculate the expression in Reverse Polish notation\n*** If the expression is not in RPN - write the expression according to the template: "(arg1) (operation) (arg2)"\n*** Suported operations list: "+", "-", "*", "/", ' 
    CalcExpression = ''
    RPN = False
    def pringInitMessage(self):
        print(self.InitMessage)
    def readCalcExpression(self):
        OPERATORS = ['+', '-', '*', '/', ' ']
        print('>>> ', end='')
        self.CalcExpression = input()
        if (self.CalcExpression[0] == '$'):
            self.RPN = True
            self.CalcExpression = self.CalcExpression.replace('$', '')
        else: 
            if (len(self.CalcExpression.split(' ')) != 3):
                return 'The input expression is incorrect'
        for token in self.CalcExpression:
            if (not token.isdecimal() and not token in OPERATORS):
                return 'The input expression is incorrect'
        return  self.CalcExpression
    def isRPN(self):
        return self.RPN