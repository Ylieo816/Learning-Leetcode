# Given two integers a and b, return the sum of the two integers without using the operators + and -.


# The adder is just an XOR + AND
# e.g. 5 plus 6:
# 101 and 110 become 011 if the carry is ignored, which is equivalent to 101 XOR 110
# The information of the carry itself is 1000, which is obtained by left shifting (Left Shift) one bit (101 AND 110)

# Loop
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        return (a & mask) if b > 0 else a

# Recurison
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        if b & mask == 0:
            return (a & mask) if b > 0 else a
        return self.getSum(a ^ b, (a & b) << 1)

# Tricky answer
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])