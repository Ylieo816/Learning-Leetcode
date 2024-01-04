# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Complexity
# Time complexity: O(mn), m: rows and n : columns of matirx
# Space complexity: O(mn), m: rows and n: columns of matrix. The space is used by the visited matrix.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0])

        def DFS(x, y):
            grid[x][y] = '0'

            if (x + 1 < h) and (grid[x+1][y] == '1'):
                DFS(x+1, y)
            if (x - 1 >= 0) and (grid[x-1][y] == '1'):
                DFS(x-1, y)
            if (y + 1 < w) and (grid[x][y+1] == '1'):
                DFS(x, y+1)
            if (y - 1 >= 0) and (grid[x][y-1] == '1'):
                DFS(x, y-1)
        
        answer = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    answer += 1
                    DFS(i, j)
        return answer