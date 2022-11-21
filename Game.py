from colorama import Fore, Back

class Game():
  def __init__(self):
    self.EMPTY = "."
    self.HEIGHT = 6
    self.WIDTH = 7
    self.REDS = 0
    self.YELLOWS = 0
    self.playerTurn = 2
    self.board = [[self.EMPTY for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
    #self.board = []
    

  def getBoard(self):
    print(type(self.board))
    return self.board

  def getBoardAttribute(self):
    return self.EMPTY, self.HEIGHT, self.WIDTH, self.REDS, self.YELLOWS

  def getPlayerTurn(self):
    return self.playerTurn
    
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
        return self.board[row][col]

  def setupBoard(self):
    for count in range(0, self.HEIGHT):
      row = [self.EMPTY] * self.WIDTH
      self.board.append(row)

  def validateMove(self, column):
    return column >= 0 and column < self.WIDTH and self.board[0][column] == "."

  def turnCounter(self):
    self.playerTurn = 3 - self.playerTurn
    print('******', self.playerTurn)
    return self.playerTurn
    """if (self.REDS + self.YELLOWS) % 2 == 0:
      self.playerTurn = 1
    else:
      self.playerTurn = 2"""

  def placeMove(self, column):
    print("placemove", self.playerTurn)
    column -= 1
    if self.validateMove(column): # move is valid 
      for row in range(self.HEIGHT - 1, -1, -1):
        if self.board[row][column] == ".":
          print(f"getPlayerTurn: {self.getPlayerTurn, self.getPlayerTurn()}")
          self.board[row][column] = "R" if self.getPlayerTurn() == 1 else "Y"
          turn = self.turnCounter()
          print(Fore.RED + "Move invalid")

  def checkWin(self):
    piece = "R" if self.playerTurn == 1 else "Y"
    for row in range(self.HEIGHT):
      for column in range(self.WIDTH - 3):
        if self.board[row][column] == piece and self.board[row][column + 1] == piece and self.board[row][column + 2] == piece and self.board[row][column + 3] == piece:
          return True

    for column in range(self.WIDTH):
      for row in range(self.HEIGHT - 3):
        if self.board[row][column] == piece and self.board[row + 1][column] == piece and self.board[row + 2][column] == piece and self.board[row + 3][column] == piece:
          return True

    for column in range(self.WIDTH - 3):
      for row in range(self.HEIGHT - 3):
        if self.board[row][column] == piece and self.board[row + 1][column + 1] == piece and self.board[row + 2][column + 2] == piece and self.board[row + 3][column + 3] == piece:
          return True

    for column in range(self.WIDTH - 3):
      for row in range(3, self.HEIGHT):
        if self.board[row][column] == piece and self.board[row - 1][column + 1] == piece and self.board[row - 2][column + 2] == piece and self.board[row - 3][column + 3] == piece:
          return True

    return False

  def checkDraw(self):
    red = 0
    yellow = 0
    empty = 0
    for i in self.board:
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