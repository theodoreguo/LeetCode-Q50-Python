# coding=utf-8
"""
Question:
Given a number represented as an array of digits, plus one to the number.

Example Questions Candidate Might Ask:
Q: Could the number be negative?
A: No. Assume it is a non-negative number.
Q: How are the digits ordered in the list? For example, is the number 12 represented by [1,2] or [2,1]?
A: The digits are stored such that the most significant digit is at the head of the list.
Q: Could the number contain leading zeros, such as [0,0,1]?
A: No.
"""

# O(n) runtime, O(1) space
class Solution:
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    def plus_one(self, digits):
        i = len(digits) - 1
        while i >= 0:
            digit = digits[i]
            if digit < 9:
                digits[i] = digit + 1
                return digits
            else:
                digits[i] = 0
                i -= 1

        # Handle the edge case where each digit of the number is 9
        digits.append(0)
        digits[0] = 1

        return digits

if __name__ == '__main__':
    print Solution().plus_one([9, 9, 9, 9, 9])
    print Solution().plus_one([1, 0, 0])
    print Solution().plus_one([8, 7, 5])