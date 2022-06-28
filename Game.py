from unittest import main


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
      option = input("Please enter a mode (t: terminal or g: gui)")
      if option == "t":
        self.setupBoard()
      elif option == "g":
        pass

  def setupBoard(self):
    for count in range(0, Game.HEIGHT):
      row = [Game.EMPTY] * Game.WIDTH
      self.__board.append(row)
    print(*self.__board, sep = "\n")

  def displayBoard(self):
    for i in range(Game.HEIGHT):
      print(*self.__board[i], sep = " ")
      print(" ")

  #validatecolumn
  #turncounter
  #validatemove
  #move
  #list of valid cols

  def validColumns(self):
    pass

  def makeMove(self, column):
    column -= 1
    if self.validateMove(column) == True:
        for row in range(Game.HEIGHT - 1, -1, -1):
          if self.__board[row][column] == ".":
            self.__board[row][column] = "R" if self.__playerTurn == 1 else "Y"
            self.turnCounter()
            self.displayBoard()
            return
    return "Move invalid"

  def validateMove(self, column):
    if self.__board[0][column] != ".":
      return False
    return True

  def turnCounter(self):
    self.__playerTurn = 3 - self.__playerTurn
    return self.__playerTurn

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

  def winner(self):
    return False

class Player():
  def __init__(self, name):
    self.__name = name

if __name__ == "__main__":
  game = Game()
  game.gamemodeOption()
  while game.winner() == False:
    move = int(input("Make a move: "))
    game.makeMove(move)
