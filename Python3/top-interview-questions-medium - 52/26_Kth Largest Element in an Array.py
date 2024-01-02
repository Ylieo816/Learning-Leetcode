# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Complexity:
# Time Complexity: O(Nlog⁡N)
# Space Complexity: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

# Complexity:
# Time Complexity: O(nlog⁡k), n elements is processed once, heap operations take O(log⁡k) time
# Space Complexity: O(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:   
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heappushpop(heap, num)
        return heap[0]

# Quick Select:
# Complexity:
# Time Complexity: Best and Average Case: O(N), Worst Case: O(N^2)
# Space Complexity: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # 1. Set the left, right boundary
        # 2. Randomly select a pivot index between the left and right
        # 3.
        #     - Move smaller than the pivot to left and  larger elements to right
        #     - Return the final position of the pivot after the partitioning
        # 4.
        #     - If position of pivot is the desired k-th largest index, return pivot.
        #     - If pivot's position greater than the desired index, adjust the right boundary and repeat.
        #     - If pivot's position lesser than the desired index, adjust the left boundary and repeat.
        left, right = 0, len(nums) - 1
        while True:
            pivot= random.randint(left, right)
            new_pivot = self.partition(nums, left, right, pivot)
            if new_pivot == len(nums) - k:
                return nums[new_pivot]
            elif new_pivot > len(nums) - k:
                right = new_pivot - 1
            else:
                left = new_pivot + 1
    
    def partition(self, nums, left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        stored_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[stored_index] = nums[stored_index], nums[i]
                stored_index += 1
        nums[right], nums[stored_index] = nums[stored_index], nums[right]
        return stored_index