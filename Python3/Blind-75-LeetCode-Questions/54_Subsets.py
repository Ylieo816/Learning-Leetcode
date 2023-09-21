# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        l = len(nums)

        def DFS(idx, path):
            answer.append(path)
            for i in range(idx, l):
                DFS(i + 1, path + [nums[i]])

        DFS(0, [])
        return answer