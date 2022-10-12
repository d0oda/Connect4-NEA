from colorama import Fore, Back

class Game():
  EMPTY = "."
  HEIGHT = 6
  WIDTH = 7
  REDS = 0
  YELLOWS = 0
  #EMPTY = " "
  
  def __init__(self):
    self.__playerTurn = 1
    self.__board = [[Game.EMPTY for _ in range(Game.WIDTH)] for _ in range(Game.HEIGHT)]
    #self.__board = []

  def playAgain(self):
    option = input("Do you want to play again? (ng: new game or e: exit) ")
    if option == "ng":
      return True
    elif option == "e":
      return False
    print(Fore.RED + 'No mode was entered')
    self.playAgain()

  def at(self, row, col):
        row -= 1 #change to 0 based
        col -= 1
        return self.__board[row][col]

  def setupBoard(self):
    for count in range(0, Game.HEIGHT):
      row = [Game.EMPTY] * Game.WIDTH
      self.__board.append(row)

  def validateMove(self, column):
    return column >= 0 and column < Game.WIDTH and self.__board[0][column] == "."

  def turnCounter(self):
    self.__playerTurn = 3 - self.__playerTurn
    return self.__playerTurn
    """if (self.REDS + self.YELLOWS) % 2 == 0:
      self.__playerTurn = 1
    else:
      self.__playerTurn = 2"""

  def checkWin(self):
    piece = "R" if self.__playerTurn == 1 else "Y"
    for row in range(Game.HEIGHT):
      for column in range(Game.WIDTH - 3):
        if self.__board[row][column] == piece and self.__board[row][column + 1] == piece and self.__board[row][column + 2] == piece and self.__board[row][column + 3] == piece:
          return True

    for column in range(Game.WIDTH):
      for row in range(Game.HEIGHT - 3):
        if self.__board[row][column] == piece and self.__board[row + 1][column] == piece and self.__board[row + 2][column] == piece and self.__board[row + 3][column] == piece:
          return True

    for column in range(Game.WIDTH - 3):
      for row in range(Game.HEIGHT - 3):
        if self.__board[row][column] == piece and self.__board[row + 1][column + 1] == piece and self.__board[row + 2][column + 2] == piece and self.__board[row + 3][column + 3] == piece:
          return True

    for column in range(Game.WIDTH - 3):
      for row in range(3, Game.HEIGHT):
        if self.__board[row][column] == piece and self.__board[row - 1][column + 1] == piece and self.__board[row - 2][column + 2] == piece and self.__board[row - 3][column + 3] == piece:
          return True

    return False

  def checkDraw(self):
    red = 0
    yellow = 0
    empty = 0
    for i in self.__board:
      for j in i:
        if j == "R":
          red += 1
        elif j == "Y":
          yellow += 1
        else:
          empty += 1
    self.REDS = red
    self.YELLOWS = yellow
    if(yellow == 21 and red == 21):
      return True
    return False