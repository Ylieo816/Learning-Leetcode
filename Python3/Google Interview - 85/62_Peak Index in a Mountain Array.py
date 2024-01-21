# An array arr is a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.

# Binary Search
# Time complexity: O(log⁡n)
# Space complexity: O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

# # Easy and quick solution
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))

# # Time complexity: O(n)
# # Space complexity: O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 0
        while arr[i] < arr[i + 1]:
            i += 1
        return i