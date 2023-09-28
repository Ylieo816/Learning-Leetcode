# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        col, row = len(board), len(board[0])
        w_l = len(word)

        # # # # # #  Optimization for flitering wrong status
        if w_l > (col * row):
            return False

        count = Counter(sum(board, []))
        
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
        
        # # # # # #  

        visited = [[False] * row for _ in range(col)]
        def DFS(x, y, level):
            # if level == len(word), then word has been found
            if level == w_l:
                return True
            
            # out of bounds
            # OR current letter does not match letter on board
            # OR letter already visited
            if not (0 <= x < row) or not (0 <= y < col) or (word[level] != board[y][x]) or visited[y][x]:
                return False

            # to keep track of the letter already visited, add it's position to the set
            # after DFS we can remove it from the set.
            visited[y][x] = True

            tmp = (
                DFS(x + 1, y, level + 1) or 
                DFS(x - 1, y, level + 1) or 
                DFS(x, y + 1, level + 1) or 
                DFS(x, y - 1, level + 1))

            visited[y][x] = False
            # bracktracking
            return tmp

        for i in range(row):
            for j in range(col):
                    if DFS(i, j, 0):
                        return True
        return False