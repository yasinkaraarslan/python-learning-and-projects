import sqlite3

conn = sqlite3.connect("gamelibrary.sqlite")
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Developer ;
DROP TABLE IF EXISTS Genre ;
DROP TABLE IF EXISTS Game ;
DROP TABLE IF EXISTS GameGenre ;

CREATE TABLE Developer ( 
    id INTEGER PRIMARY KEY, 
    name TEXT UNIQUE
);
CREATE TABLE Genre ( 
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);
CREATE TABLE Game (
    id INTEGER PRIMARY KEY,
    title TEXT UNIQUE,
    developer_id INTEGER
);
CREATE TABLE GameGenre (
   game_id INTEGER,
   genre_id INTEGER,
   PRIMARY KEY (game_id, genre_id)
)
''')

lst = [
    ("The last of us", "Naughty Dog", ["Action-Adventure","Horror"]),
    ("Silent hill 2", "Bloober Team", ["Horror","Psychological"]),
    ("God of War", "Santa Monica Studio", ["Action-Adventure","Hack and Slash"])
]

for developer, title, genres in lst :
    cur.execute('''INSERT OR IGNORE INTO Developer (name)
        VALUES (?)''', (developer,))
    cur.execute('SELECT id FROM Developer WHERE name = ? ', (developer,))
    developer_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Game (title, developer_id)
        VALUES (?, ?)''', (title, developer_id))
    cur.execute('SELECT id FROM Game WHERE title = ?', (title,))
    game_id = cur.fetchone()[0]
    for genre in genres :
        cur.execute('''
        INSERT OR IGNORE INTO Genre (name) VALUES (?)''',(genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
        genre_id = cur.fetchone()[0]
        cur.execute('''
        INSERT OR IGNORE INTO GameGenre (game_id, genre_id) VALUES (?, ?)''', (game_id, genre_id))
                                                                                            
conn.commit()

for row in cur.execute('''SELECT Game.title, Developer.name, Genre.name FROM Game JOIN Developer on Game.developer_id = Developer.id JOIN GameGenre ON Game.id = GameGenre.game_id JOIN Genre ON GameGenre.genre_id = Genre.id''') :
    print(str(row[0]), row[1], row[2])