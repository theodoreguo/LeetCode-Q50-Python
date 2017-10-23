# coding=utf-8
"""
Question:
Find the contiguous subarray within an array of integers that has the largest product. For example, given the array
[2, 3, -2, 4], the contiguous subarray [2, 3] has the largest product = 6.

Example Questions Candidate Might Ask:
Q: Could the subarray be empty?
A: No, the subarray must contain at least one number.
"""

"""
O(n) runtime, O(1) space – Dynamic programming

This problem is very similar to Q45.
Besides keeping track of the largest product, we also need to keep track of the smallest product since the smallest 
product which is the largest in the negative sense could become the maximum when being multiplied by a negative number.

Let us denote that:
f(k) = Largest product subarray, from index 0 up to k.
Similarly,
g(k) = Smallest product subarray, from index 0 up to k.
Then,
f(k) = max(f(k - 1) * nums[k], nums[k], g(k - 1) * nums[k]),
g(k) = min(g(k - 1) * nums[k], nums[k], f(k - 1) * nums[k]).
There we have a dynamic programming formula. Using two arrays of size n, we could deduce the final answer as f(n - 1). 
Since we only need to access its previous elements at each step, two variables are sufficient.
"""
class Solution:
    def max_subarray(self, nums):
        """
        :type obstacle_grid: [int]
        :rtype int
        """
        max_product, min_product, max_ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            mx, mn = max_product, min_product
            max_product = max(max(nums[i], mx * nums[i]), mn * nums[i])
            min_product = min(min(nums[i], mx * nums[i]), mn * nums[i])
            max_ans = max(max_product, max_ans)
        return max_ans

if __name__ == '__main__':
    a1 = [2, 3, -2, 4]
    print Solution().max_subarray(a1)

    a2 = [1, 2, -1, -4, -3, 4]
    print Solution().max_subarray(a2)
