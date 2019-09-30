from classes.calculator import Calculator
from classes.reader import Reader
from classes.writer import Writer

r = Reader()
r.pringInitMessage()
expr = r.readCalcExpression()
isRPN = r.isRPN()
isFIB = r.isFIB()
c = Calculator(isRPN, isFIB,  expr)
calculus = c.calc()
err = c.getErr()
w = Writer(calculus, err)
w.printResult()