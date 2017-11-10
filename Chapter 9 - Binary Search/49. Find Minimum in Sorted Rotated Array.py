# coding=utf-8
"""
Question:
Suppose a sorted array is rotated at some pivot unknown to you beforehand (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
You may assume no duplicate exists in the array.
"""

"""
O(log n) runtime, O(1) space

There are two cases for two elements:
A = [1, 2]
B = [2, 1]
For A, 1 < 2 => Am < Ar, and therefore it will set r = m => r = 0.
For B, 2 > 1 => Am > Ar, and therefore it will set l = m + 1 => l = 1. 
Therefore, it is clear that when l == r, we have found the minimum element.
"""
class Solution:
    def find_min(self, nums):
        """
        :type nums: [int]
        :rtype int
        """
        l, r = 0, len(nums) - 1
        while l < r and nums[l] >= nums[r]:
            m = (l + r) / 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]

if __name__ == '__main__':
    print Solution().find_min([3, 5, 6, 1, 2])
    print Solution().find_min([2, 3, 5, 9, 0, 1])
