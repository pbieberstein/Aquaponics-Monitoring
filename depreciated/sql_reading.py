'''
This script is used for testing how to connect and read the values in the sqlite DB
in ../data ... once this works, it will be plugged into the "start.py" script.

'''

import sqlite3
conn = sqlite3.connect('../data/sql_www_ap.sqlite')

c = conn.cursor()

def get_phy_value(id):
    '''
    :param name: "Temp -> 0"; "RH -> 1";  "pH -> 2"; "EC -> 3"
    :return:
    '''
    command = 'SELECT "value_phy" FROM sensors WHERE id == ' + str(id)
    for row in c.execute(command):
        value = row
        value = str(value).replace('(', '').replace(')', '').replace(',', '')
        return value


get_phy_value(3)

'''
for row in c.execute('SELECT "value_phy" FROM sensors WHERE id == "2"'):
    pH = row
    print row
    print str(pH)[1:5]
'''



conn.close()

