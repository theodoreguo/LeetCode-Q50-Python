# coding=utf-8
"""
Question:
A robot is located at the top-left corner of a m × n grid (marked ‘Start’ in the diagram below). The robot can only move
either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked
‘Finish’ in the diagram below). How many possible unique paths are there?

Note: m and n will be at most 100.
"""

"""
O((m + n, n)) runtime, O(m + n) space – Backtracking

When you reach row = m and col = n, you know you’ve reached the bottom-right corner, and there is one additional unique 
path to it. 
However, when you reach row > m or col > n, then it’s an invalid path and you should stop traversing. 
For any grid at row = r and col = c, you have two choices: Traverse to the right or traverse to the bottom. 
Therefore, the total unique paths at grid (r, c) are equal to the sum of total unique paths from the grid to the right 
and the grid below.
"""
class Solution:
    def unique_paths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype int
        """
        return self.backtrack(0, 0, m, n)

    def backtrack(self, r, c, m, n):
        """
        :type r: int
        :type c: int
        :type m: int
        :type n: int
        rtype int
        """
        if r == m and c == n - 1:
            return 1
        if r >= m or c >= n:
            return 0
        return self.backtrack(r + 1, c, m, n) + self.backtrack(r, c + 1, m, n)

"""
Improved Backtracking Solution using Memorization (top-down dynamic programming):
Although the above backtracking solution is easy to code, it is very inefficient in the sense that it recalculates the 
same solution for a grid over and over again. By caching the results, we prevent recalculation and only calculate when 
necessary. Here, we are using a dynamic programming (DP) technique called memorization.
"""
class Solution2:
    def unique_paths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype int
        """
        mat = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                mat[i][j] = -1
        return self.backtrack(0, 0, m, n, mat)

    def backtrack(self, r, c, m, n, mat):
        """
        :type r: int
        :type c: int
        :type m: int
        :type n: int
        :type mat: [[int]]
        rtype int
        """
        if r == m - 1 and c == n - 1:
            return 1
        if r >= m or c >= n:
            return 0
        if mat[r + 1][c] == -1:
            mat[r + 1][c] = self.backtrack(r + 1, c, m, n, mat)
        if mat[r][c + 1] == -1:
            mat[r][c + 1] = self.backtrack(r, c + 1, m, n, mat)
        return mat[r + 1][c] + mat[r][c + 1]

"""
O(mn) runtime, O(mn) space – Bottom-up dynamic programming

Bottom-up dynamic programming:
The total unique paths at grid (r, c) are equal to the sum of total unique paths from grid to the right (r, c + 1) and 
the grid below (r + 1, c).
It's observed that all grids of the bottom edge and right edge must all have only one unique path to the bottom-right 
corner. Using this as the base case, we can build our way up to our solution at grid (1, 1) using the relationship above.
"""
class Solution3:
    def unique_paths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype int
        """
        mat = [[0] * (n + 1) for _ in range(m + 1)]
        mat[m - 1][n] = 1
        r = m - 1
        while r >= 0:
            c = n - 1
            while c >= 0:
                mat[r][c] = mat[r + 1][c] + mat[r][c + 1]
                c -= 1
            r -= 1
        return mat[0][0]

if __name__ == '__main__':
    print Solution().unique_paths(2, 2)
    print Solution().unique_paths(6, 2)
    print '-----' * 5
    print Solution2().unique_paths(2, 2)
    print Solution2().unique_paths(6, 2)
    print '-----' * 5
    print Solution3().unique_paths(2, 2)
    print Solution3().unique_paths(6, 2)
