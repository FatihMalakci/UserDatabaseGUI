import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()


#Creating our table.
c.execute('''CREATE TABLE users
             (name,sirname,age,phone number)''')

# Inserting an example user.
c.execute("INSERT INTO users VALUES('Fatih','Malakçı','24','5419768923')")

#Saving
conn.commit()

#Closing
conn.close()