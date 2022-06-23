class Game():

  EMPTY = " "

  def __init__(self, player1, player2):
    self.__player1 = Player()
    self.__player2 = Player()
    self.__board = []

  def setupBoard(self):
    for count in range(0, 6):
      row = [Game.EMPTY] * 7
      self.__board.append(row)
    '''print(*self.__board, sep = "\n")'''

class Player():
  pass

game1 = Game("1", "2")
game1.setupBoard()