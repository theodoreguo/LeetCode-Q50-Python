# coding=utf-8
"""
Question:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Example Questions Candidate Might Ask:
Q: Is the empty string valid?
A: Yes.
"""

"""
O(n) runtime, O(n) space

To validate the parentheses, we need to match each closing parenthesis with its opening counterpart. A Last-In-First-Out 
(LIFO) data structure such as stack is the perfect fit.
As we see an opening parenthesis, we push it onto the stack. On the other hand, when we encounter a closing parenthesis, 
we pop the last inserted opening parenthesis from the stack and check if the pair is a valid match. Using dictionary is 
a maintainable way when matching parentheses.
"""
class Solution:
    def is_valid(self, s):
        """
        :type s: str
        :rtype bool
        """
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in lookup:
                stack.append(char)
            elif len(stack) == 0 or lookup[stack.pop()] != char:
                return False
        return len(stack) == 0

if __name__ == '__main__':
    print Solution().is_valid("()[]{}")
    print Solution().is_valid("()[{]}")
    print Solution().is_valid("(]")
    print Solution().is_valid("([)]")
