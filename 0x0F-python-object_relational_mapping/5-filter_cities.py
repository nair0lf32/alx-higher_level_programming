#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]
    conn = MySQLdb.connect(user=user, passwd=pwd, db=db)
    csr = conn.cursor()
    csr.execute("SELECT cities.name FROM cities INNER JOIN states \
        ON cities.state_id = states.id WHERE states.name LIKE BINARY '{}' \
        ORDER BY cities.id ASC".format(state_name))
    for city in csr.fetchall():
        print(", ".join(city[0]))
