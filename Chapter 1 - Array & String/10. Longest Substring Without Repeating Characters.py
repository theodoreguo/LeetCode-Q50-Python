# coding=utf-8
"""
Question:
Given a string, find the length of the longest substring without repeating characters. For example, the longest
substring without repeating letters for “abcabcbb” is “abc”, which the length is 3. For “bbbbb” the longest substring
is “b”, with the length of 1.
"""

# O(n) runtime, O(1) space – Two iterations
class Solution(object):
    def longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = list(s)
        exist = {}
        i, max_len = 0, 0
        for j in xrange(len(chars)):
            while exist.get(chars[j]):
                exist[chars[i]] = False
                i += 1
            exist[chars[j]] = True
            max_len = max(j - i + 1, max_len)
        return max_len

# O(n) runtime, O(1) space
class Solution2(object):
    def longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len, i, visited = 0, 0, [False for _ in xrange(256)]
        for j, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[i]:
                    visited[ord(s[i])] = False
                    i += 1
                i += 1
            else:
                visited[ord(char)] = True
            max_len = max(j - i + 1, max_len)
        return max_len

if __name__ == '__main__':
    print Solution().longest_substring("abcabcbb")
    print Solution().longest_substring("tmmzuxt")
    print Solution().longest_substring("pwwkew")

    print Solution2().longest_substring("abcabcbb")
    print Solution2().longest_substring("tmmzuxt")
    print Solution2().longest_substring("pwwkew")