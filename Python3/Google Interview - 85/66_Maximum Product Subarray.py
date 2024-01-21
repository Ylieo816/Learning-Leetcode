# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# time complex: O(n)
# space complex: O(1) 

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num, min_num = nums[0], nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_num, min_num = min_num, max_num
            
            max_num = max(nums[i], nums[i] * max_num)
            min_num = min(nums[i], nums[i] * min_num)
            answer = max(answer, max_num)

        return answer