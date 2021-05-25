import sqlite3

conn = sqlite3.connect('teams.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE sports_team
          (id INTEGER PRIMARY KEY ASC, 
           name VARCHAR(250) NOT NULL,
           email VARCHAR(250) NOT NULL,
           phone_number INTEGER NOT NULL,
           type VARCHAR(10) NOT NULL,
           date_of_birth VARCHAR(30) NOT NULL,
           position VARCHAR(30),
           salary INTEGER,
           jersey_number INTEGER
           )
          ''')

conn.commit()
conn.close()
