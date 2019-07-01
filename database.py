import sqlite3


def connectdatabase(database_name):
    conn = sqlite3.connect(f'{database_name}')
    print(f"{database_name} database connected.")
    c = conn.cursor()
    return c

#Creating our table.
def createtable(table):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute(f'''CREATE TABLE {table}
             (name,sirname,age)''')

def insertuser(name,sirname,age):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(?,?,?)",(name,sirname,age))
    print(f'User created Name : {name} Sirname : {sirname} Age : {age}')
    conn.commit()
    conn.close()

def deleteuser(name,sirname):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute(f"DELETE FROM users WHERE name='{name}' AND sirname= '{sirname}'")
    print(f"User {name} {sirname} Deleted.")
    conn.commit()
    conn.close()


def databasename():
    print('Now using the Users.db database')


if __name__ == '__main__':
    gir = input('Enter a database name :')
    # createtable(gir)
    connectdatabase(gir)
