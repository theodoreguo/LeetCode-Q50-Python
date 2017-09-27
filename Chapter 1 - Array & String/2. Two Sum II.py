
"""
O(n) runtime, O(n) space

Question:
Similar to Question [1. Two Sum], except that the input array is already sorted in ascending order.
"""

class Solution(object):
    """
    O(n) runtime, O(1) space – Tow pointers
    Let’s assume we have two indices pointing to the ith and jth elements, Ai and Aj respectively. The sum of Ai and Aj could only fall into one of these three possibilities:
    i. Ai + Aj > target. Increasing i isn’t going to help us, as it makes the sum even bigger. Therefore we should decrement j.
    ii. Ai + Aj < target. Decreasing j isn’t going to help us, as it makes the sum even smaller. Therefore we should increment i.
    iii. Ai + Aj == target. We have found the answer.
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        
        while i < j:
            sum = nums[i] + nums[j]
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            else:
                return [i, j]

        return []

if __name__ == '__main__':
    print Solution().twoSum([3, 5, 7, 12, 23], 28)
