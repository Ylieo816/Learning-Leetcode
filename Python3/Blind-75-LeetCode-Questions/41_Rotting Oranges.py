# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        row, col = len(grid), len(grid[0])
        fresh_count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0
        if not q:
            return -1

        count = -1
        while q:
            count += 1
            for _ in range(len(q)):
                (x, y) = q.popleft()
                if (x-1 >= 0) and (grid[x-1][y] == 1):
                    grid[x-1][y] = 2
                    q.append((x-1, y))
                    fresh_count -= 1
                if (x+1 < row) and (grid[x+1][y] == 1):
                    grid[x+1][y] = 2
                    q.append((x+1, y))
                    fresh_count -= 1
                if (y-1 >= 0) and (grid[x][y-1] == 1):
                    grid[x][y-1] = 2
                    q.append((x, y-1))
                    fresh_count -= 1
                if (y+1 < col) and (grid[x][y+1] == 1):
                    grid[x][y+1] = 2
                    q.append((x, y+1))
                    fresh_count -= 1

        return count if fresh_count == 0 else -1