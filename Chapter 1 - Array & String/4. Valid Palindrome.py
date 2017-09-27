# coding=utf-8
"""
Question:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome. "race a car" is not a palindrome.

Example Questions Candidate Might Ask:
Q: What about an empty string? Is it a valid palindrome?
A: For the purpose of this problem, we define empty string as valid palindrome.
"""

"""
The idea is simple, have two pointers – one at the head while the other one at the tail. 
Move them towards each other until they meet while skipping non-alphanumeric characters.
Consider the case where given string contains only non-alphanumeric characters. 
This is a valid palindrome because the empty string is also a valid palindrome.
"""
class Solution:
    def is_palindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True

if __name__ == '__main__':
    print Solution().is_palindrome("A man, a plan, a canal: Panama")
