# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# - I can be placed before V (5) and X (10) to make 4 and 9. 
# - X can be placed before L (50) and C (100) to make 40 and 90. 
# - C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

# Time complexity : O(1)
# Space complexity : O(1)
class Solution:
    def intToRoman(self, num: int) -> str:
        table = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
        # or list
        # symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        # values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        answer = ''
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while n <= num:
                answer += table[n]
                num -= n
        return answer

# Time complexity : O(1)
# Space complexity : O(1)
class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        values = [1000, 500, 100, 50, 10, 5, 1]
        ptr = 0
        answer = ''
        while num > 0:
            if num < values[ptr]:
                ptr += 1
                continue
            
            if str(num)[0] == '4':
                answer += symbols[ptr] + symbols[ptr - 1]
                num = num + values[ptr] - values[ptr - 1]
            elif str(num)[0] == '9':
                answer += symbols[ptr + 1] + symbols[ptr - 1]
                num = num + values[ptr + 1] - values[ptr - 1]
            else:
                answer += symbols[ptr]
                num -= values[ptr]
        return answer