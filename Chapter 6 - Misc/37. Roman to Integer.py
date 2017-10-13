# coding=utf-8
"""
Question:
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.

Roman literals and its decimal representations:
Roman Literal  Decimal
      I           1
      V           5
      X           10
      L           50
      C           100
      D           500
      M           1000
"""

"""
O(mn) runtime, O(1) space

Step by step calculation of roman numeral "MXCVI":
Roman literals from left to right  Accumulated total
M                                  1000
MX                                 1000 + 10 = 1010
MXC                                1010 + (100 – 2 * 10) = 1010 + 80 = 1090
MXCV                               1090 + 5 = 1095
MXCVI                              1095 + 1 = 1096
"""
class Solution:
    def roman_to_int(self, s):
        """
        :type s: str
        :rtype: int
        """
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        decimal = 0
        for i in range(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
                decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
            else:
                decimal += numeral_map[s[i]]
        return decimal

if __name__ == '__main__':
    print Solution().roman_to_int("MXCVI")
    print Solution().roman_to_int("XIX")
    print Solution().roman_to_int("DCCCXCIX")
    print Solution().roman_to_int("CMXCIX")
    print Solution().roman_to_int("MMMCMXCIX")
