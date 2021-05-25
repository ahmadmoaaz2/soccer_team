import sqlite3

conn = sqlite3.connect('teams.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE sports_team
          ''')

conn.commit()
conn.close()
