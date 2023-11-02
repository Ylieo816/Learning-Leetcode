# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        distance = len(nums) - 1
        for i in range(distance, -1, -1):
            # comfirm that current step + idx can reach destination
            # if so, update destination to now idx
            if i + nums[i] >= distance:
                distance = i
        return distance == 0

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # keey jump max steps
        max_step = nums[0]
        for i in range(1, len(nums)):
            if max_step == 0:
                return False
            # max previous step and now step, so that we can keep max steps
            max_step = max(max_step - 1, nums[i])
        return True