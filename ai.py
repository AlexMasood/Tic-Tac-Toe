import random
from board import Board as b
class AI:
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
        print("######")



            
