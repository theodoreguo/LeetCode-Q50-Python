# coding=utf-8
"""
Question:
Validate if a given string is numeric. Some examples:
"0" -> true
"0.1" -> true
"abc" -> false

Example Questions Candidate Might Ask:
Q: How to account for whitespaces in the string?
A: When deciding if a string is numeric, ignore both leading and trailing whitespaces.
Q: Should I ignore spaces in between numbers – such as “1 1”?
A: No, only ignore leading and trailing whitespaces. “1 1” is not numeric.
Q: If the string contains additional characters after a number, is it considered valid?
A: No. If the string contains any non-numeric characters (excluding whitespaces and decimal point), it is not numeric.
Q: Is it valid if a plus or minus sign appear before the number?
A: Yes. “+1” and “-1” are both numeric.
Q: Should I consider only numbers in decimal? How about numbers in other bases such as hexadecimal (0xFF)?
A: Only consider decimal numbers. “0xFF” is not numeric.
Q: Should I consider exponent such as “1e10” as numeric?
A: No. But feel free to work on the challenge that takes exponent into consideration.
""" 

class InputType:
    INVALID    = 0
    SPACE      = 1
    SIGN       = 2
    DIGIT      = 3
    DOT        = 4
    EXPONENT   = 5

# O(n) runtime, O(1) space
class Solution(object):
    def valid_number(self, s):
        """
        :type s: str
        :rtype: bool
        """
        transition_table = [[-1, 0, 3, 1, 2, -1],  # next states for state 0
                            [-1, 8, -1, 1, 4, 5],  # next states for state 1
                            [-1, -1, -1, 4, -1, -1],  # next states for state 2
                            [-1, -1, -1, 1, 2, -1],  # next states for state 3
                            [-1, 8, -1, 4, -1, 5],  # next states for state 4
                            [-1, -1, 6, 7, -1, -1],  # next states for state 5
                            [-1, -1, -1, 7, -1, -1],  # next states for state 6
                            [-1, 8, -1, 7, -1, -1],  # next states for state 7
                            [-1, 8, -1, -1, -1, -1]]  # next states for state 8

        state = 0
        for char in s:
            inputType = InputType.INVALID
            if char.isspace():
                inputType = InputType.SPACE
            elif char == '+' or char == '-':
                inputType = InputType.SIGN
            elif char.isdigit():
                inputType = InputType.DIGIT
            elif char == '.':
                inputType = InputType.DOT
            elif char == 'e' or char == 'E':
                inputType = InputType.EXPONENT

            state = transition_table[state][inputType]

            if state == -1:
                return False

        return state == 1 or state == 4 or state == 7 or state == 8

class Solution2(object):
    def valid_number(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        return bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))

class Solution3(object):
    def remove_spaces(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        i = 0
        j = n - 1
        while i < n and s[i] == ' ':
            i += 1
        while j > -1 and s[j] == ' ':
            j -= 1
        return s[i:j+1]

    def valid_number(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = self.remove_spaces(s)
        n = len(s)

        if n == 0:
            return False

        i = 0

        hasDigit = False
        dotFlag = False
        eFlag = False
        hasSign = False

        while i < n:
            if s[i].isdigit():
                i += 1
                hasDigit = True
                hasSign = True
            elif not dotFlag and s[i] == '.':
                i += 1
                dotFlag = True
                hasSign = True
            elif hasDigit and not eFlag and (s[i] == 'e' or s[i] == 'E'):
                i += 1
                dotFlag = True
                eFlag = True
                hasDigit = False
                hasSign = False
            elif not hasDigit and not hasSign and (s[i] == '+' or s[i] == '-'):
                i += 1
                hasSign = True
            else:
                return False

        if hasDigit:
            return True
        else:
            return False

# Reference: https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA
class Solution4(object):
    def valid_number(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # define a DFA
        state = [{},
                 {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
                 {'digit': 3, '.': 4},
                 {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
                 {'digit': 5},
                 {'digit': 5, 'e': 6, 'blank': 9},
                 {'sign': 7, 'digit': 8},
                 {'digit': 8},
                 {'digit': 8, 'blank': 9},
                 {'blank': 9}]
        currentState = 1
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [3, 5, 8, 9]:
            return False
        return True

# Reference: https://leetcode.com/problems/valid-number/discuss/23739/Easy-Python-Solution-68-ms-beats-100
class Solution5(object):
    def valid_number(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True

if __name__ == '__main__':
    print Solution().valid_number(" 0.1 ")
    print Solution().valid_number("abc")
    print Solution().valid_number("1 a")
    print Solution().valid_number("2e10")
    print "*" * 10
    print Solution2().valid_number(" 0.1 ")
    print Solution2().valid_number("abc")
    print Solution2().valid_number("1 a")
    print Solution2().valid_number("2e10")
    print "*" * 10
    print Solution3().valid_number(" 0.1 ")
    print Solution3().valid_number("abc")
    print Solution3().valid_number("1 a")
    print Solution3().valid_number("2e10")
    print "*" * 10
    print Solution4().valid_number(" 0.1 ")
    print Solution4().valid_number("abc")
    print Solution4().valid_number("1 a")
    print Solution4().valid_number("2e10")
    print "*" * 10
    print Solution5().valid_number(" 0.1 ")
    print Solution5().valid_number("abc")
    print Solution5().valid_number("1 a")
    print Solution5().valid_number("2e10")
