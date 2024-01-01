# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Complexity:
# Time Complexity: O(Nlog⁡N)
# Space Complexity: O(1)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return sorted(nums, reverse=True)[k-1]

# Complexity:
# Time Complexity: O(nlog⁡k), n elements is processed once, heap operations take O(log⁡k) time
# Space Complexity: O(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:   
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]

# Quick Select:
# Complexity:
# Time Complexity: Best and Average Case: O(N), Worst Case: O(N^2)
# Space Complexity: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

#         # 1. Set the left, right boundary
#         # 2. Randomly select a pivot index between the left and right
#         # 3.
#         #     - Move smaller than the pivot to left and  larger elements to right
#         #     - Return the final position of the pivot after the partitioning
#         # 4.
#         #     - If position of pivot is the desired k-th largest index, return pivot.
#         #     - If pivot's position greater than the desired index, adjust the right boundary and repeat.
#         #     - If pivot's position lesser than the desired index, adjust the left boundary and repeat.
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, right, mid = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quick_select(left, k)
            
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))

            return pivot

        return quick_select(nums, k)