# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Best answer and faster (do left and then do right)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        answer = [1] * l
        pre, post = 1, 1
        for i in range(l):
            answer[i] *= pre
            pre *= nums[i]
            answer[l-i-1] *= post
            post *= nums[l-i-1]
        return answer

# original think, slower
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left_start, right_start, answer = [0] * l, [0] * l, [0] * l
        left_start[0], right_start[-1] = nums[0], nums[-1]
        for i in range(l - 1):
            left_start[i+1] = nums[i+1] * left_start[i]
            right_start[l-i-2] = nums[l-i-2] * right_start[l-i-1]

        for i in range(l):
            if i == 0:
                answer[i] = right_start[i+1]
            elif i == (l-1):
                answer[i] = left_start[l-2]
            else:
                answer[i] = left_start[i-1] * right_start[i+1]
        return answer