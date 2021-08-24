import numpy as np
class Board:
    def createBoard():
        board = np.array([[0, 0, 0],[0, 0, 0],[0, 0, 0]])
        return board
    
    """
    input of the board 3 by 3 numpy array, player int, row number int, column number int
    checks if move is legal and sets the new board as its output
    returns 0 if check fails
    """
    def move(board,player,rowNum,colNum):
        if(Board.checkMove(board,rowNum,colNum)):
            board[rowNum][colNum] = player
            return board
        else:
            return 0

    """
    input of the board 3 by 3 numpy array, row number int, row column int
    checks if placing a move in the given coordinates are legal
    returns true if legal, false if not
    """
    def checkMove(board,rowNum,colNum):
        if(board[rowNum][colNum] == 0):
            return True
        else:
            return False
    
    def printBoard(board):
        print(board)
        
    """
    input of the row 3 element array, player int
    for each element the element is set to 0 if it isnt the players move, this is to ignore empty coords and the other players moves
    checks if the list contains 3 of the players move
    returns true if check passes, else false
    """
    def checkRow(row, player):
        for index in range(0,2):
            if (row[index] != player):#potentially add a check to see if row[index] isnt 0, may be faster than assignment
                row[index] = 0
        if(all(row)):
            return True
        else:
            return False
    
    """
    input of board 3 by 3 numpy array, player int
    creates a copy of the board
    loops over each row to check if win condition has been met
    checks if diagonal win condition has been met
    rotates the board by 90 degrees
    repeats the loop
    returns true if win condition has been met
    """
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
                    