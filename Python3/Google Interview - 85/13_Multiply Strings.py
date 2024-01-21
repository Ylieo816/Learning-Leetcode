# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Time complexity: O(M⋅N)
# Space complexity: O(M+N)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        N = len(num1) + len(num2)
        answer = [0] * N
        
        first, second = num1[::-1], num2[::-1]

        for idx1, digit1 in enumerate(first):
            for idx2, digit2 in enumerate(second):
                cur_idx = idx1 + idx2
                carry = answer[cur_idx]

                multiplication = int(digit1) * int(digit2) + carry
                answer[cur_idx] = multiplication % 10
                answer[cur_idx + 1] += multiplication // 10
        
        if answer[-1] == 0:
            answer.pop()

        return ''.join(str(digit) for digit in reversed(answer))


# Fast but wrong speculative answer
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for i in num1:
            n1 = n1*10 + (ord(i)-48)
        for i in num2:
            n2 = n2*10 + (ord(i)-48)
        return f"{n1*n2}"