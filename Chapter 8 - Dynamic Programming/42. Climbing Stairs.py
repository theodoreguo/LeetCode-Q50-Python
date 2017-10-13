# coding=utf-8
"""
Question:
You are climbing a staircase. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""



"""
O(n) runtime, O(1) space – Dynamic programming

Set base cases f(1) = 1, f(2) = 2.
We can calculate f(n) easily by storing previous values in an one dimension array and work our way up to n. Heck, we can 
even optimize this further by storing just the previous two values.
"""
class Solution:
    def climb_stairs(self, n):
        """
        :type n: int
        :rtype int
        """
        if n == 1:
            return 1
        p, q = 1, 1
        for _ in range(2, n + 1):
            temp = q
            q += p
            p = temp
        return q

"""
O(2^n) runtime, O(n) space

Define:
f(n) = number of ways climbing to the nth step. 
To reach to the nth step, only two choices available:
1. Advance one step from the n – 1th step.
2. Advance two steps from the n – 2th step.
Therefore, f(n) = f(n – 1) + f(n – 2), which is the exact same recurrence formula defined by the Fibonacci sequence 
(with different base cases, though).
Set base cases f(1) = 1, f(2) = 2.
"""
class Solution2:
    def climb_stairs(self, n):
        steps = [0] * (n + 1)
        return self.calc_ways(n, steps)

    def calc_ways(self, n, steps):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if steps[n] != 0:
            return steps[n]
        steps[n] = self.calc_ways(n - 1, steps) + self.calc_ways(n - 2, steps)
        return steps[n]

if __name__ == '__main__':
    print Solution().climb_stairs(1)
    print Solution().climb_stairs(2)
    print Solution().climb_stairs(6)
    print '-----' * 5
    print Solution2().climb_stairs(1)
    print Solution2().climb_stairs(2)
    print Solution2().climb_stairs(6)
