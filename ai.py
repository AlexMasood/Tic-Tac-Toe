import random
import numpy as np
import pickle
"""
Implementation of reinforcement AI based on code created by MJeremy2017
https://github.com/MJeremy2017/reinforcement-learning-implementation/blob/master/TicTacToe/tic-tac-toe.ipynb
"""

class AI:
    def __init__(self, name, expRate = 0.3):
        self.name = name
        self.states = []
        self.lr = 0.2
        self.expRate = expRate
        self.decayGamma = 0.9
        self.statesValues = {}
    
    def getHash(self,board):
        boardHash = str(board.reshape(9))
        return boardHash
    
    def getName(self):
        return self.name
    
    """
    takes list of positions, the numpy array of the current board, and the player as inputs.
    random move generated if random uniform number is below expRate
    each next potential legal move has its board created, hashed, and checked if in dictionary,If in dictionary value is set to value stored in the dictionary
    largest value is selected as its action 
    """
    def chooseAction(self, positions, currentBoard, symbol):
        if (np.random.uniform(0,1) <= self.expRate):
            idx = np.random.choice(len(positions))
            action = positions[idx]
        else:
            valueMax = -999
            for p in positions:
                nextBoard = currentBoard.copy()
                nextBoard[p[0],p[1]] = symbol
                nextBoardHash = self.getHash(nextBoard)
                if (self.statesValues.get(nextBoardHash) is None):
                    value = 0
                else:
                    value = self.statesValues.get(nextBoardHash)
                if(value >= valueMax):
                    valueMax = value
                    action = p
        return action
    
    def addState(self,state):
        self.states.append(state)

    """
    input of reward
    at the end of the game backpropagate update states value
    """
    def feedReward(self, reward):
        for st in reversed(self.states):
            if self.statesValues.get(st) is None:
                self.statesValues[st] = 0
            self.statesValues[st] += self.lr*(self.decayGamma*reward - self.statesValues[st])
            reward = self.statesValues[st]


    def reset(self):
        self.states = []

    def savePolicy(self):
        fw = open('policy_'+str(self.name),'wb')
        pickle.dump(self.statesValues, fw)
        fw.close()
    
    def loadPolicy(self,file):
        fr = open(file,'rb')
        self.statesValues = pickle.load(fr)
        fr.close()

    """
    Input of board object And player
    retrieves possible moves selects a random move plays move
    no validation needed since any remaining move is a legal move
    """
    def randomMove(self, board, player):
        moveList = board.getRemainingMoves(board.getBoard())
        moveCoord = random.choice(moveList)
        board.move(player,moveCoord[0],moveCoord[1])
        board.printBoard()
        