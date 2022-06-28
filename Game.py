from unittest import main


class Game():

  EMPTY = "."

  def __init__(self):
    self.__player1 = Player("Player 1")
    self.__player2 = Player("Player 2")
    self.__board = []

  def gamemodeOption(self):
      option = input("Please enter a mode (t: terminal or g: gui)")
      if option == "t":
        self.setupBoard()
        self.displayBoard()
      elif option == "g":
        pass



  def setupBoard(self):
    for count in range(0, 6):
      row = [Game.EMPTY] * 7
      self.__board.append(row)
    print(self.__board)
    
    '''for i in range(6):
      print("")
      for j in range(7):
        print(self.__board[i][j])'''

  def displayBoard(self):
    """print(*self.__board, sep = "\n")"""
    for i in range(6):
      print("")
      for j in range(7):
        print(self.__board[i][j])

  #validatecolumn
  #turncounter
  #validatemove
  #move
  #list of valid cols

  def validColumns(self):
    pass

  def makeMove(self):
    pass

  def validateMove(self):
    pass

  def turnCounter(self):
    pass

  def validateBoard(self):
    red = 0
    yellow = 0
    empty = 0
    for i in board:
        for j in i:
            if board[j] == "R":
                red += 1
            elif board[j] == "Y":
                yellow += 1
            else:
                empty += 1
    if(yellow == 42 or red == 42):
      return False
    return True

class Player():
  def __init__(self, name):
    self.__name = name

if __name__ == "__main__":
  game = Game()
  game.setupBoard()
