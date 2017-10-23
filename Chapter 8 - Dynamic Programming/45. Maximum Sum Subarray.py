# coding=utf-8
"""
Question:
Find the contiguous subarray within an array (containing at least one number) that has the largest sum.
For example, given the array [2, 1, –3, 4, –1, 2, 1, –5, 4], the contiguous array [4, –1, 2, 1] has the largest sum = 6.
"""

"""
O(n) runtime, O(1) space – Dynamic programming

To devise a dynamic programming formula, let us assume that we are calculating the maximum sum of subarray that ends at 
a specific index.

Let's denote that:
f(k) = Maximum sum of subarray ending at index k.
Then, f(k) = max(f(k - 1) + nums[k], nums[k]).
Using an array of size n, we could deduce the final answer by as f(n – 1), with the initial state of f(0) = A[0]. Since 
we only need to access its previous element at each step, two variables are sufficient.
Notice the difference between the two: maxEndingHere and maxSoFar; the former is the maximum sum of subarray that must 
end at index k, while the latter is the global maximum subarray sum.
"""
class Solution:
    def max_subarray(self, nums):
        """
        :type obstacle_grid: [int]
        :rtype int
        """
        max_ending_here, max_so_far = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_ending_here, max_so_far)
        return max_so_far

if __name__ == '__main__':
    a1 = [2, 1, -3, 4, -1, 2, 1, -5, 4]
    print Solution().max_subarray(a1)

    a2 = [1, 2, -1, -4, 3, 4]
    print Solution().max_subarray(a2)
