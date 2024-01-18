# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        if (-(2**31) <= x <= (2**31-1)) and x != 0:
            x = int(str(x)[::-1]) if x > 0 else int((str(x)[1:])[::-1]) * -1
            if (-(2**31) <= x <= (2**31-1)):
                return x
        return 0

class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT, MIN_INT = 2 ** 31 - 1, -2 ** 31
        reverse = 0

        while x != 0:
            if reverse > MAX_INT / 10 or reverse < MIN_INT / 10:
                return 0
            digit = x % 10 if x > 0 else x % -10
            reverse = reverse * 10 + digit
            # remove decimal
            x = math.trunc(x / 10)

        return reverse