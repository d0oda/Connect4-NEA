from Game import *
import tkinter as tk
from itertools import product
import colorama
from colorama import Fore, Back
colorama.init(autoreset = True)


class UI():
  def __init__(self):
    self.g = Game()
    #self.b = self.g.board
    #self.EMPTY, self.HEIGHT, self.WIDTH, self.REDS, self.YELLOWS = self.g.getBoardAttribute()
    #self.playerTurn = self.g.playerTurn





class Terminal(UI):  
  def displayBoard(self, bd):
    #prints column numbers
    for i in range(1, 8, 1):
      print(i, end = " ")
    print(" ")

    #prints board
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
    #self.__game_win = None
    self.root = tk.Tk()
    self.root.title("Connect 4")
    self.root.geometry("500x500")
    self.firstSquareRow = 50
    self.firstSquareColumn = 55
    self.COLWIDTH = 55
    self.ROWHEIGHT = 50
    self.gameWindow = None
    super().__init__()

###########################################################
#
# CATEGORY A SKILL: ADVANCED OOP
# Used the super() function to inherit the self.g 
# attribute from the parent class UI
#
###########################################################

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
    self.gameWindow = tk.Toplevel(self.root)
    self.gameWindow.title("Game")
    self.setupBoard(self.gameWindow)
    
    #self.board = []
    #print(game.board)
    self.finished = False

    """while True:
        t = self.game.getPlayerTurn()
        print(self.game.getValidColumns())
        myWin = game.checkWin()
        if myWin[0]==5:
            print(Back.BLUE + "The winner is: ", myWin[1])
            break
        if self.game.checkDraw():
            print(Fore.GREEN + "Game Drawn")
            break
        print(self.game.YELLOWS, self.game.REDS)"""

  def drawBoard(self, gamewin):
    colPos = self.firstSquareColumn
    rowPos = self.firstSquareRow
    board = self.g.getBoard()
    #self.canvas = tk.Canvas(gamewin, width=500, height=500, bg="white")
    #self.canvas.pack(fill="both", expand=True)
    for x in range(self.g.HEIGHT):
      for y in range(self.g.WIDTH):
        if board[x][y] == "R":
          self.canvas.create_oval(colPos, rowPos, colPos+45, rowPos+45, fill="red", tags=("piece",y))
        elif board[x][y] == "Y":
          self.canvas.create_oval(colPos, rowPos, colPos+45, rowPos+45, fill="yellow", tags=("piece",y))
        else:
          self.canvas.create_oval(colPos, rowPos, colPos+45, rowPos+45, fill="white", tags=("piece",y))
        colPos += self.COLWIDTH
        #self.squareDict[x][y]=[colPos,rowPos,colPos+45,rowPos+45]
      colPos = self.COLWIDTH
      rowPos += self.ROWHEIGHT
      #self.canvas.create_text(colPos, rowPos, font="Calibri 20 bold", text=i+1)

  def colClicked(self, c):
    try:
      self.g.placeMove(c+1)
      self.drawBoard(self.gameWindow)
      myWin = self.g.checkWin()
      if myWin[0]==5:
        quit()
      if self.g.checkDraw():
        quit()



  #     [x,y]=self.g.getPosOfNewPiece()
  #  #   [sc,sr,ec,er] = self.squareDict[x,y]
  #     sx = c * self.COLWIDTH
  #     sy = 0 * self.ROWHEIGHT
  #     ex = (c+1) * self.COLWIDTH
  #     ey = (c+1) * self.ROWHEIGHT
  #     self.canvas.create_oval(sc,sr,ec,er, fill="red", tags=("piece",y))
    except GameError as e:
      print(e)


  def setupBoard(self, gamewin):
 #   self.squareDict = {}
    self.g.setupBoard()
    bg = self.g.getBoard()
    colPos = self.firstSquareColumn
    rowPos = self.firstSquareRow
    self.canvas = tk.Canvas(gamewin, width=500, height=500, bg="white")
    self.canvas.pack(fill="both", expand=True)
    for x in range(self.g.HEIGHT):
      for y in range(self.g.WIDTH):
        self.canvas.create_oval(colPos, rowPos, colPos+45, rowPos+45, fill="white", tags=("piece",y))
        colPos += self.COLWIDTH
        #self.squareDict[x][y]=[colPos,rowPos,colPos+45,rowPos+45]
      rowPos += self.ROWHEIGHT
      #self.canvas.create_text(colPos, rowPos, font="Calibri 20 bold", text=i+1)
    

      colPos = self.firstSquareColumn

    self.canvas.create_text(250, rowPos+70, font="Calibri 20 bold", text=f"Player {self.g.getPlayerTurn()}'s turn")

    self.colButtons = tk.Frame(gamewin)
    self.colButtons.columnconfigure(0, weight=1)
    self.colButtons.columnconfigure(1, weight=1)
    self.colButtons.columnconfigure(2, weight=1)
    self.colButtons.columnconfigure(3, weight=1)
    self.colButtons.columnconfigure(4, weight=1)
    self.colButtons.columnconfigure(5, weight=1)
    self.colButtons.columnconfigure(6, weight=1)

    for i in range(7):
      cmd = lambda c=i: self.colClicked(c)
      colButton = tk.Button(self.colButtons, command = cmd, text=i+1)
      colButton.grid(row=0, column=i, sticky="NSEW")

    self.colButtons.pack(pady=20)


  def colourIn(self):
    pass


  def quit(self):
    self.root.destroy()
    quit()
    

  def run(self):
    self.root.mainloop()


  def signup(self):
    usernameEntry = tk.Entry(self.root)
    usernameEntry.pack()