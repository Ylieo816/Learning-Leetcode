# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.

# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

# Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        answer = []
        if len(nums) == 0:
            answer.append([lower, upper])
            return answer
        
        # Check for missing numbers between the lower bound and nums[0]
        if lower < nums[0]:
            answer.append([lower, nums[0] - 1])

        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] <= 1:
                continue
            answer.append([nums[i] + 1, nums[i+1] - 1])

        # Check for missing numbers between the nums[-1] + 1 and upper bound
        if nums[-1] < upper:
            answer.append([nums[-1] + 1, upper])

        return answer