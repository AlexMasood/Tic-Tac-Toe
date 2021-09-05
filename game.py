from board import Board as b
from ai import AI
from player import Player
"""
Implementation of reinforcement AI based on code created by MJeremy2017
https://github.com/MJeremy2017/reinforcement-learning-implementation/blob/master/TicTacToe/tic-tac-toe.ipynb
"""
class Game:
    def __init__(self, p1, p2):
        self.beingPlayed = True
        self.p1 = p1
        self.p2 = p2
    
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
    Input of how many rounds will be played
    Finds legal moves, decide the best course of action adds states as a board hash
    Checks board win condition, assigns reward and resets if game is over
    repeats for the second AI

    """
    def aIVsAI(self,rounds = 100):
        for i in range(rounds):
            if(i%10000 == 0):
                print("rounds {}".format(i))
            boardObj = b()
            while (self.beingPlayed):
                positions = boardObj.getRemainingMoves(boardObj.getBoard())
                p1Action = self.p1.chooseAction(positions, boardObj.getBoard(), 1)
                boardObj.move(1,p1Action[0],p1Action[1])
                boardHash = boardObj.getHash()
                self.p1.addState(boardHash)

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
                    self.p2.addState(boardHash)

                    if((boardObj.checkBoard(2)) or not(boardObj.getRemainingMoves(boardObj.getBoard()))):
                        self.giveReward(boardObj)
                        self.p1.reset()
                        self.p2.reset()
                        boardObj.reset()
                        break
    
    """
    Single game of tic-tac-toe with no rewards on win or draw
    """
    def humanVsAI(self):
        boardObj = b()
        boardObj.printBoard()
        while (self.beingPlayed):
            positions = boardObj.getRemainingMoves(boardObj.getBoard())
            p1Action = self.p1.chooseAction(positions, boardObj.getBoard(), 1)
            boardObj.move(1,p1Action[0],p1Action[1])
            boardHash = boardObj.getHash()
            self.p1.addState(boardHash)
            boardObj.printBoard()

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
                if(boardObj.checkBoard(2)):
                    print(self.p2.getName() + " has won")
                    boardObj.reset()
                    break

    """
    whilst the game is being played,
    player 1 move
    check win condition
    else check draw condition (turn>8 without a win)
    else play player 2
    check win condition
    """
    def humanVsHuman(self,player1, player2):
        turn = 0
        firstPlayer = Player(player1)
        secondPlayer = Player(player2)
        boardObj = b()
        boardObj.printBoard()
        while (self.beingPlayed):
            firstPlayer.playerMove(boardObj,1)
            turn += 1
            if(boardObj.checkBoard(1)):
                print(firstPlayer.getName() + " has won")
                self.beingPlayed = False
            else:
                if(turn > 8):
                    print("Draw")
                    self.beingPlayed = False
                else:
                    secondPlayer.playerMove(boardObj,2)
                    turn += 1
                    if(boardObj.checkBoard(2)):
                        print(secondPlayer.getName() + " has won")
                        self.beingPlayed = False

"""
Sets up, trains, and saves the AI
"""
def trainAI(repitions):
    p1 = AI("p1")
    p2 = AI("p2")
    st = Game(p1, p2)
    print("training...")
    st.aIVsAI(repitions)
    p1.savePolicy()
    p2.savePolicy()

"""
Loads computers AI is first player
"""  
def computerFirst():
    p1 = AI("computer", expRate = 0)
    p2 = Player("Human")
    p1.loadPolicy("policy_p1")

    st = Game(p1,p2)
    st.humanVsAI()

"""
Loads computers AI second player
"""
def humanFirst():
    p1 = Player("Human")
    p2 = AI("computer", expRate = 0)
    p2.loadPolicy("policy_p2")

    st = Game(p1,p2)
    st.humanVsAI() 


trainAI(50000)
computerFirst()
