# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Concept of Method
#       nums = [ _1_, 8,4,5,3,7]     arr = [1]              (initial step)
#       nums = [1, _8_, 4,5,3,7]     arr = [1, 8]           (8 > 1, so    append 8)
#       nums = [1,8, _4_, 5,3,7]     arr = [1, 4]           (4 < 8, so overwrite 8)
#       nums = [1_8,4, _5_, 3,7]     arr = [1, 4, 5]        (5 > 4, so    append 5)
#       nums = [1_8,4,5, _3_, 7]     arr = [1, 3, 5]        (3 < 5, so overwrite 4)
#       nums = [1_8,4,5,3, _7_ ]     arr = [1, 3, 5, 7]     (7 > 5, so    append 7)    

# bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        answer = []
        answer.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > answer[-1]:
                answer.append(nums[i])
            else:
                # bisect_left: find the index for insert nums[i] in order
                answer[bisect_left(answer, nums[i])] = nums[i]
        return len(answer)

# DP
# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                # find how many numbers can in front of dp[i], if so, dp[i] ++
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # return the max sub num
        return max(dp)