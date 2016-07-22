'''
This script is used for testing how to connect and read the values in the sqlite DB
in ../data ... once this works, it will be plugged into the "start.py" script.

'''

import sqlite3
conn = sqlite3.connect('../data/sql_www_ap.sqlite')

c = conn.cursor()


for row in c.execute('SELECT * FROM sensors'):
    print row




conn.close()
