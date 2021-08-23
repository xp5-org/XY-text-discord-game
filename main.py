import sqlite3



class Player:
  def __init__(self, name, playerid):
    self.name = name
    self.playerid = playerid
    self.position_x = 0
    self.position_y = 0
    self.inventory = []
    self.health = 0
    self.score = 0
    self.sql_read()

  def currentlocation(self):
    pos = [self.position_x, self.position_y]
    print(self.name, pos)
    return pos

  def sql_read(self):
    con = sqlite3.connect("PlayerDB.db")
    cursorObj = con.cursor()
    cursorObj.execute('''SELECT * FROM playerinfo WHERE id = ?''', (str(self.playerid)))
    rows = cursorObj.fetchall()
    # print('PlayerID', rows[0][0])
    # print('Player Name', rows[0][1])
    # print('Player X-Pos', rows[0][2])
    # print('Player Y-Pos', rows[0][3])
    self.position_x = rows[0][2]
    self.position_y = rows[0][3]
    self.inventory = (rows[0][4]).strip('][').split(', ')
    # print('name:', self.name, ' , ', 'inventory: ', self.inventory)
    self.health = rows[0][5]
    self.score = rows[0][6]

  def sql_update(self):
    con = sqlite3.connect("PlayerDB.db")
    cursorObj = con.cursor()
    print('DEBUG: Num of rows updated: ', cursorObj.execute('''UPDATE playerinfo SET position_x = ? , position_y = ? WHERE id = ?''', (self.position_x, self.position_y, str(self.playerid))).rowcount)
    con.commit()
    print('update statement ran for : ', self.position_x, self.position_y, self.playerid)
    sql_fetch(con)



  def move(self, command):
    if command == 'up':
        self.position_y += 1
        print('up')
    if command == 'down':
        self.position_y -= 1
        print('down')
    if command == 'left':
        self.position_x -= 1
        print('left')
    if command == 'right':
        self.position_x += 1
        print('right')
    print('movement command executed inside class')
    self.sql_update()


  def action(self, command):
    if command == 'open':
        print('open action performed at ', [self.position_x, self.position_y], 'block-id-command-here')
    if command == 'close':
        print('close action performed at ', [self.position_x, self.position_y])

  def block_id_commands(x_yargs_list):
    output = fetch_sql_for_location(x, y)
    blockname = output['block-name']
    blocktype = output['block-type']
    return blockname






# SQL for store load player info

def sql_connection(tablename):
    try:
        con = sqlite3.connect(tablename)
        return con
    except Error:
        print(Error)


def sql_create_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE playerinfo(id, name, position_x, position_y, inventory, health, score)")
    con.commit()

def sql_newplayer(con, id, name):
    # bug - doesnt check if duplicate ID exists
    cursorObj = con.cursor()
    tablename = "playerinfo"
    playerid = id # should be N+1
    playername = name
    position_x = '0'
    position_y = '0'
    # inventory = {"apple": "5", "pear": "2"}
    inventory = str(['apple', '5', 'pear', '2'])
    health = '90'
    score = '12'
    sectorcolumns = (playerid, playername, position_x, position_y, inventory, health, score)
    cursorObj.execute('INSERT INTO ' + tablename + '(id, name, position_x, position_y, inventory, health, score) VALUES(?, ?, ?, ?, ?, ?, ?)', sectorcolumns)
    con.commit()

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM playerinfo')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)




con = sql_connection("PlayerDB.db")
# sql_create_table(con) #create table
# sql_newplayer(con, '0', 'jack') # insert starting values for Player-0
# sql_newplayer(con, '1', 'jill') # insert starting values for Player-1
#sql_fetch(con) # show these values
sql_fetch(con)


# exit()

# create player john ID0 & jill ID1 starting at 0,0
p1 = Player("Jack", 0)
p2 = Player("Jill", 1)

# example of how to print players name
print(p1.name)

# force-set location of player's x
# p1.position_x = 1

# print just one specific value
print(p1.position_x) 

# print the current location x/y
p1.currentlocation()

# move player 1 left 3 spaces
p1.move('left')
p1.move('left')
p1.move('left')
p1.move('down')
sql_fetch(con)
# move player 2 right 3 spaces
p2.move('right')
p2.move('right')
p2.move('right')
p2.move('up')



p1.sql_read()
p2.sql_read()


iter = 0
while iter < 50:
    p2.move('up')
    p1.move('left')
    iter += 1
    


# print x/y of player 1 and player 2 
p1.currentlocation()
p2.currentlocation()
sql_fetch(con)

p1.action('open')


