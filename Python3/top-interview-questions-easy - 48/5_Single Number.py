# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in (nums):
            if str(num) not in dic:
                dic[str(num)] = 1
            else:
                del dic[str(num)]
        return int(list(dic.keys())[0])

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)
