from tkinter import *
from itertools import product
import colorama
from colorama import Fore, Back
colorama.init(autoreset = True)


class GameError(Exception):
  pass

class Game():

  EMPTY = "."
  HEIGHT = 6
  WIDTH = 7
  REDS = 0
  YELLOWS = 0
  #EMPTY = " "

  def __init__(self):
    self.__player1 = Player("Player 1")
    self.__player2 = Player("Player 2")
    self.__playerTurn = 1
    self.__board = [[Game.EMPTY for _ in range(Game.WIDTH + 1)] for _ in range(Game.HEIGHT)]
    #self.__board = []

  

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
        return self.__board[row][col]

  def setupBoard(self):
    for count in range(0, Game.HEIGHT):
      row = [Game.EMPTY] * Game.WIDTH
      self.__board.append(row)

  def displayBoard(self):
    for i in range(1, Game.WIDTH + 1, 1):
      print(i, end = " ")
    print(" ")
    for j in range(Game.HEIGHT):
      print(*self.__board[j], sep = " ")
      print(" ")

  def placeMove(self, column):
    column -= 1
    if self.validateMove(column):
      for row in range(Game.HEIGHT - 1, -1, -1):
        if self.__board[row][column] == ".":
          self.__board[row][column] = "R" if self.__playerTurn == 1 else "Y"
          return
    print(Fore.RED + "Move invalid")

  def validateMove(self, column):
    return column >= 0 and column < Game.WIDTH and self.__board[0][column] == "."

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
    for row in range(Game.HEIGHT):
      for column in range(Game.WIDTH - 3):
        if self.__board[row][column] == piece and self.__board[row][column + 1] == piece and self.__board[row][column + 2] == piece and self.__board[row][column + 3] == piece:
          return True

    for column in range(Game.WIDTH):
      for row in range(Game.HEIGHT - 3):
        if self.__board[row][column] == piece and self.__board[row + 1][column] == piece and self.__board[row + 2][column] == piece and self.__board[row + 3][column] == piece:
          return True

    for column in range(Game.WIDTH - 3):
      for row in range(Game.HEIGHT - 3):
        if self.__board[row][column] == piece and self.__board[row + 1][column + 1] == piece and self.__board[row + 2][column + 2] == piece and self.__board[row + 3][column + 3] == piece:
          return True

    for column in range(Game.WIDTH - 3):
      for row in range(3, Game.HEIGHT):
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


class GUI():
    def __init__(self):
        self.__game_win = None
        root = Tk()
        root.title("Tic Tac Toe")
        frame = Frame(root)
        frame.pack()

        Button(
            frame, 
            text = "Help",
            command=self.__show_help
        ).pack(fill=X)

        Button(
            frame, 
            text = "Play",
            command = self.__play_game
        ).pack(fill=X)

        Button(
            frame, 
            text = "Quit",
            command = self.__quit
        ).pack(fill=X)

        scroll = Scrollbar(frame)
        console = Text(frame, height = 4, width = 50)
        scroll.pack(side = RIGHT, fill = Y)
        console.pack(side = LEFT, fill = Y)

        scroll.config(command = console.yview)
        console.config(yscrollcommand = scroll.set)

        self.__root = root
        self.__console = console

    def __show_help(self):
        pass

    def __play_game(self):
        if self.__game_win:
            return
        self.__game = Game()
        self.__finished = False

        game_win = Toplevel(self.__root)
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


            cmd = lambda r = row, c = col: self.__play(r, c)

            Button(
                frame,
                textvariable = b,
                command = cmd
            ).grid(row = row, column = col, sticky = N + S + E + W)

        for i in range(3):
            Grid.rowconfigure(frame, i, weight = 1)
            Grid.columnconfigure(frame, i, weight = 1)

        self.__game_win = game_win
        Button(game_win, text = "Dismiss", command = self.__dismiss_game_win).grid(row = 1, column = 0)

    def __dismiss_game_win(self):
        self.__game_win.destroy()
        self.__game_win = None

    def __play(self, r, c):
        if self.__finished:
            return

        try:
            self.__game.play(r + 1, c + 1)
        except GameError as e:
            self.__console.insert(END, f"{e}\n")

        for r, c in product(range(3), range(3)):
            self.__buttons[r][c].set(self.__game.at(r + 1, c + 1))

        if self.__game.winner == Game.DRAW:
            self.__console.insert(END, "Game is drawn\n")
            self.__finished = True
        elif self.__game.winner:
            self.__console.insert(END, f"Game is won by {self.__game.winner}\n")
            self.__finished = True


    def __quit(self):
        self.__root.quit()

    def run(self):
        self.__root.mainloop()