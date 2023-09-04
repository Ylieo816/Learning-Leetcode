# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = Counter(nums)
        for c in table:
            if table[c] > (len(nums) // 2):
                return c

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore Voting Algorithm: since majority num is more than half, so no matter how many count, the majority num will be keeped until final
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate