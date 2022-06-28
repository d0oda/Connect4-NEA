from turtle import width
from unittest import main
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
    print(*self.__board, sep = "\n")

  def displayBoard(self):
    for i in range(Game.HEIGHT):
      print(*self.__board[i], sep = " ")
      print(" ")

  def makeMove(self, column):
    column -= 1
    if self.validateMove(column) == True:
        for row in range(Game.HEIGHT - 1, -1, -1):
          if self.__board[row][column] == ".":
            self.__board[row][column] = "R" if self.__playerTurn == 1 else "Y"
            self.turnCounter()
            self.displayBoard()
            return
    print(Fore.RED + "Move invalid")
    return

  def validateMove(self, column):
    if column >= 0 and column < 7:
      if self.__board[0][column] != ".":
        return False
      return True
    return False

  def turnCounter(self):
    self.__playerTurn = 3 - self.__playerTurn
    if self.__playerTurn == 1:
      print(Back.RED + "Player 1's Turn: ")
    else:
      print(Back.YELLOW + "Player 2's Turn: ")
    return self.__playerTurn

  def checkWin(self):
    piece = "R" if self.__playerTurn == 1 else "Y"
    for column in range(Game.WIDTH - 3):
      for row in range(Game.HEIGHT):
        if self.__board[row][column] == piece and self.__board[row][column + 1] == piece and self.__board[row][column + 2] == piece and self.__board[row][column + 3] == piece:
          return True
        return False

    '''for column in range(Game.WIDTH):
      for row in range(Game.HEIGHT - 3):
        if self.__board[row][column] == piece and self.__board[row + 1][column] == piece and self.__board[row + 2][column] == piece and self.__board[row + 3][column] == piece:
          return True
        return False

    for column in range(Game.WIDTH - 3):
      for row in range(Game.HEIGHT - 3):
        if self.__board[row][column] == piece and self.__board[row + 1][column + 1] == piece and self.__board[row + 2][column + 2] == piece and self.__board[row + 3][column + 3] == piece:
          return True
        return False

    for column in range(Game.WIDTH - 3):
      for row in range(3, Game.HEIGHT):
        if self.__board[row][column] == piece and self.__board[row - 1][column + 1] == piece and self.__board[row - 2][column + 2] == piece and self.__board[row - 3][column + 3] == piece:
          return True
        return False'''

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
  game.gamemodeOption()
  while game.checkWin() == False:
    move = int(input("Make a move: "))
    game.makeMove(move)
  print("The winner is:")
