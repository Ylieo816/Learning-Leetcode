# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Two ptr to compare
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        water, left_max, right_max = 0, 0, 0

        while left < right:
            left_max  = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1

        return water

# find min(max left and max right), but too slow
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i in range(1, len(height)):
            min_height = min(max(height[0:i]), max(height[i:len(height)]))
            if min_height > height[i]:
                water += min_height - height[i]
        return water