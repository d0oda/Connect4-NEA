import sqlite3

"""conn = sqlite3.connect("Connect4.db")
c = conn.cursor()

c.execute("CREATE TABLE Users (username VARCHAR(50) PRIMARY KEY, password VARCHAR(50))")
c.execute("CREATE TABLE Statistics (statsID int PRIMARY KEY, username VARCHAR(50), numWins int, numLosses int, maxWinStreak int)")
c.execute("CREATE TABLE SavedGames (gameID int PRIMARY KEY, player1 VARCHAR(50), player2 VARCHAR(50), gameState)")"""


class DBMS():
  def __init__(self):
    self.conn = sqlite3.connect("Connect4.db")
    c = self.conn.cursor()
    self.existsTable = c.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='{Users}'""")

###########################################################
#
# CATEGORY A SKILL: ADVANCED DATABASE
# 3 tables are linked through use of
# foreign key
#
###########################################################

  def Createtables(self):
    c = self.conn.cursor()
    c.execute('''CREATE TABLE Users
         (username VARCHAR(50) PRIMARY KEY NOT NULL,
         password VARCHAR(50) NOT NULL);''')
    # mode could be 1 or 2 for single player and multiplayer
    # outcome could be 0 for lose, 1 for win and 2 for draw
    c.execute('''CREATE TABLE Statistics
         (statsID INT PRIMARY KEY NOT NULL,
         username VARCHAR(50) NOT NULL,
         date VARCHAR(100) NOT NULL,
         mode INT NOT NULL, 
         outcome INT NOT NULL);''')

    c.execute('''CREATE TABLE SavedGames
         (gameID INT PRIMARY KEY NOT NULL,
         player1 VARCHAR(50) NOT NULL,
         player2 VARCHAR(50) NOT NULL,
         gameState NOT NULL);''')
    c.close()


  def InsertUser(self, username, password):
###########################################################
#
# CATEGORY A SKILL: ADVANCED DATABASE
# use of SQL functions to insert into databases as well as
# updating existing records
#
###########################################################
    c = self.conn.cursor()
    #c.execute(''' INSERT INTO Users (username, password) VALUES (?, ?) ''')
    c.execute(f"INSERT INTO Users (username, password) VALUES ({username}, {password})")
    self.conn.commit()
    c.close()


  def UpdateStats(self, username):
    c = self.conn.cursor()
    c.execute("""SELECT * FROM Statistics WHERE username = %s""")

    c.close()





if __name__ == '__main__':
  database = DBMS()
  database.Createtables()
  database.InsertUser("fei", "1234")