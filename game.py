from numpy.core.arrayprint import format_float_scientific
from board import Board as b
from ai import AI
from player import Player
import pygame
"""
Implementation of reinforcement AI based on code created by MJeremy2017
https://github.com/MJeremy2017/reinforcement-learning-implementation/blob/master/TicTacToe/tic-tac-toe.ipynb
"""
class Game:
    def __init__(self, p1, p2,row = 3,col = 3,pygame = True):
        self.beingPlayed = True
        self.p1 = p1
        self.p2 = p2
        self.pygame = pygame
        self.row = row
        self.col = col
        self.pixelSize = 100
    """
    Input of the current board object
    Feed both AI based on winner or draw
    """
    def giveReward(self,boardObj):
        if(boardObj.checkBoard(1)):
            self.p1.feedReward(1)
            self.p2.feedReward(0)
        elif(boardObj.checkBoard(2)):
            self.p1.feedReward(0)
            self.p2.feedReward(1)
        else:
            self.p1.feedReward(0.1)
            self.p2.feedReward(0.5)
    
    """
    Input board row, board column, win number, and of how many rounds will be played
    Finds legal moves, decide the best course of action adds states as a board hash
    Checks board win condition, assigns reward and resets if game is over
    repeats for the second AI

    """
    def aIVsAI(self, row, col, winNum, rounds = 100):
        for i in range(rounds):
            #if(i%1 == 0):
            print("rounds {}".format(i))
            boardObj = b(row, col, winNum)
            while (self.beingPlayed):
                positions = boardObj.getRemainingMoves(boardObj.getBoard())
                p1Action = self.p1.chooseAction(positions, boardObj.getBoard(), 1)
                boardObj.move(1,p1Action[0],p1Action[1])
                boardHash = boardObj.getHash()
                boardShrinkHash = boardObj.getShrinkHash()
                self.p1.addState(boardHash)
                self.p1.addState(boardShrinkHash)

                if((boardObj.checkBoard(1)) or not(boardObj.getRemainingMoves(boardObj.getBoard()))):
                    self.giveReward(boardObj)
                    self.p1.reset()
                    self.p2.reset()
                    boardObj.reset()
                    break
                else:
                    positions = boardObj.getRemainingMoves(boardObj.getBoard())
                    p2Action = self.p2.chooseAction(positions, boardObj.getBoard(), 2)
                    boardObj.move(2,p2Action[0],p2Action[1])
                    boardHash = boardObj.getHash()
                    boardShrinkHash = boardObj.getShrinkHash()
                    self.p2.addState(boardHash)
                    self.p2.addState(boardShrinkHash)

                    if((boardObj.checkBoard(2)) or not(boardObj.getRemainingMoves(boardObj.getBoard()))):
                        self.giveReward(boardObj)
                        self.p1.reset()
                        self.p2.reset()
                        boardObj.reset()
                        break
    
    """
    Inputs of board rows, board columns, and win number
    Inputs of row column and win number
    Single game of tic-tac-toe with no rewards on win or draw
    Use function computerFirstGame or humanFirstGame to choose who is first
    """
    def humanVsAI(self, row, col, winNum):
        boardObj = b(row, col, winNum)
        boardObj.printBoard()
        print("######")
        while (self.beingPlayed):
            positions = boardObj.getRemainingMoves(boardObj.getBoard())
            p1Action = self.p1.chooseAction(positions, boardObj.getBoard(), 1)
            boardObj.move(1,p1Action[0],p1Action[1])
            boardHash = boardObj.getHash()
            self.p1.addState(boardHash)
            boardObj.printBoard()
            print("######")

            if(boardObj.checkBoard(1)):
                print(self.p1.getName() + " has won")
                boardObj.reset()
                break
            elif not(boardObj.getRemainingMoves(boardObj.getBoard())):
                print("draw")
                boardObj.reset()
                break
            else:
                positions = boardObj.getRemainingMoves(boardObj.getBoard())
                p2Action = self.p2.chooseAction(positions, boardObj.getBoard(), 2)
                boardObj.move(2,p2Action[0],p2Action[1])
                boardHash = boardObj.getHash()
                self.p2.addState(boardHash)
                boardObj.printBoard()
                print("######")
                if(boardObj.checkBoard(2)):
                    print(self.p2.getName() + " has won")
                    boardObj.reset()
                    break

    def pgHumanvsAI(self, row, col, winNum):
        boardObj = b(row, col, winNum)
        loop = True
        humanTurn = True
        while loop:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    loop = False
                if(pygame.mouse.get_pressed()[0]):#left
                    if(humanTurn):
                        pos = pygame.mouse.get_pos()

                        p1Action = [int(pos[0]/self.pixelSize),int(pos[1]/self.pixelSize)]
                        print(p1Action)
                        boardObj.move(1,p1Action[0],p1Action[1])
                        boardHash = boardObj.getHash()
                        self.p1.addState(boardHash)
                        humanTurn = not humanTurn
                        if(boardObj.checkBoard(1)):
                            print(self.p1.getName() + " has won")
                            boardObj.reset()
                            break
                        elif not(boardObj.getRemainingMoves(boardObj.getBoard())):
                            print("draw")
                            boardObj.reset()
                            break
            if(not humanTurn):

                positions = boardObj.getRemainingMoves(boardObj.getBoard())
                p2Action = self.p2.chooseAction(positions, boardObj.getBoard(), 2)
                boardObj.move(2,p2Action[0],p2Action[1])
                boardHash = boardObj.getHash()
                self.p2.addState(boardHash)
                boardObj.printBoard()
                print("######")
                if(boardObj.checkBoard(2)):
                    print(self.p2.getName() + " has won")
                    boardObj.reset()
                    #break
                humanTurn = not humanTurn

            img = pygame.surfarray.make_surface(boardObj.getBoard())
            img = pygame.transform.scale(img, (row * self.pixelSize,col * self.pixelSize))
            #draw to the screen
            self.screen.fill((0,0,0)) 
            self.screen.blit(img,(0,0))
            pygame.display.flip()
        #pygame.quit()

    """
    Inputs of board rows, board columns, and win number
    whilst the game is being played,
    player 1 move
    check win condition
    else check draw condition (turn>8 without a win)
    else play player 2
    check win condition
    """
    def humanVsHuman(self, rowLen, colLen, winNum):
        boardObj = b(rowLen, colLen, winNum)
        boardObj.printBoard()
        while (self.beingPlayed):
            positions = boardObj.getRemainingMoves(boardObj.getBoard())
            p1Action = self.p1.chooseAction(positions, boardObj.getBoard(), 1)
            boardObj.move(1,p1Action[0],p1Action[1])
            boardObj.printBoard()
            if(boardObj.checkBoard(1)):
                print(self.p1.getName() + " has won")
                self.beingPlayed = False
            else:
                if(not boardObj.getRemainingMoves(boardObj.getBoard())):
                    print("Draw")
                    self.beingPlayed = False
                else:
                    positions = boardObj.getRemainingMoves(boardObj.getBoard())
                    p2Action = self.p2.chooseAction(positions, boardObj.getBoard(), 2)
                    boardObj.move(2,p2Action[0],p2Action[1])
                    boardObj.printBoard()
                    if(boardObj.checkBoard(2)):
                        print(self.p2.getName() + " has won")
                        self.beingPlayed = False

    def setupScreen(self):
        pygame.display.set_mode((self.col*self.pixelSize,self.row*self.pixelSize))
        self.screen = pygame.display.get_surface()
