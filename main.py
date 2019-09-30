from classes.calculator import Calculator
from classes.reader import Reader
from classes.writer import Writer

r = Reader()
r.pringInitMessage()
expr = r.readCalcExpression()
isRPN = r.isRPN()
c = Calculator(isRPN, expr)
calculus = c.calc()
err = c.getErr()
w = Writer(calculus, err)
w.printResult()