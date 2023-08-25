# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 1:
            while(n % 3 == 0):
                n /= 3
        return n == 1

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        i = 1
        while( i < n):
            i *= 3
        return i == n