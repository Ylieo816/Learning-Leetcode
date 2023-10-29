# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Complexity
# - Time complexity: O(n)
# - Space complexity: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        ptr = 0
        while ptr <= right:
            if nums[ptr] == 0:
                nums[ptr], nums[left] = nums[left], nums[ptr]
                ptr += 1
                left += 1
            elif nums[ptr] == 2:
                nums[ptr], nums[right] = nums[right], nums[ptr]
                right -= 1
            else:
                ptr += 1