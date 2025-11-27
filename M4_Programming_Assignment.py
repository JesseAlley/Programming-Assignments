# 11.1 Create a file called zoo.py. In it, define a function called hours()
# that prints the string 'Open 9-5 daily'. Then, use the interactive interpreter
# to import the zoo module and call its hours() function.
import zoo
zoo.hours()


# 11.2 In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
import zoo as menagerie
menagerie.hours()

#11.3 Staying in the interpreter, import the hours() function from zoo directly and call it.
from zoo import hours
hours()

# 16.4 Use the sqlite3 module to create a SQLite database called books.db
# and a table called books with these fields: title (text), author (text),
# and year (integer).

# 16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 16.4.
# As in 16.6, select and print the title column from the book table in alphabetical order.



import sqlite3

#create database
conn = sqlite3.connect("books.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS books
    (title TEXT,
    author TEXT,
    year INTEGER)
    """)
conn.commit()

#populate database
ins = 'INSERT INTO books (title, author, year) VALUES (?, ?, ?)'
cur.execute(ins, ("The Weirdstone of Brisingamen", "Alan Garner", 1960))
cur.execute(ins, ('Perdido Street Station', 'China Mieville', 2000))
cur.execute(ins, ('Thud!', 'Terry Pratchett', 2005))

conn.commit()
conn.close()

#print database using sqlalchemy

import sqlalchemy as sa

conn = sa.create_engine('sqlite:///books.db')

# SELECT titles in alphabetical order
result = conn.execute("SELECT title FROM books ORDER BY title ASC")

for row in result:
    print(row[0])

conn.close()