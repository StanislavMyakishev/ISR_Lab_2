from classes.calculator import Calculator
from classes.reader import Reader
from classes.writer import Writer
from classes.fileWriter import filewriter

class fileReader:
    """Reades input data from input() file name and calculates each expression
    """
    InitMessage = '*** Write input file name'
    inPath = ''
    outPath = ''
    isRPN = False
    isFIB = False
    isFAC = False
    CalcExpression = ''
    def readInPath(self):
        print(self.InitMessage)
        print('>>> ', end='')
        self.inPath = input()
    def doMath(self):
        if (self.inPath == ''):
            self.inPath = 'input.txt'
        f = open(self.inPath)
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
            w = filewriter(calculus, err, self.outPath)
            if (self.outPath == ''):
                self.outPath = w.openFile()
            w.printResult()
            self.isRPN = False
            self.isFIB = False
            self.isFAC = False