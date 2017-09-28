# coding=utf-8
"""
Question:
Implement strStr().
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
""" 

"""
 O(nm) runtime, O(1) space – Brute force
 
i.   needle or haystack is empty. If needle is empty, always return 0. If haystack is empty, then there will
     always be no match (return –1) unless needle is also empty which 0 is returned.
ii.  needle’s length is greater than haystack’s length. Should always return –1. 
iii. needle is located at the end of haystack. For example, “aaaba” and “ba”. Catch possible off-by-one errors.
iv.  needle occur multiple times in haystack. For example, “mississippi” and “issi”. It should return index 2
     as the first match of “issi”.
v.   Imagine two very long strings of equal lengths = n, haystack = “aaa...aa” and needle = “aaa...ab”. You should
     not do more than n character comparisons, or else your code will get Time Limit Exceeded in OJ.
"""
class Solution(object):
    def strStr(self, haystack, needle):
            """
            :type haystack: str
            :type needle: str
            :rtype: int
            """
            
            for i in range(0, len(haystack) + 1):
                for j in range(0, len(needle) + 1):
                    if j == len(needle):
                        return i  # Looping through needle done
                    if i + j == len(haystack):
                        return -1  # needle’s length is greater than haystack’s length or no match
                    if (needle[j] != haystack[i + j]):
                        break  # Encounter non-matched character, break to next loop
            return -1

# O(nm) runtime, O(m) space
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in xrange(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
    
if __name__ == '__main__':
    print Solution().strStr("a", "")
    print Solution().strStr("abababcdab", "ababcdx")
    print Solution().strStr("mississippi", "issi")

    print Solution2().strStr("a", "")
    print Solution2().strStr("abababcdab", "ababcdx")
    print Solution2().strStr("mississippi", "issi")
