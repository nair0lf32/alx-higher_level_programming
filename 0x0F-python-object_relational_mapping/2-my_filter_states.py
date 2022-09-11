#!/usr/bin/python3
"""Lists all states matching
input filter from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    conn = MySQLdb.connect(user=user, passwd=pwd, db=db)
    csr = conn.cursor()
    csr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
        ORDER BY states.id ASC".format(sys.argv[4]))
    for state in csr.fetchall():
        print(state)
