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

class Solution2:
    # @param s, a string
    # @return a string
    def reverse_words(self, s):
        new_string = ''
        j = len(s)
        # iterate the string in a reversed order
        for i in range(len(s) - 1, -1, -1):
            # trim the trailing space
            if s[i] == ' ':
                j = i
            # if we encountered a " " before the worlds, we know a word ended here, append " " or the word
            elif i == 0 or s[i - 1] == ' ':
                if len(new_string) != 0:
                    new_string += ' '
                new_string += s[i:j]
        return new_string

if __name__ == '__main__':
    print Solution().reverse_words(' the  sky is   blue ')
    print Solution2().reverse_words(' the  sky is   blue ')
