# Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

# Implement the Solution class:

#     - Solution(int[] nums) Initializes the object with the integer array nums.
#     - int[] reset() Resets the array to its original configuration and returns it.
#     - int[] shuffle() Returns a random shuffling of the array.

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums_new = self.nums[:]
        random.shuffle(nums_new)
        return nums_new


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()