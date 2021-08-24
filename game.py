from board import Board as b
import numpy as np
class Game:
    def __init__(self):
        self.beingPlayed = True
    
    """
    whilst the game is being played,
    player 1 move
    check win condition
    else check draw condition (turn>8 without a win)
    else play player 2
    check win condition
    """
    def GameLoop(self):
        turn = 0
        board = b.createBoard()
        b.printBoard(board)
        while (self.beingPlayed):
            board = self.playerMove(board,1)
            turn += 1
            if(b.checkBoard(board, 1)):
                print("Player 1 has won")
                self.beingPlayed = False
            else:
                if(turn > 8):
                    print("Draw")
                    self.beingPlayed = False
                else:
                    board = self.playerMove(board,2)
                    turn += 1
                    if(b.checkBoard(board, 2)):
                        print("Player 2 has won")
                        self.beingPlayed = False

    """
    input of the current board and which players move it is
    asks for the row and column from the player
    validates that its a legal move and repeats the input if it is not
    inputs the players choice into the board
    prints the new board to terminal
    outputs the board
    """
    def playerMove(self,board,player):
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        while(not(0 <= row <= 2) or not(0 <= col <= 2) or b.checkMove(board,row,col) != True):
            print("Make sure the coordinate hasn't been previously used.")
            row = int(input("Enter row between or equal to 0 and 2: "))
            col = int(input("Enter column between or equal to 0 and 2: "))
        if(b.checkMove(board,row,col) == True):
            board = b.move(board,player,row,col)
        b.printBoard(board)
        return board
Game().GameLoop()