class Player:
    def __init__(self,name):
        self.name = name
    
    def getName(self):
        return self.name
    """
    Input of remaining positions the board and the player
    ask for the input of the row and column
    whilst row and column are not in the positions list repeats question
    add to board
    """
    def chooseAction(self,positions,board,player):
        print("It is player "+str(player)+"'s turn.")
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        while([row,col] not in positions):
            print("Make sure the coordinate hasn't been previously used.")
            row = int(input("Enter row between or equal to 0 and 2: "))
            col = int(input("Enter column between or equal to 0 and 2: "))
        return [row,col]
    
    def addState(self,state):
        pass
    def feedReward(self):
        pass
    def reset(self):
        pass
