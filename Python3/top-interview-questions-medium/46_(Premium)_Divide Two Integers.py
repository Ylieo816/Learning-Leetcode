# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign, answer = 1, 0
        if dividend == 0 or abs(dividend) < abs(divisor):
            return 0
        elif (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1

        dividend, divisor = abs(dividend), abs(divisor)

        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                dividend -= (divisor << i)
                answer += (1 << i)

        if sign == 1:
            if answer > (2**31 - 1):
                # return MAX
                return 2**31 - 1
            else:
                return answer
        else:
            # return -answer
            return (answer - answer - answer)