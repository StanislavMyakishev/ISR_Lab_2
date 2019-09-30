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
    FIB = False
    FAC = False
    err = True
    def __init__(self, RPN, FIB, FAC, expr):
        self.FAC = FAC
        self.RPN = RPN
        self.FIB = FIB
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
    def calcFac(self):
        if len(self.expr) != 1:
            self.err = True
            return 0
        else: 
            self.err = False
            num = int(self.expr[0])
            if num > 9000:
                print('IT IS OVER 9000')
                self.err = True
                return 0
            i = 1
            while num >= 1:
                i = i * num
                num -= 1
            return i
    def calcFib(self):
        if len(self.expr) != 1:
            self.err = True
            return 0
        else: 
            self.err = False
            num = int(self.expr[0])
            if num == 0:
                return 0
            elif num == 1 or num == 2:
                return 1
            elif num > 2:
                a = 1
                b = 1
                for _ in range(3, num + 1):
                    c = a + b
                    a, b = b, c
                return c
    def calc(self):
        if (self.RPN == True):
            self.result = self.calcRPN()
            return self.result
        elif (self.FIB == True): 
            self.result = self.calcFib()
            return self.result
        elif (self.FAC == True):
            self.result = self.calcFac()
            return self.result
        else:
            self.expr = [self.expr[0], self.expr[2], self.expr[1]]
            self.result = self.calcRPN()
            return self.result
    def getErr(self):
        return self.err