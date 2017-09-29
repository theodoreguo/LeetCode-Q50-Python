# coding=utf-8
"""
Question:
Given two strings S and T, determine if they are both one edit distance apart.

Hint:
1. If | n – m | is greater than 1, we know immediately both are not one-edit distance apart.
2. It might help if you consider these cases separately, m == n and m ≠ n.
3. Assume that m is always ≤ n, which greatly simplifies the conditional statements. If m > n, we could just simply swap
   S and T.
4. If m == n, it becomes finding if there is exactly one modified operation. If m ≠ n, you do not have to consider the
   delete operation. Just consider the insert operation in T.
"""

"""
O(n) runtime, O(1) space – Simple one-pass

We make a first pass over S and T concurrently and stop at the first non-matching character between S and T.
1. If S matches all characters in T, then check if there is an extra character at the end of T. (Modify operation)
2. If | n – m | == 1, that means we must skip this non-matching character only in T and make sure the remaining 
   characters between S and T are exactly matching. (Insert operation)
3. If | n – m | == 0, then we skip both non-matching characters in S and T and make sure the remaining characters
   between S and T are exactly matching. (Append operation)
"""
class Solution(object):
    def is_one_edit_distance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if m > n:
            return self.is_one_edit_distance(t, s)
        if n - m > 1:
            return False

        i, shift = 0, n - m
        while i < m and s[i] == t[i]:
            i += 1

        # Append operation
        if i == m:
            return shift > 0

        # Modify operation
        if shift == 0:
            i += 1

        # Insert operation
        while i < m and s[i] == t[i + shift]:
            i += 1

        return i == m

if __name__ == '__main__':
    print Solution().is_one_edit_distance("teacher", "acher")
    print Solution().is_one_edit_distance("abacdfdcab", "abacdgfdcab")
