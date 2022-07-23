from tkinter.tix import TEXT
from turtle import right
import colorama
from colorama import Fore, Back
colorama.init(autoreset = True)

from abc import ABC, abstractmethod
from tkinter import *
from itertools import product

class UI(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError




class Terminal(UI):

  EMPTY = "."
  HEIGHT = 6
  WIDTH = 7
  REDS = 0
  YELLOWS = 0

  def __init__(self):
    self.__player1 = Player("Player 1")
    self.__player2 = Player("Player 2")
    self.__playerTurn = 1
    self.__board = []

  

  def playAgain(self):
    option = input("Do you want to play again? (ng: new game or e: exit) ")
    if option == "ng":
      return True
    elif option == "e":
      return False
    print(Fore.RED + 'No mode was entered')
    self.playAgain()

  def setupBoard(self):
    for count in range(0, self.HEIGHT):
      row = [self.EMPTY] * self.WIDTH
      self.__board.append(row)

  def displayBoard(self):
    for i in range(1, self.WIDTH + 1, 1):
      print(i, end = " ")
    print(" ")
    for j in range(self.HEIGHT):
      print(*self.__board[j], sep = " ")
      print(" ")

  def placeMove(self, column):
    column -= 1
    if self.validateMove(column):
      for row in range(self.HEIGHT - 1, -1, -1):
        if self.__board[row][column] == ".":
          self.__board[row][column] = "R" if self.__playerTurn == 1 else "Y"
          return
    print(Fore.RED + "Move invalid")

  def validateMove(self, column):
    return column >= 0 and column < self.WIDTH and self.__board[0][column] == "."

  def turnCounter(self):
    #self.__playerTurn = 3 - self.__playerTurn
    if (self.REDS + self.YELLOWS) % 2 == 0:
      self.__playerTurn = 1
    else:
      self.__playerTurn = 2
    
  def displayTurn(self):
    if self.__playerTurn == 1:
      print(Back.RED + "Player 1's Turn ")
    else:
      print(Back.YELLOW + "Player 2's Turn ")
    return self.__playerTurn

  def checkWin(self):
    piece = "R" if self.__playerTurn == 1 else "Y"
    for row in range(self.HEIGHT):
      for column in range(self.WIDTH - 3):
        if self.__board[row][column] == piece and self.__board[row][column + 1] == piece and self.__board[row][column + 2] == piece and self.__board[row][column + 3] == piece:
          return True

    for column in range(self.WIDTH):
      for row in range(self.HEIGHT - 3):
        if self.__board[row][column] == piece and self.__board[row + 1][column] == piece and self.__board[row + 2][column] == piece and self.__board[row + 3][column] == piece:
          return True

    for column in range(self.WIDTH - 3):
      for row in range(self.HEIGHT - 3):
        if self.__board[row][column] == piece and self.__board[row + 1][column + 1] == piece and self.__board[row + 2][column + 2] == piece and self.__board[row + 3][column + 3] == piece:
          return True

    for column in range(self.WIDTH - 3):
      for row in range(3, self.HEIGHT):
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

class Player():
  def __init__(self, name):
    self.__name = name


class GUI(UI):
  def __init__(self):
    self.__checkWin = None
    root = Tk()
    root.title("Connect 4")
    frame = Frame(root)
    frame.pack()

    
    Button(
        frame, 
        text = "Help",
        command=self.__showHelp
    ).pack(fill=X)

    Button(
        frame, 
        text = "Play",
        command = self.__playGame
    ).pack(fill=X)

    Button(
        frame, 
        text = "Quit",
        command = self.__quit
    ).pack(fill=X)

    scroll = Scrollbar(frame)
    console = TEXT(frame)
    scroll.pack(side = RIGHT)
    console.pack(side = TOP)

    scroll.config(command = console.yview)
    console.config(yscrollcommand = scroll.set)

    self.__root = root
    self.__console = console


  def run(self):
    print("pass")
  
  def __showHelp(self):
    pass

  def __playGame(self):
    pass

  def __quit(self):
    self.__root.quit()
