# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def DFS(path, visited):
            if len(path) == len(nums):  # ran already all char
                answer.append(path[:])  # need shallow copy or deep copy
                return
            
            for idx, value in enumerate(nums):
                if visited[idx]:    # jump next char when visited this char
                    continue
                path.append(value)
                visited[idx] = True
                DFS(path, visited)  # run next char
                #  next round
                path.pop()
                visited[idx] = False

        DFS([], [False] * len(nums))
        return answer