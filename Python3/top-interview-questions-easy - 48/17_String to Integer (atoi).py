# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:

# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
class Solution:
    def myAtoi(self, str: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(str) == 0:
            return 0

        while pos < len(str):
            current_char = str[pos]
            if state == 0:
                if current_char == " ":
                    state = 0
                elif current_char == "+" or current_char == "-":
                    state = 1
                    sign = 1 if current_char == "+" else -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: 
            return 0

        first_char = -1
        first_num = -1
        end_num = -1
        value = "+-0123456789"
        for i in range(len(s)):                
            if (first_char == -1):
                first_char = i
            if (end_num != -1) and not (s[i] in value[2:]):
                break
            if s[i] in value[2:]:
                if first_num == -1:
                    first_num = i
                if (i != 0) and (s[i-1] in value[0:2]):
                    first_num = i-1
                end_num = i

        if first_char != first_num:
            return 0
        elif -(2**31)<= int(s[first_num:end_num+1]) <= (2**31 - 1):
            return (int(s[first_num:end_num+1]))
        elif s[first_num] == "-":
            return (-(2**31))
        else:
            return ((2**31 - 1))