# coding=utf-8
"""
O(n) runtime, O(n) space

Question:
Design and implement a TwoSum class. It should support the following operations: add and find.

add(input) – Add the number input to an internal data structure.
find(value) – Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5); find(4) -> true; find(7) -> false
"""

from collections import defaultdict

class TwoSum(object):
    def __init__(self):
        """
        Initialize the internal data structure - dictionary.
        """
        self.lookup = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.lookup[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.lookup:
            target = value - key
            if key == target:
                # For duplicates, ensure there are at least two individual numbers,
                # e.g., double 2 sum to 4.
                if lookup[key] >= 2:
                    return True
            elif target in self.lookup:
                return True
            # One line implementation:
            # if target in self.lookup and (target != key or self.lookup[key] > 1):
            #     return True
        return False


if __name__ == '__main__':
    Sol = TwoSum()

    for i in (1, 3, 5):
        Sol.add(i)

    for i in (4, 7):
        print Sol.find(i)
