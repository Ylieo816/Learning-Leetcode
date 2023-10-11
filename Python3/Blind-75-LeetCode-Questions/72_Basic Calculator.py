# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

class Solution:
    def calculate(self, s: str) -> int:
        sign, answer, num = 1, 0, 0
        stack = []

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-':
                answer += num * sign
                sign = -1 if c == '-' else 1
                num = 0
            elif c == '(':
                stack.append(answer)
                stack.append(sign)
                answer = 0
                sign = 1
            elif c == ')':
                answer += sign * num
                answer *= stack.pop()
                answer += stack.pop()
                num = 0
        return answer + num * sign