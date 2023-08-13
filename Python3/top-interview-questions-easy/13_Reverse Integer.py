# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# class Solution:
#     def reverse(self, x: int) -> int:
#         flag = True if x > 0 else False
#         x = int(str(x)[::-1]) if x > 0 else int(str(x)[1::-1]) * -1

#         if (-(2**31)<=s<= (2**31-1)):
#             return x
#         else:
#             return 0
x = 1534236469
if (-(2**31) <= x <= (2**31-1)) and x != 0:
    y = (str(x)[1:])[::-1]
    print(y)
    print(int(str(x)[::-1]) if x > 0 else int(y) * -1)
else:
    print(0)

# class Solution:
#     def reverse(self, x: int) -> int:
#         if x == 0:
#             return 0
#         elif x > 0:
#             flag = 1
#         else:
#             flag = -1
        
#         x = list(str(abs(x)))
#         s = ""
#         for i in range(len(x)):
#             s += x[len(x) - i - 1]
#         s = flag * int(s)
        
#         if (-(2**31)<=s<= (2**31-1)):
#             return s
#         else:
#             return 0
            
        
        
        
        
        # first answer: slice objects 
#         s = str(x)
#         s = int(s[::-1]) if x > 0 else int(s[:0:-1]) * -1
        
#         if 2147483647 > s > -2147483648:
#             return s

            
        
        