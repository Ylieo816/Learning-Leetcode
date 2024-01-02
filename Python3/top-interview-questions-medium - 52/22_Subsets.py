# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Complexity
# Time complexity: O(2^n) - There are 2^n possible subsets for n elements.
# Space complexity: O(n) - At most, the depth of the recursion is n, and 'twos' holds a maximum of n elements at any given time.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        l = len(nums)

        def backtrack(idx, combination):
            answer.append(combination)
            for i in range(idx, l):
                backtrack(i + 1, combination + [nums[i]])
        
        backtrack(0, [])
        return answer