import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)


class Game():

  EMPTY = "."
  HEIGHT = 6
  WIDTH = 7

  def __init__(self):
    self.__player1 = Player("Player 1")
    self.__player2 = Player("Player 2")
    self.__playerTurn = 1
    self.__board = []

  def gamemodeOption(self):
      option = input("Please enter a mode (t: terminal or g: gui) ")
      if option == "t":
        self.setupBoard()
      elif option == "g":
        pass
      else:
        print(Fore.RED + 'No mode was entered')
        self.gamemodeOption()

  def setupBoard(self):
    for count in range(0, Game.HEIGHT):
      row = [Game.EMPTY] * Game.WIDTH
      self.__board.append(row)

  def displayBoard(self):
    for i in range(1, Game.WIDTH + 1, 1):
      print(i, end = " ")
    print(" ")
    for j in range(Game.HEIGHT):
      print(*self.__board[j], sep = " ")
      print(" ")

  def placeMove(self, column):
    column -= 1
    if self.validateMove(column):
      for row in range(Game.HEIGHT - 1, -1, -1):
        if self.__board[row][column] == ".":
          self.__board[row][column] = "R" if self.__playerTurn == 1 else "Y"
          return
    print(Fore.RED + "Move invalid")

  def validateMove(self, column):
    return column >= 0 and column < Game.WIDTH and self.__board[0][column] == "."

  def turnCounter(self):
    self.__playerTurn = 3 - self.__playerTurn
    
  def displayTurn(self):
    if self.__playerTurn == 1:
      print(Back.RED + "Player 1's Turn ")
    else:
      print(Back.YELLOW + "Player 2's Turn ")
    return self.__playerTurn

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
    if(yellow == 21 and red == 21):
      return True
    return False

class Player():
  def __init__(self, name):
    self.__name = name

if __name__ == "__main__":
  game = Game()
  game.gamemodeOption()
  game.displayBoard()
  while True:
    game.displayTurn()
    move = int(input("Make a move: "))
    game.placeMove(move)
    game.displayBoard()
    if game.checkWin():
      print("The winner is:")
      break
    if game.checkDraw():
      print("Game Drawn")
      break
    game.turnCounter()
