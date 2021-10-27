import numpy as np
class Board:
    def __init__(self,row = 3,col = 3,winNum = 3):
        self.board = np.zeros((row,col),dtype=int)
        self.col = col
        self.row = row
        self.winNum = winNum
        self.boardHash = None
        self.isEnd = False
        self.solutionArray = np.array([448,273,292,146,84,73,56,7])
        

    def getBoard(self):
        return self.board

    """
    Creates a hash of the current board returns board hash
    """
    def getHash(self):
        self.boardHash = str(self.board.ravel())
        return self.boardHash
    
    def getShrinkHash(self):
        boardCopy = self.board.copy()
        while(np.all(boardCopy[0] == 0)):
            boardCopy = np.delete(boardCopy,(0), axis = 0)
        while(np.all(boardCopy[-1] == 0)):
            boardCopy = np.delete(boardCopy,(-1), axis = 0)
        while(np.all(boardCopy[:, 0] == 0)):
            boardCopy = np.delete(boardCopy,(0), axis = 1)
        while(np.all(boardCopy[: ,-1] == 0)):
            boardCopy = np.delete(boardCopy,(-1), axis = 1)
        
        return str(boardCopy.ravel())
    
    """
    resets all dates for training
    """
    def reset(self):
        self.board = np.zeros((self.row,self.col),dtype=int)
        self.boardHash = None
        self.isEnd = False
    """
    input of the board 3 by 3 numpy array, player int, row number int, column number int
    checks if move is legal and sets the new board as its output
    returns 0 if check fails
    """
    def move(self,player,rowNum,colNum):
        if(self.checkMove(rowNum,colNum)):
            self.board[rowNum][colNum] = player
            return True
        else:
            return False

    """
     row number int, row column int
    checks if placing a move in the given coordinates are legal
    returns true if legal, false if not
    """
    def checkMove(self,rowNum,colNum):
        if(self.getBoard()[rowNum][colNum] == 0):
            return True
        else:
            return False
    
    def printBoard(self):
        print(self.board)
        
    """
    Input of any length row and player counter
    Creates a copy of the row to allow editing
    for each element the element is set to 0 if it isnt the players move, this is to ignore empty coords and the other players moves
    checks if the list contains the amount required to win of the players move
    returns true if check passes, else false
    """
    def checkRow(self,row, player):
        for index in range(0,len(row)):
            if (row[index] != player):
                row[index] = 0
        for x in range((len(row)-self.winNum+1)):
            if (all(row[x:self.winNum+x])):
                return True
        else:
            return False
    
    """
    player character
    creates a copy of the board
    loops over each row to check if win condition has been met 
    rotates the board by 90 degrees and repeates check
    Creates a list of all diagonal combinations
    does a row check on all diagonal combinations
    returns true if win condition has been met
    """
    def checkBoard(self,player):
        boardCopy = np.copy(self.board)
        for x in range(0,2):
            for row in boardCopy:
                if (self.checkRow(row,player)):
                    self.isEnd = True
                    return True
            boardCopy = np.rot90(boardCopy)
        diags = [boardCopy[::-1,:].diagonal(i).copy() for i in range(-boardCopy.shape[0]+1,boardCopy.shape[1])]
        diags.extend(boardCopy.diagonal(i).copy() for i in range(boardCopy.shape[1]-1,-boardCopy.shape[0],-1))
        
        for row in diags:
            if(len(row)>=self.winNum):
                if (self.checkRow(row,player)):
                    self.isEnd = True
                    return True
        
    """
    Checks and returns remaining possible moves
    """
    def getRemainingMoves(self,board):
        remainingMoves = []
        for row in range(0,len(board)):
            for col in range(0,len(board[0])):
                if(board[row][col] == 0):
                    remainingMoves.append([row,col])
        return remainingMoves
    
    """
    Check and returns how many spaces are remaining
    """
    def openSpaces(self):
        return np.count_nonzero(self.board == 0)
    
    def binarySolver(self,board,player):
        tempBoard = board.copy()
        for row in tempBoard:
            for index in range(0,len(row)):

                if (row[index] != player):
                    row[index] = 0
                if (row[index] == 2):
                    row[index] = 1
        singleArrayBoard = tempBoard.ravel()
        boardInt = int("0b"+''.join(map(str, singleArrayBoard)),2)
        for ans in self.solutionArray:
            if(boardInt&ans == ans):
                return True
        return False

