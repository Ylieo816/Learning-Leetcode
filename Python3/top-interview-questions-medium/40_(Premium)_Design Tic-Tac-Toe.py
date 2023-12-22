# Design a Tic-tac-toe game that is played between two players on a n x n grid.

# You may assume the following rules:

# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.


class TicTacToe:
# Optimized DP
# Time Complexity: O(1)
# Space Complexity: O(n)
    def __init__(self, n: int):
        self.n = n
        self.Row = [0] * n
        self.Col = [0] * n
        self.Dia, self.antiDia = 0, 0

    def move(self, row: int, col: int, player: int) -> int:
        add = 1 if player == 1 else -1
        self.Row[row] += add
        self.Col[col] += add
        if row == col:  self.Dia += add
        if row+col+1 == self.n: self.antiDia += add
        if (abs(self.Row[row]) == self.n or abs(self.Col[col]) == self.n or
            abs(self.Dia) == self.n or abs(self.antiDia) == self.n):
            return player
       
        return 0
        


# Optimized Brute Force
# Time Complexity: O(n)
# Space Complexity: (n^2)
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.table = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.table[row][col] = player

        def checkRow(row, player):
            # check row
            for i in range(self.n):
                if self.table[row][i] != player:
                    return False
            return True


        def checkCol(col, player):
            # check col
            for i in range(self.n):
                if self.table[i][col] != player:
                    return False
            return True

        def checkDiagonal(player):
            # check diagonal row (Top-left to Bottom-right)
            for i in range(self.n):
                if self.table[i][i] != player:
                    return False
            return True


        def checkAntiDiagonal(player):
            # check diagonal row (Bottom-left to Top-right)
            for i in range(self.n):
                if self.table[i][self.n - i - 1] != player:
                    return False
            return True
        
        if (checkRow(row, player) or checkCol(col, player) or 
            (row == col and checkDiagonal(player)) or (row+col+1 == self.n and checkAntiDiagonal(player))):
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)