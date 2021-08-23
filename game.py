from board import Board as b
import numpy as np
class Game:
    def __init__(self):
        self.beingPlayed = True
    
    
    def GameLoop(self):
        turn = 0
        board = b.createBoard()
        b.printBoard(board)
        while (self.beingPlayed):
            board = self.playerMove(board,1)
            turn += 1
            if(b.checkBoard(board, 1)):
                print("player 1 has won")
                self.beingPlayed = False
            else:
                if(turn > 8):
                    print("draw")
                    self.beingPlayed = False
                else:
                    board = self.playerMove(board,2)
                    turn += 1
                    if(b.checkBoard(board, 2)):
                        print("player 2 has won")
                        self.beingPlayed = False


    def playerMove(self,board,player):
        row = int(input("enter row: "))
        col = int(input("enter column: "))
        while((0 <= row <= 2) and (0 <= col <= 2) and b.checkMove(board,row,col) != True):
            row = int(input("enter row between or equal to 0 and 2: "))
            col = int(input("enter column between or equal to 0 and 2: "))
        
        print(b.checkMove(board,row,col))
        if(b.checkMove(board,row,col) == True):
            board = b.move(board,player,row,col)
        b.printBoard(board)
        return board
g = Game()
g.GameLoop()
