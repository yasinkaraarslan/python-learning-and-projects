import sqlite3

conn = sqlite3.connect("ages.sqlite")
cur = conn.cursor()

cur.executescript('''
  DROP TABLE IF EXISTS Ages;
  CREATE TABLE Ages (
   name VARCHAR(128), 
   age INTEGER
)
''')

cur.executescript('''
   DELETE FROM Ages;
   INSERT INTO Ages (name, age) VALUES ('Derrin', 14);
   INSERT INTO Ages (name, age) VALUES ('Dhavid', 37);
   INSERT INTO Ages (name, age) VALUES ('Abbiegail', 19);
   INSERT INTO Ages (name, age) VALUES ('Aiyana', 38);
   INSERT INTO Ages (name, age) VALUES ('Zak', 16);
''')

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')

row = cur.fetchone()

if row :
    print("HEX", row[0])

conn.commit()
conn.close()