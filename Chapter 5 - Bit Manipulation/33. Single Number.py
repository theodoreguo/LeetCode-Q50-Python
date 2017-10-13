# coding=utf-8
"""
Question:
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example Questions Candidate Might Ask:
Q: Does the array contain both positive and negative integers?
A: Yes.
Q: Could any element appear more than twice?
A: No.
"""

"""
O(n) runtime, O(1) space

XOR-ing a number with itself is zero. If we XOR all numbers together, it would effectively cancel out all elements that 
appear twice leaving us with only the single number. As the XOR operation is both commutative and associative, the order 
in how you XOR them does not matter.
"""
class Solution:
    def single_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        for x in nums:
            num ^= x
        return num

if __name__ == '__main__':
    print Solution().single_number([2, 3, 6, 4, 4, 5, 3, 6, 2])
    print Solution().single_number([0, 6, 0])
