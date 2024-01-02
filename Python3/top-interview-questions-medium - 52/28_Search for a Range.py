# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# Binary Search (Optimized):
# Time Complexity: O(n) -  One pass through the array using two pointers
# Space Complexity: O(1) - Constant extra space is used
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        first, last = -1, -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first, last = mid, mid
                while first > 0 and nums[first - 1] == target:
                    first -= 1
                while last < len(nums) - 1 and nums[last + 1] == target:
                    last += 1
                return [first, last]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [first, last]

# Binary Search:
# Time Complexity: O(n) - Two binary searches are performed.
# Space Complexity: O(1) - Constant extra space is used.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    # leftBias=[True/False], if false, res is rightBiased
    def binSearch(self, nums, target, leftBias):
        left, right = 0, len(nums) - 1
        i = -1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                i = mid
                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1
        return i