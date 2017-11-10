# coding=utf-8
"""
Question:
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand (i.e., 0 1 2 4 5 6 7 might
become 4 5 6 7 0 1 2).
Find the minimum element.
The array may contain duplicates.
"""

"""
O(log n) runtime, O(1) space

For case where Al == Am == Ar, the minimum could be on Am’s left or right side (e.g., [1, 1, 1, 0, 1] or 
[1, 0, 1, 1, 1]). In this case, we could not discard either subarrays and therefore such worst case degenerates to the 
order of O(n).
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
            elif nums[m] < nums[l]:
                r = m
            else:  # nums[l] == nums[m] == nums[r]
                l = l + 1
        return nums[l]

if __name__ == '__main__':
    print Solution().find_min([1, 1, 1, 0, 1])
    print Solution().find_min([2, 2, 3, 5, 9, 0, 0, 1])
