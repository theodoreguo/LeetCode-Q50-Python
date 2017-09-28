# coding=utf-8
"""
Question:
Similar to Question [6. Reverse Words in a String], but with the following constraints:
“The input string does not contain leading or trailing spaces and the words are always separated by a single space.”
Could you do it in-place without allocating extra space?
""" 

# O(n) runtime, O(1) space – In-place reverse
class Solution(object):
    def reverse_words(self, s):
        """
        :type s: a list consisting of a string's characters (List[str])
        :rtype: nothing
        """
        def __reverse_string(s, start, end):
            for i in xrange((end - start) / 2):
                s[start + i], s[end - 1 - i] = s[end - 1 - i], s[start + i]

        __reverse_string(s, 0, len(s))
        i = 0
        for j in xrange(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                __reverse_string(s, i, j)
                i = j + 1

if __name__ == '__main__':
    s = ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']
    Solution().reverse_words(s)
    print s
