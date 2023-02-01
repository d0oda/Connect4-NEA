from Game import *

array = [5,6,2,9,4,2,3,5,1,3,7,5,3,6,9]

game = Game()
ai = AI(game)

ai.sortScores(array)

game.setupBoard()
board = game.getBoard()

print(game.openRow(6,board))

centreColumn = [x for x in board[:][int(7/2)]]
print(centreColumn)
"""print(board)
print(board[1][1])"""

import numpy as np
board2 = np.zeros((6,7))
#print(board2)


for i in range(1, 8, 1):
  print(i, end = " ")
print(" ")

#prints board
for j in range(6):
  print(*str(board2[j]).replace('0.', '.'), sep= " ")
  print(" ")