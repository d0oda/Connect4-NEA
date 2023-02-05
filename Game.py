import random
import colorama
from colorama import Fore, Back
import sqlite3
import math
from copy import copy, deepcopy

class GameError(Exception):
  pass





class Game():
  def __init__(self):
    self.EMPTY = "."
    self.HEIGHT = 6
    self.WIDTH = 7
    self.REDS = 0
    self.YELLOWS = 0
    self.playerTurn = 1
    self.x = 0
    self.y = 0
    #self.board = [[self.EMPTY for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
    self.board = []


  def getBoard(self):
    #print(type(self.board))
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
###########################################################
#
# CATEGORY A SKILL: LIST OPERATIONS
# storing the game board as a 2D array
#
###########################################################
    for count in range(0, self.HEIGHT):
      row = [self.EMPTY] * self.WIDTH
      self.board.append(row)


  def validateMove(self, column):
    try:
      if column == None:
        raise ValueError("empty")
      column = int(column)
    except:
      return False
    #print(column)
    #print(self.board)
    return column >= 0 and column < self.WIDTH and self.board[0][column] == "."
  

  def getValidColumns(self):
    availableColumns = []
    for column in range(self.WIDTH):
      if self.validateMove(column):
        availableColumns.append(column)
    return availableColumns


  def turnCounter(self):
    self.playerTurn = 3 - self.playerTurn
    #print('******', self.playerTurn)
    return self.playerTurn
    """if (self.REDS + self.YELLOWS) % 2 == 0:
      self.playerTurn = 1
    else:
      self.playerTurn = 2"""

  def simulateMove(self, bdr, row, column, piece):
    bdr[row][column] = piece


  def placeMove(self, column):
    self.y = column
    #print("placemove", self.playerTurn)
    column -= 1
    #if self.validateMove(column): # move is valid 
    for row in range(self.HEIGHT - 1, -1, -1):
      #print("*****", row,column)
      if self.board[row][column] == ".":
        #print(f"getPlayerTurn: {self.getPlayerTurn, self.getPlayerTurn()}")
        self.board[row][column] = "R" if self.getPlayerTurn() == 1 else "Y"
        self.x = row
        turn = self.turnCounter()
        break
    """else:
      print(Fore.RED + "Move invalid")
      return False
      #raise GameError("Move invalid")"""


  def getPosOfNewPiece(self):
    return [self.x,self.y]


  def checkWin(self):
    #print(self.board)
    #horizontal check
    piece = "R" if self.playerTurn == 2 else "Y"
    for row in range(self.HEIGHT):
      for column in range(self.WIDTH - 3):
        #print(row, column)
        if self.board[row][column] == piece and self.board[row][column + 1] == piece and self.board[row][column + 2] == piece and self.board[row][column + 3] == piece:
          flag = 1
          #print(piece, "wins 1")
          return [flag, piece]

    #vertical check
    for column in range(self.WIDTH):
      for row in range(self.HEIGHT - 3):
        if self.board[row][column] == piece and self.board[row + 1][column] == piece and self.board[row + 2][column] == piece and self.board[row + 3][column] == piece:
          flag = 1
          #print(row, column)
          #print(piece, "wins 2")
          return [flag, piece]

    #upward diagonal
    for column in range(self.WIDTH - 3):
      for row in range(self.HEIGHT - 3):
        #print(row, column)
        if self.board[row][column] == piece and self.board[row + 1][column + 1] == piece and self.board[row + 2][column + 2] == piece and self.board[row + 3][column + 3] == piece:
          flag = 1
          #print(piece, "wins 3")
          return [flag, piece]

    #downward diagonal
    for column in range(self.WIDTH - 3):
      for row in range(3, self.HEIGHT):
        #print(row, column)
        if self.board[row][column] == piece and self.board[row - 1][column + 1] == piece and self.board[row - 2][column + 2] == piece and self.board[row - 3][column + 3] == piece:
          flag = 1
          #print(piece, "wins 4")
          return [flag, piece]
    flag = 2
    return [flag, piece]


  def checkWin_ai(self, b):
    #print(self.board)
    #horizontal check
    piece = "R" if self.playerTurn == 2 else "Y"
    for row in range(self.HEIGHT):
      for column in range(self.WIDTH - 3):
        #print(row, column)
        if b[row][column] == piece and b[row][column + 1] == piece and b[row][column + 2] == piece and b[row][column + 3] == piece:
          flag = 1
          #print(piece, "wins 1")
          return [flag, piece]

    #vertical check
    for column in range(self.WIDTH):
      for row in range(self.HEIGHT - 3):
        if b[row][column] == piece and b[row + 1][column] == piece and b[row + 2][column] == piece and b[row + 3][column] == piece:
          flag = 1
          #print(row, column)
          #print(piece, "wins 2")
          return [flag, piece]

    #upward diagonal
    for column in range(self.WIDTH - 3):
      for row in range(self.HEIGHT - 3):
        #print(row, column)
        if b[row][column] == piece and b[row + 1][column + 1] == piece and b[row + 2][column + 2] == piece and b[row + 3][column + 3] == piece:
          flag = 1
          #print(piece, "wins 3")
          return [flag, piece]

    #downward diagonal
    for column in range(self.WIDTH - 3):
      for row in range(3, self.HEIGHT):
        #print(row, column)
        if b[row][column] == piece and b[row - 1][column + 1] == piece and b[row - 2][column + 2] == piece and b[row - 3][column + 3] == piece:
          flag = 1
          #print(piece, "wins 4")
          return [flag, piece]
    flag = 2
    return [flag, piece]
  
  def consecutivePieces(self, n, piece):
    sequence = 0
    for row in range(self.HEIGHT):
      for col in range(self.WIDTH-n+1):
        if self.board[row][col:col+n] == [piece for i in range(n)]:
          sequence += 1
    #print("This is what we are checking: ", row, col)
    #print(self.board)
    for col in range(self.WIDTH):
      for row in range(self.HEIGHT-n+1):
        #print("This is what we are checking: ", col, row)
        print(f"this is row {row}, this is row+n {row+n}, this is col {col}")
        print(self.board)
        verticalPieces = [r[col] for r in self.board[row:row+n]]
        if verticalPieces == [piece for i in range(n)]:
          sequence += 1

    for col in range(self.WIDTH-n+1):
      for row in range(self.HEIGHT-n+1):
        if self.board[row:row+n][col:col+n] == [piece for i in range(n)]:
          sequence += 1

    for col in range(self.WIDTH-n+1):
      for row in range(self.HEIGHT):
        if self.board[row][col:col+n] == [piece for i in range(n)]:
          sequence += 1
    
    return sequence

  def boardAttractiveness(self, board, piece):
    eval = 0
    centreColumn = [i for i in board[:][self.WIDTH//2]]
    pieceNo = centreColumn.count(piece)
    eval += pieceNo * 4

    for i in range(2,5):
      print("This is boardAttractiveness i", i)
      noOfSequences = self.consecutivePieces(i, piece)
      if i == 2:
        eval += noOfSequences * 2
      elif i == 3:
        eval += noOfSequences * 6
      elif i == 4:
        eval += noOfSequences * 1000000
    return eval


  
  def isTerminal(self, board):
    if self.checkWin_ai(board)[0] == 1 or self.getValidColumns() == []:
      return True
    return False


  def checkDraw(self):
    red = 0
    yellow = 0
    empty = 0
    for row in self.board:
      for square in row:
        if square == "R":
          red += 1
        elif square == "Y":
          yellow += 1
        else:
          empty += 1
    self.REDS = red
    self.YELLOWS = yellow
    if(yellow == 21 and red == 21):
      return True
    return False
  
  #checks where the piece will fall in the current column
  def openRow(self, column, board):
    for i in range(self.HEIGHT-1, -1, -1):
      #print("This is the row number: ", i)
      if board[i][column] == ".":
        return i



class AI():
  def __init__(self,game):
    self.g = game

  def findMove(self):
    available = self.g.getValidColumns()
    return random.choice(available)

  def sortScores(self, eval):
    #print(eval)
    if len(eval) > 1:
      mid = len(eval)//2
      arr1 = eval[:mid]
      arr2 = eval[mid:]

      self.sortScores(arr1)
      self.sortScores(arr2)

      i=0
      j=0
      k=0

      while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
          eval[k] = arr1[i]
          i += 1
        else:
          eval[k] = arr2[j]
          j += 1
        k += 1
      
      while i < len(arr1):
        eval[k] = arr1[i]
        i += 1
        k += 1

      while j < len(arr2):
        eval[k] = arr2[j]
        j += 1
        k += 1
    
    return eval

    """for i in range(len(eval)):
        print(eval[i], end=" ")
    print()"""

  def miniMax(self, board, depth, maximising):
    alpha = -math.inf
    beta = math.inf
    available = self.g.getValidColumns()
    boardTerm = self.g.isTerminal(board)
    AIPiece = "Y"
    PLAYERPiece = "R"

    if depth == 0 or boardTerm:
      if boardTerm:
        if self.g.checkWin_ai(board)[0] == 1 and self.g.checkWin_ai(board)[1] == AIPiece:
          return (None, 100000000)
        elif self.g.checkWin_ai(board)[0] == 1 and self.g.checkWin_ai(board)[1] == PLAYERPiece:
          return (None, -100000000)
        else:
          return (None, 0)
      else:
        score = self.g.boardAttractiveness(board, AIPiece)
        return (None, score)

    if maximising is True:
      print(board)
      boardCopy = deepcopy(board)
      bestScore = -math.inf
      bestColumn = self.findMove()
      #print("Best Column: ", bestColumn)
      scoreColumns = []
      for c in available:
        nextOpenRow = self.g.openRow(bestColumn, boardCopy)
        self.g.simulateMove(boardCopy, nextOpenRow, c, AIPiece)
        nextScore = self.miniMax(boardCopy, depth -1, False)[1]
        scoreColumns.append(nextScore)
      print("Score for columns: ", scoreColumns)

      bestScore = self.sortScores(scoreColumns)[-1]
      alpha = max(bestScore, alpha)
      if alpha >= beta:
        print("AI went crazy")
        quit()
        """if nextScore > bestScore:
          bestScore = nextScore
          bestColumn = c"""

        

      return bestColumn, bestScore

    else:
      boardCopy = board
      worstScore = math.inf
      worstColumn = self.findMove()
      scoreColumns = []
      for c in available:
        nextOpenRow = self.g.openRow(worstColumn, boardCopy)
        self.g.simulateMove(boardCopy, nextOpenRow, c, PLAYERPiece)
        nextScore = self.miniMax(boardCopy, depth - 1, True)[1]
        scoreColumns.append(nextScore)

      worstScore = self.sortScores(scoreColumns)[0]
      beta = min(worstScore, beta)
      if beta <= alpha:
        print("AI went crazy")
        quit()
        """if nextScore < worstScore:
          worstScore = nextScore
          worstColumn = c"""
        


      return worstColumn, worstScore