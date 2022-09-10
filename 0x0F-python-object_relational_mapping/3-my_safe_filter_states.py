#!/usr/bin/python3
"""Lists all states starting with 'N' from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    conn = MySQLdb.connect(user=user, passwd=pwd, db=db)
    csr = conn.cursor()
    csr.execute("SELECT * FROM states ORDER BY states.id ASC")
    for state in csr.fetchall():
        if state[1] == sys.argv[4]:
            print(state)
