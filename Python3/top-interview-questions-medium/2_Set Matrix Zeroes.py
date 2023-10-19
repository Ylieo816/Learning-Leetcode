# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Fix the question resquest (in place)
# Time Complexity: O(N^2)
# Space Complexity: 1
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h, w = len(matrix), len(matrix[0])
        
        first_row_has_zero = False
        first_col_has_zero = False

        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_has_zero = True
                    if j == 0:
                        first_col_has_zero = True
                    matrix[0][j] = matrix[i][0] = 0

        # update the cell to be zero if it's in a zero row or col
        for row in range(1, h):
            for col in range(1, w):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        # update the first row and col if they're zero
        if first_row_has_zero:
            for y in range(w):
                matrix[0][y] = 0

        # update the first col and col if they're zero
        if first_col_has_zero:
            for x in range(h):
                matrix[x][0] = 0

# best Time Complex
# Time Complexity: O(N^2)
# Space Complexity:O(2*k)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h, w = len(matrix), len(matrix[0])
        points = []
        uni_x, uni_y = set(), set()
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    points.append((i, j))
                    uni_x.add(i)
                    uni_y.add(j)

        for x, y in points:
            if y in uni_y:
                for i in range(h):
                    matrix[i][y] = 0
                uni_y.remove(y)
            if x in uni_x:
                for j in range(w):
                    matrix[x][j] = 0
                uni_x.remove(x)

        return matrix

# best Space Complex: 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h, w = len(matrix), len(matrix[0])
        uni_h, uni_w = set(), set()
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    uni_h.add(i)
                    uni_w.add(j)

        for x in uni_h:
            for i in range(w):
                matrix[x][i] = 0
        for y in uni_w:
            for j in range(h):
                matrix[j][y] = 0

        return matrix