# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        positive, nagetive, zero = [], [], []

        for num in nums:
            if num > 0:
                positive.append(num)
            elif num < 0:
                nagetive.append(num)
            else:
                zero.append(num)
    
        POSITIVE, NAGETIVE = set(positive), set(nagetive)

        # check if contain [0, 0, 0]
        if len(zero) > 2:
            answer.add((0, 0, 0))

        # check if contain the cases of [-num, 0, num]
        if zero:
            for num in POSITIVE:
                if -num in NAGETIVE:
                    answer.add((-num, 0, num))
        
        #  check if two postive with one nageitve
        for i in range(len(positive)):
            for j in range(i + 1, len(positive)):
                target = -(positive[i] + positive[j])
                if target in NAGETIVE:
                    answer.add(tuple(sorted([positive[i], positive[j], target])))

        
        #  check if two nagetive with one positive
        for i in range(len(nagetive)):
            for j in range(i + 1, len(nagetive)):
                target = -(nagetive[i] + nagetive[j])
                if target in POSITIVE:
                    answer.add(tuple(sorted([nagetive[i], nagetive[j], target])))

        return answer