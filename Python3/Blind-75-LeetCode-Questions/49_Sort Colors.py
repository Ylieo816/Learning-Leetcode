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
        left, idx, right = 0, 0, len(nums) - 1
        while idx <= right:
            if nums[idx] == 0:
                nums[idx], nums[left] = nums[left], nums[idx]
                idx += 1
                left += 1
            elif nums[idx] == 2:
                nums[idx], nums[right] = nums[right], nums[idx]
                right -= 1
            else:
                idx += 1