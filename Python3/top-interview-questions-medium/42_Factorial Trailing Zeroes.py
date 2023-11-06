# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Find the pattern and find out how many 5's there are in the number to determine the number of 0's in the end.
        # For example: 5!=120 has one 0, 25! contains 5, 10,15,20,25(5*5), so there are six 0s
        pattern, cnt = 5, 0
        while pattern <= n:
            cnt += (n // pattern)
            pattern *= 5
        return cnt