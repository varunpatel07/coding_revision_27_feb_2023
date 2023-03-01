class Solution:
    def isValidSudoku(self, board):
        sub_set=set()
        for i in range(9):
            row_set=set()
            col_set=set()
            for j in range(9):
                if(board[i][j] in row_set or board[j][i] in col_set) :
                    print('1')
                    return False
                if(board[i][j]!='.'):
                    row_set.add(board[i][j])
                if(board[j][i]!='.'):
                    col_set.add(board[j][i])

        for i in range(9):
            for j in range(9):
                if(board[i][j]!='.'):
                    if((i//3,j//3,board[i][j]) in sub_set):
                        return False
                    sub_set.add((i//3,j//3,board[i][j]))
        return True  

        pass

obj = Solution()
board = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]]
print(obj.isValidSudoku(board))
