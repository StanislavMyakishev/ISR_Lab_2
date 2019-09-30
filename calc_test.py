from classes.calculator import Calculator
from classes.reader import Reader
from classes.writer import Writer
from unittest.mock import patch
import unittest

class Test_Calculator(unittest.TestCase):
    def test_readerRPN(self):
        r = Reader()
        user_input = ['$5 5 +']
        expected_output = '5 5 +'
        with patch('builtins.input', side_effect=user_input):
            output = r.readCalcExpression()
        self.assertEqual(output, expected_output)
    def test_readerWrongInput(self):
        r = Reader()
        user_input = ['#5 5 +']
        expected_output = 'The input expression is incorrect'
        with patch('builtins.input', side_effect=user_input):
            output = r.readCalcExpression()
        self.assertEqual(output, expected_output)
    def test_readerNotRPN(self):
        r = Reader()
        user_input = ['5 + 5']
        expected_output = '5 + 5'
        with patch('builtins.input', side_effect=user_input):
            output = r.readCalcExpression()
        self.assertEqual(output, expected_output)
    def test_readerWrongTypeInput(self):
        r = Reader()
        user_input = ['5 + 5 + 5']
        expected_output = 'The input expression is incorrect'
        with patch('builtins.input', side_effect=user_input):
            output = r.readCalcExpression()
        self.assertEqual(output, expected_output)
    def test_CalculatorRPN(self):
        r = Reader()
        expr = '7 2 3 * -'
        isRPN = True
        c = Calculator(isRPN, expr)
        output = c.calc()
        expected_output = 1
        self.assertEqual(output, expected_output)
    def test_CalculatorNormal(self):
        r = Reader()
        expr = '6 * 5'
        isRPN = False
        c = Calculator(isRPN, expr)
        output = c.calc()
        expected_output = 30
        self.assertEqual(output, expected_output)
    def test_Writer(self):
        calculus = 30
        err = False
        w = Writer(calculus, err)
        output = w.printResult()
        expected_output = True
        self.assertEqual(output, expected_output)
    def test_WriterErr(self):
        calculus = 30
        err = True
        w = Writer(calculus, err)
        output = w.printResult()
        expected_output = '*** The expression was not calculated succsesfully'
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()