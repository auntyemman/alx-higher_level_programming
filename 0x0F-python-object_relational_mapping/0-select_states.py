#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv

    if len(args) != 4:
        print(
            "Usage: {} username password database_name".formatformat(args[0]))
        exit(1)

    username = args[1]
    password = args[2]
    data = args[3]

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    cur.execute('SELECT * FROM states ORDER BY id ASC;')

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
