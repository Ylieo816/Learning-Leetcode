# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# # Two ptr
# # Time Complexity: O(n^2). twoSumII is O(n), and we call it n times
# # Space Complexity: from O(log⁡n) to O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        # check the mid num only <= 0
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            # if first or no equal to neighbor
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, answer)
        return answer

    def twoSum(self, nums, i, answer):
        low, height = i + 1, len(nums) - 1
        while low < height:
            # keep track find all rest pair
            summ = nums[i] + nums[low] + nums[height]
            if summ < 0:
                low += 1
            elif summ > 0:
                height -= 1
            else:
                answer.append([nums[i], nums[low], nums[height]])
                low += 1
                height -= 1
                # avoid low same as next one
                while low < height and nums[low] == nums[low - 1]:
                    low += 1

# Check with No sort
# # Time Complexity: O(n^2). twoSumII is O(n), and we call it n times
# # Space Complexity: from O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer, dup = set(), set()
        seen = {}
        for i, val_1 in enumerate(nums):
            if val_1 not in dup:
                dup.add(val_1)
                for j, val_2 in enumerate(nums[i+1:]):
                    target = - val_1 - val_2
                    if target in seen and seen[target] == i:
                        answer.add(tuple(sorted((val_1, val_2, target))))
                    seen[val_2] = i
        return answer


# Divide into each part to check
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        positive, negative, zero = [], [], []
        for num in nums:
            if num > 0:
                positive.append(num)
            elif num < 0:
                negative.append(num)
            else:
                zero.append(num)
                
        POSITIVE, NEGATIVE = set(positive), set(negative)
        
        # check all 0
        if len(zero) > 2:
            answer.add((0, 0, 0))
            
        # check one zero, one positive, one negative
        if zero:
            for num in POSITIVE:
                if -num in NEGATIVE:
                    answer.add((-num, 0, num))
            
            
        # check two positive with one negative
        for i in range(len(positive)):
            for j in range(i+1, len(positive)):
                target = - (positive[i] + positive[j])
                if target in NEGATIVE:
                    answer.add(tuple(sorted([positive[i], positive[j], target])))
                    
            
        # check two negative with one positive
        for i in range(len(negative)):
            for j in range(i+1, len(negative)):
                target = - (negative[i] + negative[j])
                if target in POSITIVE:
                    answer.add(tuple(sorted([negative[i], negative[j], target])))
                    
        return answer