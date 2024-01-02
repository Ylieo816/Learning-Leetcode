# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

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