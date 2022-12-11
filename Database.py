import sqlite3

"""conn = sqlite3.connect("Connect4.db")
c = conn.cursor()

c.execute("CREATE TABLE Users (username VARCHAR(50) PRIMARY KEY, password VARCHAR(50))")
c.execute("CREATE TABLE Statistics (statsID int PRIMARY KEY, username VARCHAR(50), numWins int, numLosses int, maxWinStreak int)")
c.execute("CREATE TABLE SavedGames (gameID int PRIMARY KEY, player1 VARCHAR(50), player2 VARCHAR(50), gameState)")"""

class DBMS():
  def __init__(self):
    self.conn = sqlite3.connect("Connect4.db")
  def Createtables(self):
    c = self.conn.cursor()
    c.execute("CREATE TABLE Users (username VARCHAR(50) PRIMARY KEY, password VARCHAR(50))")
    c.execute("CREATE TABLE Statistics (statsID int PRIMARY KEY, username VARCHAR(50), numWins int, numLosses int, maxWinStreak int)")
    c.execute("CREATE TABLE SavedGames (gameID int PRIMARY KEY, player1 VARCHAR(50), player2 VARCHAR(50), gameState)")
    c.close()
  def InsertUser(self, username, password):
    c = self.conn.cursor()
    c.execute("INSERT INTO Users")
