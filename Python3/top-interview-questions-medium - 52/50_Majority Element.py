# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for key in count:
            if count[key] > (len(nums) // 2):
                return key

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore Voting Algorithm
        count, char =0, 0
        for num in nums:
            if count == 0:
                char = num
            
            if char == num:
                count += 1
            else:
                count -= 1

        return char