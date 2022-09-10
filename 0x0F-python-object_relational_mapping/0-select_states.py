#!/usr/bin/python3

'''
a script that lists all states
from the database
'''

import MySQLdb 
from sys import argv

if __name__ == '__main__':

    connect = MySQL.connect(username=argv[1], password=argv[2], database=argv[3], host='localhost', port=3306)

    cursor = connect.cursor()
    cursor = connect.execute('SELECT * FROM states ORDER BY id ASC')
    db = cursor.fetchall()

    for i in db:
        print(i)
    cursor.close()
    db.close()
