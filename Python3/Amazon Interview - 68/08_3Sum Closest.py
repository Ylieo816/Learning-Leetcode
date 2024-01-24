# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Two ptr
# Time Complexity: O(n^2).
# Space Complexity: from O(log⁡n) to O(n)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            low, height = i + 1, len(nums) - 1
            while low < height:
                summ = nums[i] + nums[low] + nums[height]
                if abs(target - summ) < abs(diff):
                    diff = target - summ
                if summ < target:
                    low += 1
                else:
                    height -= 1
            if diff == 0:
                break
        return target - diff

# Bruce Solution
# Time Limit Exceeded
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = float('inf')
        length = len(nums)
        for i1 in range(length):
            for i2 in range(i1+1, length):
                for i3 in range(i2+1, length):
                    summ = nums[i1] + nums[i2] + nums[i3]
                    if abs(summ - target) < abs(answer - target):
                        answer = summ
        return answer