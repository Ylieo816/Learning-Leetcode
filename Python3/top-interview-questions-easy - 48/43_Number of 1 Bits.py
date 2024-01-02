# Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Note:

# Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

# Shortest Answer but too late
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# Faster but still late
class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        while(n != 0):
            n = n & (n-1)
            num += 1
        return num

# Check last bit and add it
class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        while n > 0:
            num += n & 1
            n >>= 1
        return num
        