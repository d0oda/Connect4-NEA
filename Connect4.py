from UI import *
from Database import *


def gamemodeOption():
    database = DBMS()
    if database.existsTable is None:
      database.Createtables()
    else:
      pass
    
    option = input("Please enter a mode (t: terminal or g: gui), or quit (q) ")
    if option == "t":
      players = int(input("1 or 2 human players? "))
      ui = Terminal()
      game = Game()
      ai = AI(game)
      game.setupBoard()
      bg = game.getBoard()
      ui.displayBoard(bg)
      '''(usr, psw) = ui.signup()
      database.InsertUser(username=usr, password=psw)
      ui.userCreated(usr)'''
      if players == 1:
        while True:
          #print(f"1 {game.board}")
          t = game.getPlayerTurn()
          ui.displayTurn(t)
          #print(f"2 {game.board}")
          if t == 1:
            move = int(input("Make a move: "))
          elif t == 2:
            move = ai.findMove()
          #print(f"3 {game.board}")
          game.placeMove(move)
          bg = game.getBoard()
          myWin = game.checkWin()
          #print(f"4 {game.board}")
          ui.displayBoard(bg)
          if myWin[0]==1:
              print(Back.BLUE + "The winner is: ", myWin[1])
              break
          if game.checkDraw():
              print(Back.GREEN + "Game Drawn")
              break

      elif players == 2:
        while True:
          t = game.getPlayerTurn()
          #print(game.getValidColumns())
          ui.displayTurn(t)
          #bg = game.getBoard()
          move = int(input("Make a move: "))
          game.placeMove(move)
          bg = game.getBoard()
          #result = ai.miniMax()
          #print(result)
          ui.displayBoard(bg)
          myWin = game.checkWin()
          if myWin[0]==1:
              print(Back.BLUE + "The winner is: ", myWin[1])
              break
          if game.checkDraw():
              print(Back.GREEN + "Game Drawn")
              break
          #print(game.YELLOWS, game.REDS)
    elif option == "g":
      ui = GUI()

    elif option == "q":
      quit()


    else:
      gamemodeOption()





if __name__ == "__main__":
  while True:
    gamemodeOption()
    '''game = Game()
    game.gamemodeOption()
    
   '''