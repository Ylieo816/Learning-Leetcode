# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = True
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9 and flag:
                digits[i] += 1
                flag = False
            elif digits[i] == 9 and flag:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
        return digits

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         num = ""
#         for i in range(len(digits)):
#             num += str(digits[i])
#         newNum = str(int(num)+1)
#         c = []
#         for i in range(len(newNum)):
#             c.append(int(newNum[i]))
#         return c