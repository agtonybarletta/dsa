"""An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

 

Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
Example 2:

Input: n = 1
Output: 3
Example 3:

Input: n = 10101
Output: 183236316
"""
from unittest import TestCase 
from functools import cache 

class Solution:
    def checkRecord(self, n: int) -> int:
        """
            rule 1 no more that two A
            AAPP -> not eligible
            APPP -> elibigle
            rule 2 no 3 or more consecutives L
            LLLP -> not eligible
            LLPL -> eligible

            Sub problem
            at index i, 
            given the amount of possible A
            give the substring cannot end with more that #L
            return the number of possible eligible

            eligibiles(i, a, l) = eligibiles(i-1, a, l -1) + eligibiles(i-1, a-1, L) + eligibiles(i-1, a, L)
        """
        L = 3 
        A = 2
        MOD = 10**9 + 7

        # we always look at i-1 
        memo = [ [1]*(L+1) for _ in range(A+1)]
        for a in range(A+1):
            for l in range(L+1):
                if a == 0 or l == 0:
                    memo[a][l] = 0

        for i in range(n):
            old_memo = [l.copy() for l in memo]
            for a in range(1,A+1):
                for l in range(1, L+1):
                    memo[a][l] = old_memo[a][L]
                    memo[a][l] += old_memo[a-1][L]
                    memo[a][l] += old_memo[a][l-1]
                    memo[a][l] = memo[a][l] %MOD
        return memo[A][L] % MOD

        """
        working soluction, memory limited exceeded
        @cache
        def eligibles(i, a, l):
            if a == 0:
                return 0
            if l == 0:
                return 0
            if i == 0:
                return 1
            ans = eligibles(i-1, a, L)
            ans += eligibles(i-1, a-1, L)
            ans += eligibles(i-1, a, l-1)
            return ans % MOD
        return eligibles(n, A, L)
        """


if __name__ == "__main__":
    n = 2
    expected = 8
    #n =1
    #expected = 3
    output = Solution().checkRecord(n)
    TestCase().assertEqual(expected, output)
