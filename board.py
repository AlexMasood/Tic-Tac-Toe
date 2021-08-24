import numpy as np
class Board:
    def createBoard():
        board = np.array([[0, 0, 0],[0, 0, 0],[0, 0, 0]])
        return board
    
    def move(board,player,rowNum,colNum):
        if(Board.checkMove(board,rowNum,colNum)):
            board[rowNum][colNum] = player
            return board
        else:
            return 0

    def checkMove(board,rowNum,colNum):
        if(board[rowNum][colNum] == 0):
            return True
        else:
            return False
    
    def printBoard(board):
        print(board)
        
    
    def checkRow(row, player):
        for index in range(0,2):
            if (row[index] != player):#potentially add a check to see if row[index] isnt 0, may be faster than assignment
                row[index] = 0
        if(all(row)):
            return True
        else:
            return False
    
    def checkBoard(board, player):
        boardCopy = np.copy(board)
        for x in range(0,2):
            for row in boardCopy:
                if (Board.checkRow(row,player)):
                    return True
            diag = [boardCopy[0][0],boardCopy[1][1],boardCopy[2][2]]
            if (Board.checkRow(diag,player)):
                return True
            boardCopy = np.rot90(boardCopy)
                    