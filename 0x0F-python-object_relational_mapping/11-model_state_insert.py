#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    session = Session(bind=engine)
    obj = State(name="Louisiana")
    session.add(obj)
    session.commit()
    print(obj.id)
    session.close()
