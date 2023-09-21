# Given an m x n matrix, return all elements of the matrix in spiral order.

# Complexity
# - Time complexity:O(M*N)
# - Space complexity:O(m*n)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:  return []
        x_len, y_len = len(matrix), len(matrix[0])


        answer = []
        top, bottom, left, right = 0, x_len - 1, 0, y_len - 1

        while len(answer) < x_len * y_len:
            for i in range(left, right + 1):
                answer.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                answer.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    answer.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    answer.append(matrix[i][left])
                left += 1
        return answer