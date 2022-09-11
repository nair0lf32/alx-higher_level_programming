#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    conn = MySQLdb.connect(user=user, passwd=pwd, db=db)
    csr = conn.cursor()
    csr.execute("SELECT citiies.id, cities.name, states.name \
        FROM cities JOIN states \
        ON cities.state_id ORDER BY cities.id ASC")
    for city in csr.fetchall():
        print(city)
