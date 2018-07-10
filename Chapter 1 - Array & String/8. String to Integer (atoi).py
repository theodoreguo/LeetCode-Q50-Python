# coding=utf-8
"""
Question:
Implement atoi to convert a string to an integer.

The atoi function first discards as many whitespace characters as necessary until the first non-whitespace character is
found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no
effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of
representable values, the maximum integer value (2147483647) or the minimum integer value (–2147483648) is returned.
""" 

# O(n) runtime, O(1) space
class Solution(object):
    def string_to_integer(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        result = 0

        if not s:
            return result

        # Trim spaces
        i = 0
        while i < len(s) and s[i].isspace():
            i += 1

        # Sign dispose
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        # Boundary value handling
        while i < len(s) and s[i] >= '0' and s[i] <= '9':
            if result > (INT_MAX - (ord(s[i]) - ord('0'))) / 10:
                return INT_MAX if sign > 0 else INT_MIN
            result = result * 10 + ord(s[i]) - ord('0')
            i += 1

        return sign * result

if __name__ == '__main__':
    print Solution().string_to_integer("")
    print Solution().string_to_integer("-1")
    print Solution().string_to_integer("2147483647")
    print Solution().string_to_integer("2147483648")
    print Solution().string_to_integer("-2147483648")
    print Solution().string_to_integer("-2147483649")
    print Solution().string_to_integer(" -3647804 790 9")
    print Solution().string_to_integer("race a car7")
    print Solution().string_to_integer("64rd9")
