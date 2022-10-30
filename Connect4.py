from UI import *

def gamemodeOption():
    option = input("Please enter a mode (t: terminal or g: gui) ")
    if option == "t":
      ui = Terminal()
      game = Game()
      game.setupBoard()
      ui.displayBoard()
      while True:
        ui.displayTurn()
        move = int(input("Make a move: "))
        ui.placeMove(move)
        ui.displayBoard()
        if game.checkWin():
            print(Back.BLUE + "The winner is:")
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