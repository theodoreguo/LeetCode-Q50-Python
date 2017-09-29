# coding=utf-8
"""
Question:
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.
Hint:
First, make sure you understand what a palindrome means. A palindrome is a string which reads the same in both
directions. For example, “aba” is a palindrome, “abc” is not.
"""

"""
O(n2) runtime, O(1) space

We could solve it in O(n2) time using only constant space.

We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, 
and there are only 2n – 1 such centers.

You might be asking why there are 2n – 1 but not n centers? The reason is the center of a palindrome can be in between
two letters. Such palindromes have even number of letters (such as “abba”) and its center are between the two ‘b’s.

Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n2).
"""
class Solution(object):
    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand_around_center(s, left, right):
            chars = list(s)
            while left >= 0 and right < len(chars) and chars[left] == chars[right]:
                left -= 1
                right += 1

            return right - left - 1

        chars = list(s)
        start, end = 0, 0
        for i in xrange(len(chars)):
            length1 = expand_around_center(s, i, i)
            length2 = expand_around_center(s, i, i + 1)
            length = max(length1, length2)
            if length > end - start:
                start = i - (length - 1) / 2
                end = i + length / 2

        return ''.join(chars[start : end + 1])

if __name__ == '__main__':
    print Solution().longest_palindrome("abb")
    print Solution().longest_palindrome("aabaa")
    print Solution().longest_palindrome("abacdgfdcaba")
    print Solution().longest_palindrome("ddgcbaabcclj")
