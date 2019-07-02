import sqlite3


def connectdatabase(database_name):
    conn = sqlite3.connect(f'{database_name}')
    print(f"{database_name} database connected.")
    c = conn.cursor()
    return c

#Creating our table.
def createtable(table,row1,row2,row3,row4):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute(f'''CREATE TABLE {table}
             ({row1},{row2},{row3},{row4})''')
    conn.commit()
    c.close()

def insertuser(name,sirname,age,phone):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(?,?,?,?)",(name,sirname,age,phone))
    print(f'User created Name : {name} Sirname : {sirname} Age : {age} Phone : {phone}')
    conn.commit()
    conn.close()
    print('Database closed.')

def deleteuser(name,sirname):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    if c.execute(f"SELECT EXISTS(SELECT name from users WHERE name like '%{name}%' AND sirname like '%{sirname}%')").fetchall() == [(1,)]:
        c.execute(f"DELETE FROM users WHERE name LIKE '%{name}%' and sirname LIKE '%{sirname}%'")
        conn.commit()
        conn.close()
        return f"User {name} {sirname} Deleted."
    else:
        return "User Not found"
        conn.commit()
        conn.close()

def checkuser(name,sirname):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    getitem = c.execute(f"SELECT EXISTS(SELECT name from users WHERE name like '%{name}%' AND sirname like '%{sirname}%')").fetchall()
    if getitem == [(1,)]:
        return True
    else:
        return False

def databasename():
    return 'Now using the users.db Database.'

def countusers():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    value = c.execute("SELECT Count(*) FROM users").fetchall()
    conn.close()
    return [x[0] for x in value][0]


if __name__ == '__main__':
    table_name = input('Enter a table name :\n')
    row_1 = input('Enter first row name :\n')
    row_2 = input('Enter second row name :\n')
    row_3 = input('Enter third row name :\n')
    row_4 = input('Enter fourth row name :\n')
    createtable(table_name,row_1,row_2,row_3,row_4)