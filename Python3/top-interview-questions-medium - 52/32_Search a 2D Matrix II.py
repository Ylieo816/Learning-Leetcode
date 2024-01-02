# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Binary Search for row
# Time complexity: O(mlogn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            if matrix[i][0] <= target <= matrix[i][-1]:
                left, right = 0, col
                while left <= right:
                    mid = left + (right - left) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False

# Time complexity: O (M + N)
# matrix[i][j] < matrix[i][j+1]
# matrix[i][j] > matrix[i-1][j]
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Logic: set a cornor to origin point
        # e.g. set Bottom Left to origin point
        # if matrix[i][j] > target: move up
        # if matrix[i][j] < target: move right
        
        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return False

        col, row = 0, len(matrix) - 1
        col_max = len(matrix[0])
        while col < col_max and row >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        return False