# coding=utf-8
"""
Question:
Given a string S, find the length of the longest substring T that contains at most two distinct characters.
For example,
Given S = “eceba”,
T is "ece" which its length is 3.
"""

# O(n) runtime, O(1) space
class Solution(object):
    def longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len, i, distinct_count, visited = 0, 0, 0, [0 for _ in xrange(256)]
        for j, char in enumerate(s):
            if visited[ord(char)] == 0:
                distinct_count += 1
            visited[ord(char)] += 1

            while distinct_count > 2:
                visited[ord(s[i])] -= 1
                if visited[ord(s[i])] == 0:
                    distinct_count -= 1
                i += 1

            max_len = max(j - i + 1, max_len)

        return max_len

if __name__ == '__main__':
    print Solution().longest_substring("eceba")
    print Solution().longest_substring("tmtmtuxt")
    print Solution().longest_substring("abaac")
