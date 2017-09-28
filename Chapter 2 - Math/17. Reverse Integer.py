# coding=utf-8
"""
Question:
Reverse digits of an integer. For example: x = 123, return 321.

Example Questions Candidate Might Ask:
Q: What about negative integers?
A: For input x = –123, you should return –321.
Q: What if the integer’s last digit is 0? For example, x = 10, 100, ...
A: Ignore the leading 0 digits of the reversed integer. 10 and 100 are both reversed as 1.
Q: What if the reversed integer overflows? For example, input x = 1000000003.
A: In this case, your function should return 0.
"""

# O(n) runtime, O(1) space
class Solution(object):
    def reverse_integer(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0

        if x < 0:
            return -self.reverse_integer(-x)

        while x != 0:
            # Handle overflow/underflow
            if abs(res) > 214748364:
                return 0
            res = res * 10 + x % 10
            x /= 10
        return res

if __name__ == '__main__':
    print Solution().reverse_integer(1244343)
    print Solution().reverse_integer(100)
    print Solution().reverse_integer(-123)