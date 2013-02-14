__author__ = 'mauricio.antunes'

#TODO: create methods to convert the postfix convention to normal convention.

import unittest
import re

# Defines a dict of operators.
operators = {"+":int.__add__,
             "-":int.__sub__,
             "*":int.__mul__,
             "/":int.__truediv__,
             "^":int.__pow__}

class RPN(object):

    def validate_expression(self, expression):

        pieces = re.split(r"\s+", expression)
        stack = []
        for piece in pieces:
            # If it is a operator
            if piece in operators.keys():
                try:
                    op2 = stack.pop()
                    op1 = stack.pop()
                except IndexError:
                    raise BadNotation("Not enough operands for RPN validator.")
                piece = operators[piece](op1, op2)
            else:
                piece = int(piece)

            stack.append(piece)

        # Checks if only one operand was passed.
        if len(stack) == 1:
            return stack.pop()
        else:
            raise BadNotation("Operators missing in the following expression: '%s'" % expression)

    def infix2postfix(self, expression):
        pass

class RPNTest(unittest.TestCase):
    def test_expression(self):
        self.assertEqual(2+4, RPN().validate_expression("2 4 +"))
        self.assertEqual(3**3, RPN().validate_expression("3 3 * 3 *"))
        self.assertEqual(2+10, RPN().validate_expression("2 10 +"))
        self.assertNotEqual(5+5, RPN().validate_expression("5 5 +"))

    def test_bad_expression(self):
        self.assertRaises(BadNotation, RPN().validate_expression("test"))
        self.assertRaises(BadNotation, RPN().validate_expression("0 +"))
        self.assertRaises(BadNotation, RPN().validate_expression("+++++"))
        self.assertRaises(BadNotation, RPN().validate_expression("1 1 1 1 + - * / ^"))

class BadNotation(Exception):
    def __init__(self, expression):
        self._msg = "Bad notation at building the following notation: %s" % expression

    def _message(self):
        return self._msg
    #TODO: learn more about properties. It seems to be cool! (http://docs.python.org/3.3/library/functions.html#property).
    message = property(_message)

# Runs RPN
if __name__ == "__main__":
    unittest.main()