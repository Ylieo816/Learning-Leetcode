# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # first answer
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:        
        # second answer
        nums1.sort()
        nums2.sort()
        pointer1 = pointer2 = 0
        incommon = []
        while((pointer1 < len(nums1)) and (pointer2 < len(nums2))):
            if nums1[pointer1] == nums2[pointer2]:
                incommon.append(nums1[pointer1])
                pointer1 += 1
                pointer2 += 1
            elif nums1[pointer1] < nums2[pointer2]:
                pointer1 += 1
            else:
                pointer2 += 1
        return incommon

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:        
        # best answer
        c1, c2 = Counter(nums1), Counter(nums2)
        incommonnum = c1 & c2
        incommon = []
        for i in incommonnum:
            incommon = incommon + [i] * incommonnum[i]
        return incommon
