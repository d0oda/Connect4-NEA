from Game import *

array = [5,6,2,9,4,2,3,5,1,3,7,5,3,6,9]

game = Game()
ai = AI(game)

ai.sortScores(array)

print(array)