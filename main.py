from classes.calculator import Calculator
from classes.reader import Reader
from classes.writer import Writer
from classes.fileReader import fileReader
from classes.fileWriter import filewriter

fr = fileReader()
fr.readFilePath()
fr.doMath()
# r = Reader()
# r.pringInitMessage()
# expr = r.readCalcExpression()
# isRPN = r.isRPN()
# isFIB = r.isFIB()
# isFAC = r.isFAC()
# c = Calculator(isRPN, isFIB, isFAC,  expr)
# calculus = c.calc()
# err = c.getErr()
# w = Writer(calculus, err)
# w.printResult()