import numpy as np
import math
import time
class Board:
    def __init__(self,row = 3,col = 3,winNum = 3):
        self.board = np.zeros((row,col),dtype=int)
        self.col = col
        self.row = row
        self.winNum = winNum
        self.boardHash = None
        self.isEnd = False
        self.singleMoveDict = {}
        self.solutionSet = {448,273,292,146,84,73,56,7}
        self.remainingMoves = {(0, 1), (1, 2), (0, 0), (2, 1), (2, 0), (1, 1), (2, 2), (1, 0), (0, 2)}
        self.populateSingleMoveDict()

    def getBoard(self):
        return self.board
    
    def printBoard(self):
        print(self.board)
    
    def populateSingleMoveDict(self):
        for row in range(0,self.row):
            for col in range(0,self.col):
                self.singleMoveDict[(row,col)] = int(math.pow(2,((3*(2-row))+(2 - col)))) 

    """
    Creates a hash of the current board returns board hash
    """
    def getHash(self,boardTuple):
        self.boardHash = tuple(boardTuple)
        return self.boardHash
    
    """
    resets all dates for training
    """
    def reset(self):
        self.board = np.zeros((self.row,self.col),dtype=int)
        self.remainingMoves = {(0, 1), (1, 2), (0, 0), (2, 1), (2, 0), (1, 1), (2, 2), (1, 0), (0, 2)}
        self.boardHash = None
        self.isEnd = False
    """
    input of player int, row number int, column number int, players board represented as a integer
    places move on the board
    removes the move from remaining moves
    no check required as legality is assumed true
    """
    def move(self,player,posTuple,playerBoardNum):
        rowNum = posTuple[0]
        colNum = posTuple[1]
        self.board[rowNum][colNum] = player
        self.getRemainingMoves().remove((rowNum,colNum))
        return (playerBoardNum|self.singleMoveDict.get((rowNum,colNum)))
    """
    input of player int, row number int, column number int, players board represented as a integer
    
    
    """
    def tempMove(self,player,posTuple,playerBoardNum):
        rowNum = posTuple[0]
        colNum = posTuple[1]
        return (playerBoardNum|self.singleMoveDict.get((rowNum,colNum)))

    """
    row number int, row column int
    checks if placing a move in the given coordinates are legal
    returns true if legal, false if not
    """
    def checkMove(self,rowNum,colNum):
        if((rowNum,colNum) in self.getRemainingMoves()):
            return True
        return False
    
    """
    Checks and returns remaining possible moves
    """
    def getRemainingMoves(self):
        return self.remainingMoves
    
    """
    input of the current board and player its checking for
    copies the board and sets all non player moves to 0
    turns the board into a binary number
    does a binary and operation on the binary number and all of the solution numbers
    returns true if the and operation returns the solution number
    false elsewise
    """
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
        for ans in self.solutionSet:
            if(boardInt&ans == ans):
                return True
        return False
    
    def binaryCheck(self,boardInt):
        for ans in self.solutionSet:
            if(boardInt&ans == ans):
                return True
        return False