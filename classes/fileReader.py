from classes.calculator import Calculator
from classes.reader import Reader
from classes.writer import Writer
from classes.fileWriter import fileWriter

class fileReader:
    InitMessage = '*** Write file name'
    FilePath = ''
    isRPN = False
    isFIB = False
    isFAC = False
    CalcExpression = ''
    def readFilePath(self):
        print(self.InitMessage)
        print('>>> ', end='')
        self.FilePath = input()
    def doMath(self):
        if (self.FilePath == ''):
            self.FilePath = 'input.txt'
        f = open(self.FilePath)
        OPERATORS = ['+', '-', '*', '/', ' ']
        for line in f:
            self.CalcExpression = line.replace('\n', '')
            if (self.CalcExpression[0] == '$'):
                self.isRPN = True
                self.CalcExpression = self.CalcExpression.replace('$', '')
            elif (self.CalcExpression[0] == 'F'):
                self.isFIB = True
                self.CalcExpression = self.CalcExpression.replace('F', '')
                self.CalcExpression = self.CalcExpression.replace(' ', '')
            elif (self.CalcExpression[0] == '!'):
                self.isFAC = True
                self.CalcExpression = self.CalcExpression.replace('!', '')
                self.CalcExpression = self.CalcExpression.replace(' ', '')
            else:
                if (len(self.CalcExpression.split(' ')) != 3):
                    print('The input expression is incorrect')
                for token in self.CalcExpression:
                    if (not token.isdecimal() and not token in OPERATORS):
                        print('The input expression is incorrect')
            c = Calculator(self.isRPN, self.isFIB, self.isFAC, self.CalcExpression)
            calculus = c.calc()
            err = c.getErr()
            w = fileWriter(calculus, err)
            w.printResult()