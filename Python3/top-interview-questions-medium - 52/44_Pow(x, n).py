# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Easy solution
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

# math
# if n is odd:  x ** n = x(x **2 ) ** ((n-1) // 2)
# if n is even: x ** n =  (x ** 2) **  (n //2 )
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(x, n):
            if n == 0:
                return 1.0
            if n == 1:
                return x

            tmp = recur(x, n//2)
            if n % 2 == 0:
                return tmp * tmp
            else:
                return x * tmp * tmp
        
        res = recur(x, abs(n))
        return res if n>0 else 1/res