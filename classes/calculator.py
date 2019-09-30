import operator

#class Calculator
# __init__ - gets boolean isRPN and string expr
# calcRPN - calcs RPN based on stack method
# calc - turns regular expr into RPN
class Calculator:
    """Calculator class - calcs given string expression in RPN or simple expression 
    
    Returns:
        numerical result or a bool -- bool err - true if an error occured, in that case numerical result is equal to zero
    """
    expr = []
    RPN = False
    err = True
    def __init__(self, RPN, expr):
        self.RPN = RPN
        self.expr = expr.split(' ')
    def calcRPN(self):
        OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        stack = [0]
        for token in self.expr:
            if token in OPERATORS:
                op2, op1 = stack.pop(), stack.pop()
                if (OPERATORS[token] != '/' and op2 != 0):
                    stack.append(OPERATORS[token](op1,op2))
                else:
                    return 0
            elif token == ' ':
                continue
            elif token:
                stack.append(int(token))
        self.err = False
        return stack.pop()
    def calc(self):
        if (self.RPN == True):
            self.result = self.calcRPN()
            return self.result
        else:
            self.expr = [self.expr[0], self.expr[2], self.expr[1]]
            self.result = self.calcRPN()
            return self.result
    def getErr(self):
        return self.err