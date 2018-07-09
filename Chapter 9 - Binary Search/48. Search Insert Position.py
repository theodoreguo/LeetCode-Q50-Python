# coding=utf-8
"""
Question:
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
 [1, 3, 5, 6], 5 → 2
 [1, 3, 5, 6], 2 → 1
 [1, 3, 5, 6], 7 → 4
 [1, 3, 5, 6], 0 → 0
"""

"""
O(log n) runtime, O(1) space

It's a direct application of Binary Search, as the keywords sorted and finding target can be spotted easily.
When the while loop ends, l must be equal to r and it is a valid index.
If nums[l] is greater than target, that means we are inserting target before nums[l], so we return l. If nums[l] is less 
than target, that means we insert target after nums[l], so we return l + 1.
"""
class Solution:
    def search_insert(self, nums, target):
        """
        :type nums: [int]
        :type target: int
        :rtype int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) / 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l + 1 if nums[l] < target else l

class Solution2:
    def search_insert(self, nums, target):
        """
        :type nums: [int]
        :type target: int
        :rtype int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return len(nums)  # The position is to append after the last element

if __name__ == '__main__':
    print Solution().search_insert([1, 3, 5, 6], 7)
    print Solution().search_insert([2, 3, 5, 9], 3)
    print '-----' * 5
    print Solution2().search_insert([1, 3, 5, 6], 7)
    print Solution2().search_insert([2, 3, 5, 9], 3)
