# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        word_len = len(word)

        # # # # # #  Optimization for flitering wrong status
        if word_len > row * col:
            return False
        
        count = Counter(sum(board, []))
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False

        # # # # # #  

        visited = [[False] * col for _ in range(row)] 
        def backtrack(x, y, level):
            # if level == len(word), then word has been found
            if level == word_len:
                return True

            # out of bounds
            # OR current letter does not match letter on board
            # OR letter already visited
            if not (0 <= x < row) or not (0 <= y < col) or (word[level] != board[x][y]) or visited[x][y]:
                return False

            # to keep track of the letter already visited, add it's position to the set
            # after DFS we can remove it from the set.          
            visited[x][y] = True

            tmp = (
                backtrack(x + 1, y, level + 1) or
                backtrack(x - 1, y, level + 1) or
                backtrack(x, y + 1, level + 1) or
                backtrack(x, y - 1, level + 1)
            )

            visited[x][y] = False
            # bracktracking
            return tmp
        
        for i in range(row):
            for j in range(col):
                if backtrack(i, j, 0):
                    return True
        return False