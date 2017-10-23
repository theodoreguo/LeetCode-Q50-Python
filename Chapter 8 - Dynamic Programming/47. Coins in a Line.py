# coding=utf-8
"""
Question:
There are n coins in a line. (Assume n is even). Two players take turns to take a coin from one of the ends of the line
until there are no more coins left. The player with the larger amount of money wins.
1. Would you rather go first or second? Does it matter?
2. Assume that you go first, describe an algorithm to compute the maximum amount of money you can win.

Hints:
If you go first, is there a strategy you can follow which prevents you from losing? Try to consider how it matters when
the number of coins is odd vs. even.
"""

class Solution:
    MAX_N = 100
    def print_moves(self, P, A, N):
        """
        :type P: [[int]]
        :type A: [int]
        :type N: int
        :rtype None
        """
        m, n = 0, N - 1
        my_turn = True
        while m <= n:
            P1 = P[m + 1][n]
            P2 = P[m][n - 1]
            player = "I" if my_turn else "You"
            if P1 <= P2:
                str1 = str(m + 1)
                str2 = str(A[m])
                str_final = str1 + "(" + str2 + ")."
                print player + " take coin no." + str_final
                m += 1
            else:
                str1 = str(n + 1)
                str2 = str(A[n])
                str_final = str1 + "(" + str2 + ")"
                print player + " take coin no." + str_final
                n -= 1
            my_turn = not my_turn
        amount = str(P[0][N-1])
        print "The total amount of money (maximum) I get is " + amount + "."

    def max_money(self, A, N):
        """
        :type A: [int]
        :type N: int
        :rtype int
        """
        P = [[0] * self.MAX_N for _ in range(self.MAX_N)]
        for i in range(N):
            m, n = 0, i
            while n < N:
                a = P[m + 2][n] if (m + 2 <= N - 1) else 0
                b = P[m + 1][n - 1] if (m + 1 <= N - 1 and n - 1 >= 0) else 0
                c = P[m][n - 2] if (n - 2 >= 0) else 0
                P[m][n] = max(A[m] + min(a, b), A[n] + min(b, c))
                m += 1; n += 1
        self.print_moves(P, A, N)
        return P[0][N-1]

if __name__ == '__main__':
    a1 = [2, 1, 5, 2]
    n1 = 4
    print Solution().max_money(a1, n1)
