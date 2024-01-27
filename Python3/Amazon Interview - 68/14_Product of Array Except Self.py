# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# One Pass
# Time complexity : O(N)
# Space complexity : O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # cur pos = except self, so pre will skip self but post will run others
        l = len(nums)
        answer = [1] * l
        pre, post = 1, 1
        for i in range(l):
            answer[i] *= pre
            pre *= nums[i]
            answer[l-i-1] *= post
            post *= nums[l-i-1]
        return answer

# # Left and Right product lists
# # Time complexity : O(N)
# # Space complexity : O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        L, R, answer = [1] * l, [1] * l, [1] * l

        for i in range(1, l):
            L[i] = nums[i-1] * L[i-1]
            R[l-i-1] = nums[l-i] * R[l-i]
        for i in range(l):
            answer[i] = L[i] * R[i]
        return answer