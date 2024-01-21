# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# 1. Read in and ignore any leading whitespace.
# 2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# 3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# 4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# 5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# 6. Return the integer as the final result.

# Note:
# - Only the space character ' ' is considered a whitespace character.
# - Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

# Deterministic Finite Automaton (DFA)
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def myAtoi(self, s: str) -> int:
        answer, position, state, sign = 0, 0, 0, 1
        if len(s) == 0: return 0

        while position < len(s):
            c = s[position]
            # 0: start and check start with ' ' or '+-' or num
            if state == 0:
                if c == ' ':
                    state = 0
                elif c == '+' or c == '-':
                    state = 1
                    sign = 1 if c == '+' else -1
                elif c.isdigit():
                    state = 2
                    answer = answer * 10 + int(c)
                else:
                    return 0
            # 1: after +-, calcul num
            elif state == 1:
                if c.isdigit():
                    state = 2
                    answer = answer * 10 + int(c)
                else:
                    return 0
            # 2: keep num
            elif state == 2:
                if c.isdigit():
                    state = 2
                    answer = answer * 10 + int(c)
                else:
                    break
            else:
                return 0
            position += 1

        answer *= sign
        answer = min(answer, 2**31 -1)
        answer = max(answer, -(2**31))
        return answer