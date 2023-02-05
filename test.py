from Game import *

array = [2,4,1,2]

game = Game()
ai = AI(game)

sorted = ai.sortScores(array)
print(sorted[-1])


"""game.setupBoard()
board = game.getBoard()

print(game.openRow(6,board))

centreColumn = [x for x in board[:][int(7/2)]]
print(centreColumn)
print(board)
print(board[1][1])

import numpy as np
board2 = np.zeros((6,7))
#print(board2)


for i in range(1, 8, 1):
  print(i, end = " ")
print(" ")

#prints board
for j in range(6):
  print(*str(board2[j]).replace('0.', '.'), sep= " ")
  print(" ")"""