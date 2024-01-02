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
        if x == 0:
            return 0
        elif x > 0:
            flag = 1
        else:
            flag = -1
        
        x = list(str(abs(x)))
        s = ""
        for i in range(len(x)):
            s += x[len(x) - i - 1]
        s = flag * int(s)
        
        if (-(2**31)<=s<= (2**31-1)):
            return s
        else:
            return 0
            

        