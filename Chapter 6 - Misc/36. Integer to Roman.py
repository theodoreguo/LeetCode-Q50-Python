# coding=utf-8
"""
Question:
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.

Hint:
What is the range of the numbers?

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

# O(mn) runtime, O(1) space
class Solution(object):
    def int_to_roman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numeral_map = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        keyset, result = sorted(numeral_map.keys()), []

        while num > 0:
            for key in reversed(keyset):
                while num / key > 0:
                    num -= key
                    result += numeral_map[key]

        return "".join(result)

if __name__ == '__main__':
    print Solution().int_to_roman(19)
    print Solution().int_to_roman(899)
    print Solution().int_to_roman(999)
    print Solution().int_to_roman(3999)
