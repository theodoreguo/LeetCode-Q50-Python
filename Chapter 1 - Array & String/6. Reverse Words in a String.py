# coding=utf-8
"""
Question:
Given an input string s, reverse the string word by word.
For example, given s = "the sky is blue", return "blue is sky the".

Example Questions Candidate Might Ask:
Q: What constitutes a word?
A: A sequence of non-space characters constitutes a word.
Q: Does tab or newline character count as space characters?
A: Assume the input does not contain any tabs or newline characters.
Q: Could the input string contain leading or trailing spaces?
A: Yes. However, your reversed string should not contain leading or trailing spaces.
Q: How about multiple spaces between two words?
A: Reduce them to a single space in the reversed string.
""" 

# O(n) runtime, O(n) space
class Solution:
    # @param s, a string
    # @return a string
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

if __name__ == '__main__':
    print Solution().reverse_words(' the  sky is   blue ')