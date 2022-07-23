from UI import *

def gamemodeOption():
    option = input("Please enter a mode (t: terminal or g: gui) ")
    if option == "t":
      ui = Game()
      ui.setupBoard()
      ui.displayBoard()
      while True:
        ui.displayTurn()
        move = int(input("Make a move: "))
        ui.placeMove(move)
        ui.displayBoard()
        if ui.checkWin():
            print(Back.BLUE + "The winner is:")
            break
        if ui.checkDraw():
            print(Fore.GREEN + "Game Drawn")
            break
        ui.turnCounter()
        print(ui.YELLOWS, ui.REDS)
        if not ui.playAgain():
            break
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