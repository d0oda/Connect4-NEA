from Game import *
import tkinter as tk
from itertools import product
import colorama
from colorama import Fore, Back
colorama.init(autoreset = True)


class UI():
  def __init__(self):
    pass
    #self.g = Game()
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

    self.helpButton = tk.Button(self.buttonFrame, text="Help", command=self.clickHelpOnce)
    self.playButton = tk.Button(self.buttonFrame, text="Play", command=self.clickPlayOnce)
    self.quitButton = tk.Button(self.buttonFrame, text="Quit", command=self.quit)

    self.helpButton.grid(row=0, column=0, sticky="NSEW")
    self.playButton.grid(row=1, column=0, sticky="NSEW")
    self.quitButton.grid(row=2, column=0, sticky="NSEW")

    self.buttonFrame.pack(pady=20)

  def clickHelpOnce(self):
    buttonState = str(self.helpButton["state"])
    #print(buttonState)
    if buttonState == "normal":
      #print(buttonState)
      self.showHelp()
      self.helpButton.config(state=tk.DISABLED)
    if buttonState == "disabled":
      #print(buttonState)
      self.helpButton.config(state=tk.NORMAL)
      self.helpWindow.destroy()

  def clickPlayOnce(self):
    buttonState = str(self.playButton["state"])
    #print(buttonState)
    if buttonState == "normal":
      #print(buttonState)
      self.noPlayers()
      self.playButton.config(state=tk.DISABLED)
    if buttonState == "disabled":
      #print(buttonState)
      try:
        self.gameWindow.destroy()
        self.choosePlayers.destroy()
        self.chooseDifficulty.destroy()
        self.playButton.config(state=tk.NORMAL)
      except:
        pass

  def showHelp(self):
    #self.helpButton.config(state=tk.DISABLED)
    self.helpWindow = tk.Toplevel(self.root)
    self.helpWindow.title("Help")

    self.rules = tk.Label(self.helpWindow, text="1) the red counter plays first, click on any column button to place a counter down to the bottom of that column \n 2) the two players alternate until one player gets 4 of their own colours in a row \n 3) the first person to achieve this wins the game!")
    self.rules.pack()

    self.closeHelp = tk.Button(self.helpWindow, text="Close", command=self.clickHelpOnce)
    self.closeHelp.pack()

  def playGame(self, aiPlaying, aiDifficulty):
    #self.playButton.config(state=tk.DISABLED)
    """if self.game_win:
      return"""
    self.g = Game()
    self.ai = AI(self.g)
    self.aiPlaying = aiPlaying
    self.aiDifficulty = aiDifficulty
    self.choosePlayers.destroy()
    self.gameWindow = tk.Toplevel(self.root)
    self.gameWindow.title("Game")
    self.setupGUIBoard(self.gameWindow)
    
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
    #self.turnText = self.canvas.create_text(250, 370, font="Calibri 20 bold", text=f"Player {self.g.getPlayerTurn()}'s turn")
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
    self.canvas.delete(self.turnText)
    self.consoleRow = rowPos + 70
    self.turnText = self.canvas.create_text(250, self.consoleRow, font="Calibri 20 bold", text=f"Player {self.g.getPlayerTurn()}'s turn")


  def colClicked(self, c):
    bg = self.g.getBoard()
    rowPos = self.firstSquareRow
    try:
      if self.g.placeMove(c+1) == False:
        self.canvas.delete(self.turnText)
        self.turnText = self.canvas.create_text(250, self.consoleRow, font="Calibri 20 bold", text=f"Move Invalid")
      else:
        self.drawBoard(self.gameWindow)
        myWin = self.g.checkWin()
        if myWin[0]==1:
          self.canvas.delete(self.turnText)
          self.turnText = self.canvas.create_text(250, self.consoleRow, font="Calibri 20 bold", text=f"Player {3-self.g.getPlayerTurn()} won")
          self.colButtons.destroy()
        if self.g.checkDraw():
          self.canvas.delete(self.turnText)
          self.turnText = self.canvas.create_text(250, self.consoleRow, font="Calibri 20 bold", text=f"Game Drawn")
          self.colButtons.destroy()

    except GameError as e:
      print(e)

    if self.g.playerTurn == 2 and self.aiPlaying == True and self.g.checkWin()[0] == 2:
      if self.aiDifficulty == "easy":
        move = self.ai.findMove()
      elif self.aiDifficulty == "medium":
        move, score = self.ai.miniMax(bg, 2, True)
      elif self.aiDifficulty == "hard":
        move, score = self.ai.miniMax(bg, 5, True)
      self.g.placeMove(move+1)
      self.drawBoard(move+1)

  #     [x,y]=self.g.getPosOfNewPiece()
  #  #   [sc,sr,ec,er] = self.squareDict[x,y]
  #     sx = c * self.COLWIDTH
  #     sy = 0 * self.ROWHEIGHT
  #     ex = (c+1) * self.COLWIDTH
  #     ey = (c+1) * self.ROWHEIGHT
  #     self.canvas.create_oval(sc,sr,ec,er, fill="red", tags=("piece",y))
    


  def setupGUIBoard(self, gamewin):
 #   self.squareDict = {}
    self.g.setupBoard()
    bg = self.g.getBoard()
    colPos = self.firstSquareColumn
    rowPos = self.firstSquareRow
    self.canvas = tk.Canvas(gamewin, width=500, height=500, bg="white")
    self.canvas.pack(side=tk.TOP, fill="both", expand=True)
    for x in range(self.g.HEIGHT):
      for y in range(self.g.WIDTH):
        self.canvas.create_oval(colPos, rowPos, colPos+45, rowPos+45, fill="white", tags=("piece",y))
        colPos += self.COLWIDTH
        #self.squareDict[x][y]=[colPos,rowPos,colPos+45,rowPos+45]
      rowPos += self.ROWHEIGHT
      #self.canvas.create_text(colPos, rowPos, font="Calibri 20 bold", text=i+1)
    

      colPos = self.firstSquareColumn

    self.turnText = self.canvas.create_text(250, rowPos+70, font="Calibri 20 bold", text=f"Player {self.g.getPlayerTurn()}'s turn")

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
      colButton = tk.Button(self.colButtons, command=cmd, text=i+1)
      colButton.grid(row=0, column=i, sticky="NSEW")

    self.colButtons.pack(pady=20)

    self.endGameButton = tk.Button(gamewin, command=self.clickPlayOnce, text="Quit")
    self.endGameButton.pack()

  def noPlayers(self):
    self.choosePlayers = tk.Toplevel(self.root)
    self.choosePlayers.title("Game Setup")

    self.playerConfigButtons = tk.Frame(self.choosePlayers)
    self.playerConfigButtons.rowconfigure(0, weight=1)
    self.playerConfigButtons.rowconfigure(1, weight=1)
    self.playerConfigButtons.rowconfigure(2, weight=1)

    self.onePlayer = tk.Button(self.playerConfigButtons, command= lambda a=True:self.difficulty(a), text="1 Player")
    self.onePlayer.grid(row=0, column=0, sticky="NSEW")

    self.twoPlayer = tk.Button(self.playerConfigButtons, command=lambda a=False:self.playGame(a, None), text="2 Players")
    self.twoPlayer.grid(row=1, column=0, sticky="NSEW")

    self.cancelButton = tk.Button(self.playerConfigButtons, command=self.clickPlayOnce, text="Cancel")
    self.cancelButton.grid(row=2, column=0, sticky="NSEW")

    self.playerConfigButtons.pack(pady=20)

  def difficulty(self, a):
    self.chooseDifficulty = tk.Toplevel(self.root)
    self.chooseDifficulty.title("Game Difficulty Select")

    self.difficultyConfigButtons = tk.Frame(self.chooseDifficulty)
    self.difficultyConfigButtons.rowconfigure(0, weight=1)
    self.difficultyConfigButtons.rowconfigure(1, weight=1)
    self.difficultyConfigButtons.rowconfigure(2, weight=1)
    self.difficultyConfigButtons.rowconfigure(3, weight=1)

    self.easyDifficulty = tk.Button(self.difficultyConfigButtons, command = lambda b="easy":self.playGame(a,b), text="Easy")
    self.easyDifficulty.grid(row=0, column=0, sticky="NSEW")

    self.mediumDifficulty = tk.Button(self.difficultyConfigButtons, command = lambda b="medium":self.playGame(a,b), text="Medium")
    self.mediumDifficulty.grid(row=1, column=0, sticky="NSEW")

    self.hardDifficulty = tk.Button(self.difficultyConfigButtons, command = lambda b="hard":self.playGame(a,b), text="Hard")
    self.hardDifficulty.grid(row=2, column=0, sticky="NSEW")

    self.cancelButton = tk.Button(self.difficultyConfigButtons, command=self.clickPlayOnce, text="Cancel")
    self.cancelButton.grid(row=3, column=0, sticky="NSEW")

    self.difficultyConfigButtons.pack(pady=20)

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