# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# DFS - recursion
# Time complexity: O(N^(M/min_cand + 1)), N = len(candidates), M = target, min_cand = min(candidates)
# Space complexity: O(M/min_cand)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        self.DFS(candidates, target, [], answer)
        return answer
        
    def DFS(self, candidates, target, path, answer):
        if target < 0:  return

        if target == 0:
            answer.append(path)

        for i in range(len(candidates)):
            self.DFS(candidates[i:], target - candidates[i], path + [candidates[i]], answer)

# DP
# Time Complexity: O(M*M*N), N = len(candidates), M = target
# Space Complexity: O(M*M)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]

        for c in candidates:                    # O(N): for each candidate
            for i in range(c, target + 1):      # O(M): for each possible value <= target
                if i == c:
                    dp[i].append([c])
                for combinaion in dp[i-c]:      # O(M) worst: for each combination
                    dp[i].append(combinaion + [c])
        return dp[-1]