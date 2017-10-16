# coding=utf-8
"""
Question:
Similar to Question [43. Unique Paths], but now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space are marked as 1 and 0 respectively in the grid. For example,
There is one obstacle in the middle of a 3×3 grid as illustrated below.
 [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
 ]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

"""
O(mn) runtime, O(mn) space – Dynamic programming

Extend from the Bottom-up DP approach in Q43. Just set the total paths to 0 when you encounter an obstacle.
"""
class Solution:
    def unique_paths(self, obstacle_grid):
        """
        :type obstacle_grid: [[int]]
        :rtype int
        """
        m = len(obstacle_grid)
        if m == 0:
            return 0
        n = len(obstacle_grid[0])
        mat = [[0] * (n + 1) for _ in range(m + 1)]
        mat[m - 1][n] = 1
        r = m - 1
        while r >= 0:
            c = n - 1
            while c >= 0:
                mat[r][c] = 0 if obstacle_grid[r][c] == 1 else mat[r][c + 1] + mat[r + 1][c]
                c -= 1
            r -= 1
        return mat[0][0]

if __name__ == '__main__':
    a1 = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    a2 = [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0]
        ]
    print Solution().unique_paths(a1)
    print Solution().unique_paths(a2)
