# coding=utf-8
"""
Question:
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

"""
The general version of the question would be:
Given an array of integers, every element appears k times except for one. Find that single one who appears l times.
 
We need a array x[i] with size k for saving the bits appears i times.
For every input number a, generate the new counter by x[j] = (x[j - 1] & a) | (x[j] & ~a).
Except x[0] = (x[k] & a) | (x[0] & ~a).
 
In the equation, the first part indicates the the carries from previous one.
The second part indicates the bits not carried to next one.
 
Then the algorithms run in O(kn) and the extra space O(k).
 
Refer to Solution2 for the implementation.
"""
class Solution:
    def single_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x0, x1 , x2 = ~0, 0, 0
        for i in range(len(nums)):
            t = x2
            x2 = (x1 & nums[i]) | (x2 & ~nums[i])
            x1 = (x0 & nums[i]) | (x1 & ~nums[i])
            x0 = (t & nums[i]) | (x0 & ~nums[i])

        return x1

class Solution2:
    def single_number(self, nums, k, l):
        """
        :type nums: List[int]
        :type k: int
        :type l: int
        :rtype: int
        """
        x = [0] * k
        x[0] = ~0
        for i in range(len(nums)):
            t = x[k - 1]
            j = k - 1
            while j > 0:
                x[j] = (x[j - 1] & nums[i]) | (x[j] & ~nums[i])
                j -= 1
            x[0] = (t & nums[i]) | (x[0] & ~nums[i])
        return x[l]

if __name__ == '__main__':
    print Solution().single_number([2, 2, 6, 4, 4, 5, 6, 6, 2, 4])
    print Solution().single_number([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2])
    print '-----' * 10
    print Solution2().single_number([2, 2, 6, 4, 4, 5, 6, 6, 2, 4], 3, 1)
    print Solution2().single_number([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2], 3, 1)
