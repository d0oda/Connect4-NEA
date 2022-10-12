from Game import *
from tkinter import *
from itertools import product
import colorama
from colorama import Fore, Back
colorama.init(autoreset = True)



class GameError(Exception):
  pass



class UI():
  def displayBoard(self):
    for i in range(1, Game.WIDTH + 1, 1):
      print(i, end = " ")
    print(" ")
    for j in range(Game.HEIGHT):
      print(*self.__board[j], sep = " ")
      print(" ")
    
  def displayTurn(self):
    if self.__playerTurn == 1:
      print(Back.RED + "Player 1's Turn ")
    else:
      print(Back.YELLOW + "Player 2's Turn ")
    return self.__playerTurn



class Terminal(UI):
  def __init__(self):
    self.__game = Game()

  def placeMove(self, column):
    column -= 1
    if Game.validateMove(column):
      for row in range(Game.HEIGHT - 1, -1, -1):
        if self.__board[row][column] == ".":
          self.__board[row][column] = "R" if self.__playerTurn == 1 else "Y"
          Game.turnCounter()
          return
    print(Fore.RED + "Move invalid")

class GUI(UI):
  def __init__(self):
      self.__game_win = None
      root = Tk()
      root.title("Connect 4")
      Grid.rowconfigure(root,0,weight=1)
      Grid.columnconfigure(root,0,weight=1)
      Grid.rowconfigure(root,1,weight=1)
      Grid.rowconfigure(root,2,weight=1)

      helpButton = Button(root, text = "Help", command = self.showHelp)
      playButton = Button(root, text = "Play", command = self.playGame)
      quitButton = Button(root, text = "Quit", command = self.quit)

      helpButton.grid(row=0,column=0,sticky="NSEW")
      playButton.grid(row=1,column=0,sticky="NSEW")
      quitButton.grid(row=2,column=0,sticky="NSEW")

  def showHelp():
    pass

  def playGame(self):
      if self.__game_win:
        return
      self.__game = Game()
      self.__finished = False

      game_win = Toplevel(self.root)
      game_win.title("Game")
      frame = Frame(game_win)
      frame.grid(row = 0, column = 0)

      Grid.columnconfigure(game_win, 0, weight = 1)
      Grid.rowconfigure(game_win, 0, weight = 1)
      frame.grid(row = 0, sticky = N + S + E + W)

      self.__buttons = [[None for _ in range(self.__game.WIDTH + 1)] for _ in range(self.__game.HEIGHT)]
      for row, col in product(range(self.__game.WIDTH + 1), range(self.__game.HEIGHT)):
          b = StringVar()
          b.set(self.__game.at(row+1, col+1))
          self.__buttons[row][col] = b

  def quit():
    pass

  def run(self):
      self.__root.mainloop()