from UI import *

def gamemodeOption():
    option = input("Please enter a mode (t: terminal or g: gui) ")
    if option == "t":
      ui = Terminal()
      game = Game()
      game.setupBoard()
      bg = game.getBoard()
      ui.displayBoard(bg)
      while True:
        t = game.getPlayerTurn()
        print(game.getValidColumns())
        ui.displayTurn(t)
        #bg = game.getBoard()
        move = int(input("Make a move: "))
        game.placeMove(move)
        bg = game.getBoard()
        
        ui.displayBoard(bg)
        myWin = game.checkWin()
        if myWin[0]==5:
            print(Back.BLUE + "The winner is: ", myWin[1])
            break
        if game.checkDraw():
            print(Fore.GREEN + "Game Drawn")
            break
        print(game.YELLOWS, game.REDS)
    elif option == "g":
      ui = GUI()

    else:
      gamemodeOption()

if __name__ == "__main__":
  while True:
    gamemodeOption()
    '''game = Game()
    game.gamemodeOption()
    
   '''