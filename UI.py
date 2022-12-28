from Game import *
import tkinter as tk
from itertools import product
import colorama
from colorama import Fore, Back
colorama.init(autoreset = True)



class GameError(Exception):
  pass



class UI():
  def __init__(self):
    self.g = Game()
    #self.b = self.g.board
    #self.EMPTY, self.HEIGHT, self.WIDTH, self.REDS, self.YELLOWS = self.g.getBoardAttribute()
    #self.playerTurn = self.g.playerTurn



class Terminal(UI):  
  def displayBoard(self, bd):
    for i in range(1, 8, 1):
      print(i, end = " ")
    print(" ")
    for j in range(6):
      print(*bd[j], sep = " ")
      print(" ")

  def displayTurn(self, t):
    if t == 1:
      print(Back.RED + "Player 1's Turn ")
    else:
      print(Back.YELLOW + "Player 2's Turn ")
    return t

  def signup(self, mode):
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")
    while True:
      password2 = input("Please repeat your password: ")
      if password == password2:
        return username, password
  
  def userCreated(self, usr):
    print(f"User {usr} created successfully")

class GUI(UI):
  def __init__(self):
      self.__game_win = None
      self.root = tk.Tk()
      self.root.title("Connect 4")
      self.root.geometry("500x500")

      self.label = tk.Label(self.root, text="Connect 4")
      self.label.pack(padx=20, pady=20)

      self.buttonFrame = tk.Frame(self.root)
      self.buttonFrame.columnconfigure(0, weight=1)
      self.buttonFrame.columnconfigure(1, weight=1)
      self.buttonFrame.columnconfigure(2, weight=1)

      helpButton = tk.Button(self.buttonFrame, text="Help", command=self.showHelp)
      playButton = tk.Button(self.buttonFrame, text="Play", command=self.playGame)
      quitButton = tk.Button(self.buttonFrame, text="Quit", command=self.quit)

      helpButton.grid(row=0, column=0, sticky="NSEW")
      playButton.grid(row=1, column=0, sticky="NSEW")
      quitButton.grid(row=2, column=0, sticky="NSEW")

      self.buttonFrame.pack(pady=20)

  def showHelp():
    pass

  def playGame(self):
      if self.__game_win:
        return
      self.__game = Game()
      self.board = []
      self.__finished = False
      firstSquareRow = 50
      firstSquareColumn = 55
      colPos = firstSquareColumn
      rowPos = firstSquareRow

      game_win = tk.Toplevel(self.root)
      game_win.title("Game")

      for x in range(self.__game.HEIGHT):
        squareList = []
        for y in range(self.__game.WIDTH):
          square = tk.Canvas.create_oval(colPos, rowPos, colPos+45, rowPos+45, fill="white", tags=("piece",y))
          colPos += 55
          squareList.append(square)
        rowPos += 50
        colPos = firstSquareColumn
        self.board.append(squareList)
      
    

  def quit():
    pass

  def run(self):
      self.__root.mainloop()

  def signup(self):
    usernameEntry = tk.Entry(self.root)
    usernameEntry.pack()