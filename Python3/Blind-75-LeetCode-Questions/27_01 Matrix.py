# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

# Complexity:
# Time Complexity:
# O(m×n) - Since each cell in the matrix is processed once.

# Space Complexity:
# O(m×n) - In the worst case, all cells might be added to the queue.

#### Enhanced Breakdown:
# 1. Initialization:
# - Create a queue and initialize it with all cells containing 0s. These will be our BFS starting points.
# - Set all cells containing 1s to a large value which acts as a placeholder indicating that the cell hasn't been visited yet.

# 2. BFS Traversal:
# - Dequeue a cell and explore its neighboring cells (top, down, left, right).
# - If the distance to the current cell plus one is less than the value in the neighboring cell, update the neighboring cell's distance and enqueue it for further processing.

# 3. Wrap-up:
# - Once all cells have been visited and updated, return the transformed matrix.

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS
        if not mat or not mat[0]:   return mat

        m, n = len(mat), len(mat[0])
        MAX_VALUE = m * n
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = MAX_VALUE
        
        direction = [(0,1), (1,0), (-1,0), (0,-1)]

        while queue:
            col, row = queue.popleft()
            for i, j in direction:
                col_nei, row_nei = col + i, row + j
                if 0 <= col_nei < m and 0 <= row_nei < n and (mat[col_nei][row_nei] > mat[col][row] + 1):
                    queue.append((col_nei, row_nei))
                    mat[col_nei][row_nei] = mat[col][row] + 1
        return mat

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # DP
        n, m=len(mat), len(mat[0])
        row = [-1]*m
        dp = [row[:] for _ in range(n)]

        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    queue.append((i, j))
                    dp[i][j]=0

        while queue:
            col, row = queue.popleft()
            d = dp[col][row]
            direction = [(col, row+1), (col+1, row), (col, row-1), (col-1, row)]
            for (a, b) in direction:
                if a<0 or a>=n or b<0 or b>=m or dp[a][b]!=-1: continue 
                queue.append((a, b))
                dp[a][b] = d+1
        
        return dp