"""
Inputs of repeated training, board rows, board columns, and win number
Sets up, trains, and saves the AI
"""
def trainAI(repitions, row,col,winNum):
    p1 = AI("p1")
    p2 = AI("p2")
    st = Game(p1, p2)
    print("training...")
    st.aIVsAI(row,col, winNum, repitions)
    p1.savePolicy(row,col,winNum)
    p2.savePolicy(row,col,winNum)

"""
Inputs of board rows, board columns, and win number
Loads computers AI is first player
"""  
def computerFirstGame(row,col,winNum):
    p1 = AI("computer", expRate = 0)
    p2 = Player("Human")
    p1.loadPolicy(row, col, winNum, "p1")

    st = Game(p1,p2)
    st.humanVsAI(row,col, winNum)

"""
Inputs of board rows, board columns, and win number
Loads computers AI second player
"""
def humanFirstGame(row,col,winNum):
    

    p1 = Player("Human")
    p2 = AI("computer", expRate = 0)
    p2.loadPolicy(row, col, winNum, "p2")

    st = Game(p1,p2)
    if(st.pygame):
        pygame.init()
        st.setupScreen()
        st.pgHumanvsAI(row,col, winNum)
    else:
        st.humanVsAI(row,col, winNum) 
"""
Inputs of board rows, board columns, and win number
"""
def humanVsHumanGame(row,col,winNum):
    p1 = Player("Human1")
    p2 = Player("Human2")
    st = Game(p1,p2)
    st.humanVsHuman(row,col, winNum)

#trainAI(1000,15,15,5)
humanFirstGame(3,3,3)
#humanVsHumanGame(10,10,5)