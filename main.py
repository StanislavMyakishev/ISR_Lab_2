from classes.calculator import Calculator
from classes.reader import Reader
from classes.writer import Writer

r = Reader()
r.pringInitMessage()
expr = r.readCalcExpression()
isRPN = r.isRPN()
isFIB = r.isFIB()
isFAC = r.isFAC()
c = Calculator(isRPN, isFIB, isFAC,  expr)
calculus = c.calc()
err = c.getErr()
w = Writer(calculus, err)
w.printResult()