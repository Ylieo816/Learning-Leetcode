# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

# # Optimized Stack
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_s, cur_num = '', 0
        for char in s:
            if '0' <= char <= '9':
                cur_num = cur_num * 10 + int(char)
            elif char == '[':
                stack.append(cur_num)
                stack.append(cur_s)
                cur_num, cur_s = 0, ''
            elif char == ']':
                pre_s = stack.pop()
                pre_num = stack.pop()
                cur_s = pre_s + cur_s * pre_num
            else:
                cur_s += char

        return cur_s

# Stack, faster
# Complexity Analysis:
# Time Complexity: O(maxKcountK⋅n)
# Space Complexity: O(sum(maxKcountK⋅n))
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                answer = ''
                while stack[-1] != '[':
                    answer += stack.pop()
                stack.pop()
                
                multi, num = 1, 0
                while stack and ('0' <= stack[-1] <= '9'):
                    num += int(stack.pop()) * multi
                    multi *= 10
                
                answer *= num
                stack.append(answer)

        return (''.join(stack[::-1])[::-1])