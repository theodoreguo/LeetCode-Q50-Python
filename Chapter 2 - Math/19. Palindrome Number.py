# coding=utf-8
"""
Question:
Determine whether an integer is a palindrome. Do this without extra space.

Example Questions Candidate Might Ask:
Q: Does negative integer such as –1 qualify as a palindrome?
A: For the purpose of discussion here, we define negative integers as non-palindrome.
"""

# O(1) runtime, O(1) space
class Solution:
    """
    :type x: int
    :rtype: bool
    """
    def is_palindrome(self, x):
        if x < 0:
            return False

        div = 1
        while x / div >= 10:  # Getting and chopping the first digit dispose
            div *= 10
        while x != 0:
            l = x / div  # Get the most left digit
            r = x % 10  # Get the most right digit
            if l != r:
                return False
            x = (x % div) / 10  # Chop off one digit from both ends (chop left end digit and then right one)
            div /= 100

        return True

# O(1) runtime, O(1) space
class Solution2:
    """
    :type x: int
    :rtype: bool
    """
    def is_palindrome(self, x):
        if x < 0:
            return False

        copy, reverse = x, 0

        while copy:
            reverse = reverse * 10 + copy % 10
            copy /= 10

        return x == reverse

if __name__ == '__main__':
    print Solution().is_palindrome(0)
    print Solution().is_palindrome(888)
    print Solution().is_palindrome(67876)

    print Solution2().is_palindrome(0)
    print Solution2().is_palindrome(888)
    print Solution2().is_palindrome(67876)