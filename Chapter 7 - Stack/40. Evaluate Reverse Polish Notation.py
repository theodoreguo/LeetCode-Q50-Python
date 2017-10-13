# coding=utf-8
"""
Question:
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

Example Questions Candidate Might Ask:
Q: Is an empty array a valid input?
A: No.
"""

# O(n) runtime, O(n) space
import operator

class Solution:
    def eval_RPN(self, tokens):
        """
        :type tokens: [str]
        :rtype int
        """
        numerals, operators = [], {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        for token in tokens:
            if token not in operators:
                numerals.append(int(token))
            else:
                y, x = numerals.pop(), numerals.pop()
                numerals.append(int(operators[token](x * 1.0, y)))
        return numerals.pop()

if __name__ == '__main__':
    print Solution().eval_RPN(["2", "1", "+", "3", "*"])
    print Solution().eval_RPN(["4", "13", "5", "/", "+"])
    print Solution().eval_RPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
