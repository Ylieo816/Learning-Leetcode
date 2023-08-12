# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for i in range(9):
        #     value_row = []
        #     value_col = []
        #     value_box = []
        #     for j in range(9):
        #         if board[i][j] != ".":
        #             if board[i][j] not in value_row:
        #                 value_row.append(board[i][j])
        #             else:
        #                 return False
        #         if board[j][i] != ".":
        #             if board[j][i] not in value_col:
        #                 value_col.append(board[j][i])
        #             else:
        #                 return False
        #         if board[((i//3)*3)+(j//3)][(j%3)+(3*i)%9] != ".":
        #             if board[((i//3)*3)+(j//3)][(j%3)+(3*i)%9] not in value_box:
        #                 value_box.append(board[((i//3)*3)+(j//3)][(j%3)+(3*i)%9])
        #             else:
        #                 return False
        # return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))

