# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# If multiple answers are possible, return any of them.

# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        answer = ""
        # check sigh
        if (numerator < 0) ^ (denominator < 0):
            answer += "-"
        numerator, denominator = abs(numerator), abs(denominator)

        # add Integer part
        answer += str(numerator // denominator)
        if numerator % denominator == 0:
            return answer

        answer += '.'
        # Use a dictionary to store the position of each remainder
        remainder_dict = {}
        remainder = numerator % denominator

        # Keep adding the remainder to the result until it repeats or the remainder becomes 0
        while remainder != 0 and remainder not in remainder_dict:
            remainder_dict[remainder] = len(answer)
            remainder *= 10
            answer += str(remainder // denominator)
            remainder %= denominator

        if remainder in remainder_dict:
            answer = answer[:remainder_dict[remainder]] + "(" + answer[remainder_dict[remainder]:] + ")"

        return answer