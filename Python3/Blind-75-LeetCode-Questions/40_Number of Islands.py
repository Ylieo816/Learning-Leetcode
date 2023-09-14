# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def DFS(x, y):
            grid[x][y] = '0'

            if (x-1 >= 0) and (grid[x-1][y] == '1'):
                DFS(x-1, y)
            if (x+1 < len(grid)) and (grid[x+1][y] == '1'):
                DFS(x+1, y)
            if (y-1 >= 0) and (grid[x][y-1] == '1'):
                DFS(x, y-1)
            if (y+1 < len(grid[0])) and (grid[x][y+1] == '1'):
                DFS(x, y+1)
        

        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    answer += 1
                    DFS(i, j)
        return answer