# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Time: O(n) - In the worst case 2 scans: one for the heights and one for the stack
# Space: O(n) - in the worst case push to the stack the whole input array

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        max_rect = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                h = heights[stack[-1]]
                stack.pop()
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] -1
                max_rect = max(max_rect, h * w)
            stack.append(i)
        return max_rect