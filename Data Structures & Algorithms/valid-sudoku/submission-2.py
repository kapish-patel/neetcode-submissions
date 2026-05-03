class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCol = self.checkRowAndCol(board) 
        mat = self.check3x3Grid(board)
        print(rowCol, mat)
        return rowCol and mat
    
    def checkRowAndCol(self, board):
        # row
        for i in range(0,9):
            row = set()
            col = set()
            for j in range(0,9):
                
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
                
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])

        return True
    
    def check3x3Grid(self, board):
        # now we can get the center of each 3x3 by just adding +3 to i or j
        for i in range(1, 9, 3):
            for j in range(1, 9, 3):
                lst = self.getallElements(board,i,j)
                print(lst)
                if len(lst) != len(set(lst)):
                    print(lst)
                    return False
        return True
    
    def getallElements(self, board,i,j):
        result = []
        if board[i-1][j-1].isdigit():
            result.append(board[i-1][j-1])
        if board[i-1][j].isdigit():
            result.append(board[i-1][j])
        if board[i-1][j+1].isdigit():
            result.append(board[i-1][j+1])

        if board[i][j-1].isdigit():
            result.append(board[i][j-1])
        if board[i][j].isdigit():
            result.append(board[i][j])
        if board[i][j+1].isdigit():
            result.append(board[i][j+1])

        if board[i+1][j-1].isdigit():
            result.append(board[i+1][j-1])
        if board[i+1][j].isdigit():
            result.append(board[i+1][j])
        if board[i+1][j+1].isdigit():
            result.append(board[i+1][j+1])

        return result
            







            
                

         

        