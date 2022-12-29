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
    self.firstSquareRow = 50
    self.firstSquareColumn = 55
    self.game = Game()

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
    """if self.game_win:
      return"""
    game_win = tk.Toplevel(self.root)
    game_win.title("Game")
    self.setupBoard(game_win)
    
    #self.board = []
    #print(game.board)
    self.finished = False

    while True:
        t = self.game.getPlayerTurn()
        print(self.game.getValidColumns())
        #ui.displayTurn(t) display in console
        #move = int(input("Make a move: ")) input in GUI
        game.placeMove(move)
        bg = game.getBoard()
        
        ui.displayBoard(bg)
        myWin = game.checkWin()
        if myWin[0]==5:
            print(Back.BLUE + "The winner is: ", myWin[1])
            break
        if self.game.checkDraw():
            print(Fore.GREEN + "Game Drawn")
            break
        print(self.game.YELLOWS, self.game.REDS)

  def setupBoard(self, game_win):
    self.game.setupBoard()
    bg = self.game.getBoard()
    colPos = self.firstSquareColumn
    rowPos = self.firstSquareRow
    canvas = tk.Canvas(game_win, width=500, height=500, bg="white")
    canvas.pack()
    for x in range(self.game.HEIGHT):
      squareList = []
      for y in range(self.game.WIDTH):
        canvas.create_oval(colPos, rowPos, colPos+45, rowPos+45, fill="white", tags=("piece",y))
        colPos += 55
      rowPos += 50

      colPos = self.firstSquareColumn
      #self.board.append(squareList)

    self.colButtons = tk.Frame(game_win)
    self.colButtons.columnconfigure(0, weight=1)
    self.colButtons.columnconfigure(1, weight=1)
    self.colButtons.columnconfigure(2, weight=1)
    self.colButtons.columnconfigure(3, weight=1)
    self.colButtons.columnconfigure(4, weight=1)
    self.colButtons.columnconfigure(5, weight=1)
    self.colButtons.columnconfigure(6, weight=1)

    for i in range(7):
      colButton = tk.Button(self.colButtons, text=i+1)
      colButton.grid(row=0, column=i, sticky="NSEW")

    self.colButtons.pack(pady=20)
      
  def quit(self):
    self.root.destroy()
    

  def run(self):
    self.root.mainloop()

  def signup(self):
    usernameEntry = tk.Entry(self.root)
    usernameEntry.pack()